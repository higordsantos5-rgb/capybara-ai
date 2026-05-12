"""MCP trace records."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.mcp.permissions import MCPPermissions


@dataclass(frozen=True, slots=True)
class MCPTrace:
    """Trace for one MCP tool call."""

    tool_name: str
    server_name: str
    scope: str
    permissions: MCPPermissions
    status: str
