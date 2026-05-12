"""MCP permission declarations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MCPPermissions:
    """Explicit operation flags for one MCP tool."""

    read: bool = False
    write: bool = False
    edit: bool = False
    execute: bool = False
    mutates_external_state: bool = False

    def names(self) -> list[str]:
        names: list[str] = []
        if self.read:
            names.append("read")
        if self.write:
            names.append("write")
        if self.edit:
            names.append("edit")
        if self.execute:
            names.append("execute")
        if self.mutates_external_state:
            names.append("mutates_external_state")
        return names

    def includes(self, required: MCPPermissions) -> bool:
        return (
            (not required.read or self.read)
            and (not required.write or self.write)
            and (not required.edit or self.edit)
            and (not required.execute or self.execute)
            and (not required.mutates_external_state or self.mutates_external_state)
        )
