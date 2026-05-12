"""Non-real provider adapters that declare limitations honestly."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.core.errors import AdapterStatusError, ProviderUnavailableError
from capybara_ai.core.execution import ExecutionRequest
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import AdapterStatus
from capybara_ai.providers.base import ProviderResponse


@dataclass(slots=True)
class LimitedProviderAdapter:
    """Adapter used for experimental or contract providers in the base package."""

    provider: str
    status: AdapterStatus
    limitations: tuple[str, ...]
    requires_credentials: bool = True

    def is_available(self) -> bool:
        return self.status is not AdapterStatus.CONTRACT

    def execute(
        self,
        request: ExecutionRequest,
        card: ModelCard,
        credential: str | None,
        metadata: ExecutionMetadata,
    ) -> ProviderResponse:
        del request, card, credential, metadata
        if self.status is AdapterStatus.CONTRACT:
            raise AdapterStatusError(
                "Contract adapters cannot execute as real providers.",
                details={"provider": self.provider, "status": self.status.value},
            )
        raise ProviderUnavailableError(
            "Experimental adapter has no runtime implementation in the base install.",
            details={"provider": self.provider, "status": self.status.value},
        )
