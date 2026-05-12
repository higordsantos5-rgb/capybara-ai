"""MCP client and policy gate."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from capybara_ai.core.errors import MCPConfigurationError, MCPExecutionError, MCPPermissionError
from capybara_ai.core.metadata import ExecutionMetadata, MCPCallRecord
from capybara_ai.mcp.config import MCPClientConfig
from capybara_ai.mcp.tools import MCPToolConfig, MCPToolRequest, MCPToolResult

ToolExecutor = Callable[[dict[str, Any]], Any]


@dataclass(slots=True)
class MCPClient:
    """MCP client wrapper with default-deny policy enforcement."""

    config: MCPClientConfig
    local_executors: dict[str, ToolExecutor] = field(default_factory=dict)

    def register_local_executor(self, tool_name: str, executor: ToolExecutor) -> None:
        self.local_executors[tool_name] = executor

    def execute(self, request: MCPToolRequest, metadata: ExecutionMetadata) -> MCPToolResult:
        tool = self._authorize(request)
        record = MCPCallRecord(
            tool_name=tool.name,
            server_name=tool.server_name,
            permissions=tool.permissions.names(),
            read=tool.permissions.read,
            write=tool.permissions.write,
            edit=tool.permissions.edit,
            execute=tool.permissions.execute,
            mutates_external_state=tool.permissions.mutates_external_state,
            status="authorized",
        )
        metadata.mcp_calls.append(record)
        metadata.external_read = metadata.external_read or tool.permissions.read
        metadata.external_write = metadata.external_write or tool.permissions.write
        metadata.external_edit = metadata.external_edit or tool.permissions.edit
        metadata.external_execute = metadata.external_execute or tool.permissions.execute

        executor = self.local_executors.get(tool.name)
        if executor is None:
            record.status = "no_executor"
            raise MCPExecutionError(
                "MCP tool is authorized but no executor is registered.",
                details={"tool": tool.name, "server": tool.server_name},
            )
        try:
            output = executor(request.arguments)
        except Exception as exc:  # noqa: BLE001
            record.status = "failed"
            raise MCPExecutionError(
                "MCP tool execution failed.",
                details={
                    "tool": tool.name,
                    "server": tool.server_name,
                    "error_type": type(exc).__name__,
                },
            ) from exc
        record.status = "succeeded"
        return MCPToolResult(tool_name=tool.name, output=output)

    async def execute_stdio_sdk(
        self, request: MCPToolRequest, metadata: ExecutionMetadata
    ) -> MCPToolResult:
        """Execute a stdio MCP tool through the optional official SDK."""

        tool = self._authorize(request)
        server = self.config.servers.get(tool.server_name)
        if server is None or not server.enabled:
            raise MCPConfigurationError(
                "MCP server is not configured or enabled.",
                details={"server": tool.server_name},
            )
        if server.transport != "stdio" or server.command is None:
            raise MCPConfigurationError(
                "Only configured stdio MCP servers can use execute_stdio_sdk.",
                details={
                    "server": tool.server_name,
                    "transport": server.transport if server else None,
                },
            )
        try:
            from mcp import ClientSession, StdioServerParameters  # type: ignore[import-not-found]
            from mcp.client.stdio import stdio_client  # type: ignore[import-not-found]
        except ImportError as exc:
            raise MCPConfigurationError(
                "MCP SDK is not installed. Install capybara-ai[mcp].",
                details={"server": tool.server_name},
            ) from exc
        metadata.mcp_calls.append(
            MCPCallRecord(
                tool_name=tool.name,
                server_name=tool.server_name,
                permissions=tool.permissions.names(),
                read=tool.permissions.read,
                write=tool.permissions.write,
                edit=tool.permissions.edit,
                execute=tool.permissions.execute,
                mutates_external_state=tool.permissions.mutates_external_state,
                status="authorized",
            )
        )
        params = StdioServerParameters(command=server.command, args=list(server.args))
        try:
            async with stdio_client(params) as (read, write), ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool.name, request.arguments)
        except Exception as exc:  # noqa: BLE001
            raise MCPExecutionError(
                "MCP SDK tool execution failed.",
                details={
                    "tool": tool.name,
                    "server": tool.server_name,
                    "error_type": type(exc).__name__,
                },
            ) from exc
        return MCPToolResult(tool_name=tool.name, output=result)

    def execute_stdio_sdk_sync(
        self, request: MCPToolRequest, metadata: ExecutionMetadata
    ) -> MCPToolResult:
        return asyncio.run(self.execute_stdio_sdk(request, metadata))

    def _authorize(self, request: MCPToolRequest) -> MCPToolConfig:
        if not self.config.enabled:
            raise MCPConfigurationError("MCP is not configured.", details={"tool": request.name})
        tool = self.config.tool(request.name)
        if tool is None or not tool.allowlisted:
            raise MCPPermissionError("MCP tool is not allowlisted.", details={"tool": request.name})
        server = self.config.servers.get(tool.server_name)
        if server is None or not server.enabled:
            raise MCPConfigurationError(
                "MCP server is not configured or enabled.",
                details={"server": tool.server_name, "tool": tool.name},
            )
        if not tool.permissions.includes(request.required_permissions):
            raise MCPPermissionError(
                "MCP tool does not grant required permissions.",
                details={"tool": tool.name, "required": request.required_permissions.names()},
            )
        return tool
