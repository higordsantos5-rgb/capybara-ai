"""MCP client configuration."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.mcp.tools import MCPToolConfig


@dataclass(frozen=True, slots=True)
class MCPServerConfig:
    """Configured MCP server/connector."""

    name: str
    transport: str
    command: str | None = None
    args: tuple[str, ...] = ()
    url: str | None = None
    enabled: bool = False


@dataclass(slots=True)
class MCPClientConfig:
    """Project-level MCP configuration."""

    enabled: bool = False
    servers: dict[str, MCPServerConfig] = field(default_factory=dict)
    tools: dict[str, MCPToolConfig] = field(default_factory=dict)

    def tool(self, name: str) -> MCPToolConfig | None:
        return self.tools.get(name)
