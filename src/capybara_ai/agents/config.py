"""Agent configuration."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.core.types import ContextType


@dataclass(frozen=True, slots=True)
class AgentConfig:
    """Explicit agent configuration."""

    name: str
    instructions: str = ""
    preferred_model: str | None = None
    allowed_providers: frozenset[str] = field(default_factory=frozenset)
    allowed_models: frozenset[str] = field(default_factory=frozenset)
    accepted_context_types: frozenset[ContextType] = field(
        default_factory=lambda: frozenset(
            {ContextType.TEXT, ContextType.MARKDOWN, ContextType.CODE}
        )
    )
    allowed_tools: frozenset[str] = field(default_factory=frozenset)
    allowed_mcp_tools: frozenset[str] = field(default_factory=frozenset)
    max_steps: int = 1
    error_policy: str = "structured_error"
