"""Provider adapter port."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.core.execution import ExecutionRequest
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import AdapterStatus


@dataclass(frozen=True, slots=True)
class ProviderResponse:
    """Normalized provider response."""

    output: Any
    raw_metadata: dict[str, Any] = field(default_factory=dict)


class ProviderAdapter(Protocol):
    """Port implemented by all provider adapters."""

    provider: str
    status: AdapterStatus
    requires_credentials: bool
    limitations: tuple[str, ...]

    def is_available(self) -> bool:
        """Return whether the adapter dependency/runtime is available."""

    def execute(
        self,
        request: ExecutionRequest,
        card: ModelCard,
        credential: str | None,
        metadata: ExecutionMetadata,
    ) -> ProviderResponse:
        """Execute the provider call."""
