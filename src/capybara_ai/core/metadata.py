"""Execution metadata with secret redaction."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, cast

from capybara_ai.core.errors import CapybaraAIError, redact_value


@dataclass(slots=True)
class RoutingDecision:
    """A model/provider considered by the router."""

    provider: str
    model: str
    accepted: bool
    reason: str


@dataclass(slots=True)
class BlockRecord:
    """A validation block that prevented external execution."""

    code: str
    reason: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class MCPCallRecord:
    """Trace for an MCP tool call."""

    tool_name: str
    server_name: str
    permissions: list[str]
    read: bool = False
    write: bool = False
    edit: bool = False
    execute: bool = False
    mutates_external_state: bool = False
    status: str = "pending"


@dataclass(slots=True)
class ExecutionMetadata:
    """Minimum structured metadata required by the V1 specs."""

    agent_name: str | None = None
    provider_selected: str | None = None
    model_selected: str | None = None
    routing_decisions: list[RoutingDecision] = field(default_factory=list)
    required_capabilities: list[str] = field(default_factory=list)
    satisfied_capabilities: list[str] = field(default_factory=list)
    context_items: list[dict[str, Any]] = field(default_factory=list)
    validations: list[str] = field(default_factory=list)
    blocks: list[BlockRecord] = field(default_factory=list)
    fallback_applied: bool = False
    mcp_calls: list[MCPCallRecord] = field(default_factory=list)
    external_read: bool = False
    external_write: bool = False
    external_edit: bool = False
    external_execute: bool = False
    error: dict[str, Any] | None = None

    def add_decision(self, provider: str, model: str, accepted: bool, reason: str) -> None:
        self.routing_decisions.append(RoutingDecision(provider, model, accepted, reason))

    def add_block(self, code: str, reason: str, details: dict[str, Any] | None = None) -> None:
        self.blocks.append(BlockRecord(code, reason, redact_value(details or {})))

    def set_error(self, error: CapybaraAIError) -> None:
        self.error = error.to_dict()

    def to_dict(self) -> dict[str, Any]:
        return cast(
            dict[str, Any],
            redact_value(
                {
                    "agent_name": self.agent_name,
                    "provider_selected": self.provider_selected,
                    "model_selected": self.model_selected,
                    "routing_decisions": [asdict(decision) for decision in self.routing_decisions],
                    "required_capabilities": self.required_capabilities,
                    "satisfied_capabilities": self.satisfied_capabilities,
                    "context_items": self.context_items,
                    "validations": self.validations,
                    "blocks": [asdict(block) for block in self.blocks],
                    "fallback_applied": self.fallback_applied,
                    "mcp_calls": [asdict(call) for call in self.mcp_calls],
                    "external_read": self.external_read,
                    "external_write": self.external_write,
                    "external_edit": self.external_edit,
                    "external_execute": self.external_execute,
                    "error": self.error,
                }
            ),
        )
