"""Execution request and result contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from capybara_ai.core.errors import CapybaraAIError
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import Capability


@dataclass(slots=True)
class ExecutionRequest:
    """A normalized request before provider execution."""

    prompt: str
    context: list[Any] = field(default_factory=list)
    required_capabilities: set[Capability] = field(default_factory=set)
    stream: bool = False
    structured_schema: dict[str, Any] | None = None
    mcp_tool_requests: list[Any] = field(default_factory=list)
    preferred_model: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def all_required_capabilities(self) -> set[Capability]:
        capabilities = set(self.required_capabilities)
        capabilities.add(Capability.TEXT)
        if self.stream:
            capabilities.add(Capability.STREAMING)
        if self.structured_schema is not None:
            capabilities.add(Capability.STRUCTURED_OUTPUT)
        return capabilities


@dataclass(slots=True)
class ExecutionResult:
    """Structured success, block, or error result."""

    success: bool
    output: Any = None
    metadata: ExecutionMetadata = field(default_factory=ExecutionMetadata)
    error: CapybaraAIError | None = None
    blocked: bool = False

    @classmethod
    def ok(cls, output: Any, metadata: ExecutionMetadata) -> ExecutionResult:
        return cls(success=True, output=output, metadata=metadata)

    @classmethod
    def fail(cls, error: CapybaraAIError, metadata: ExecutionMetadata) -> ExecutionResult:
        metadata.set_error(error)
        return cls(success=False, metadata=metadata, error=error)

    @classmethod
    def block(cls, error: CapybaraAIError, metadata: ExecutionMetadata) -> ExecutionResult:
        metadata.set_error(error)
        metadata.add_block(error.code, error.message, error.details)
        return cls(success=False, metadata=metadata, error=error, blocked=True)

    def to_dict(self) -> dict[str, Any]:
        return {
            "success": self.success,
            "blocked": self.blocked,
            "output": self.output,
            "error": self.error.to_dict() if self.error else None,
            "metadata": self.metadata.to_dict(),
        }
