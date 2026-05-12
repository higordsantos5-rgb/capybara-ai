"""MCP tool contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from capybara_ai.mcp.permissions import MCPPermissions


@dataclass(frozen=True, slots=True)
class MCPToolConfig:
    """Explicitly configured MCP tool."""

    name: str
    server_name: str
    scope: str
    permissions: MCPPermissions
    allowlisted: bool = False
    description: str = ""


@dataclass(frozen=True, slots=True)
class MCPToolRequest:
    """Request to execute one MCP tool."""

    name: str
    arguments: dict[str, Any] = field(default_factory=dict)
    required_permissions: MCPPermissions = field(default_factory=MCPPermissions)


@dataclass(frozen=True, slots=True)
class MCPToolResult:
    """Normalized MCP tool result."""

    tool_name: str
    output: Any
    metadata: dict[str, Any] = field(default_factory=dict)
