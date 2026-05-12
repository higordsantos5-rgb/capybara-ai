"""Functional fake provider for tests and examples."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.core.execution import ExecutionRequest
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers.base import ProviderResponse


@dataclass(slots=True)
class FakeProviderAdapter:
    """A deterministic mock adapter that never calls external services."""

    response_prefix: str = "fake"
    provider: str = ProviderName.FAKE.value
    status: AdapterStatus = AdapterStatus.MOCK
    requires_credentials: bool = False
    limitations: tuple[str, ...] = ("No external provider call.", "No real streaming support.")

    def is_available(self) -> bool:
        return True

    def execute(
        self,
        request: ExecutionRequest,
        card: ModelCard,
        credential: str | None,
        metadata: ExecutionMetadata,
    ) -> ProviderResponse:
        del card, credential
        metadata.validations.append("fake_provider_executed_without_external_call")
        return ProviderResponse(output=f"{self.response_prefix}: {request.prompt}")
