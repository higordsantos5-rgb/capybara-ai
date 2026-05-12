"""Explicit capability registry."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.core.errors import MissingCapabilityError
from capybara_ai.core.types import AdapterStatus, Capability, ProviderName


@dataclass(slots=True)
class CapabilityRegistry:
    """Registry of known models. Known never means enabled."""

    _cards: dict[tuple[str, str], ModelCard] = field(default_factory=dict)

    def register(self, card: ModelCard) -> None:
        self._cards[(card.provider, card.model_id)] = card

    def get(self, provider: str, model_id: str) -> ModelCard | None:
        return self._cards.get((provider, model_id))

    def all_cards(self) -> list[ModelCard]:
        return list(self._cards.values())

    def require(self, provider: str, model_id: str, required: set[Capability]) -> ModelCard:
        card = self.get(provider, model_id)
        if card is None:
            raise MissingCapabilityError(
                "Model is not registered in the capability registry.",
                details={"provider": provider, "model": model_id},
            )
        missing = sorted(
            capability.value for capability in required if capability not in card.capabilities
        )
        if missing:
            raise MissingCapabilityError(
                "Model does not declare required capabilities.",
                details={"provider": provider, "model": model_id, "missing": missing},
            )
        return card


def create_default_registry() -> CapabilityRegistry:
    """Create a conservative built-in registry with explicit model cards."""

    registry = CapabilityRegistry()
    registry.register(
        ModelCard(
            provider=ProviderName.FAKE.value,
            model_id="fake-text",
            capabilities=frozenset({Capability.TEXT, Capability.MARKDOWN, Capability.CODE}),
            adapter_status=AdapterStatus.MOCK,
            source="Capybara AI test adapter contract",
            limitations=("No external provider call.", "Does not support real streaming."),
        )
    )
    registry.register(
        ModelCard(
            provider=ProviderName.OPENAI.value,
            model_id="gpt-5",
            capabilities=frozenset(
                {
                    Capability.TEXT,
                    Capability.IMAGE,
                    Capability.STREAMING,
                    Capability.STRUCTURED_OUTPUT,
                    Capability.MCP_COMPATIBLE,
                }
            ),
            adapter_status=AdapterStatus.REAL,
            source="OpenAI official Responses API documentation consulted 2026-05-11",
            limitations=(
                "Requires capybara-ai[openai] and a consumer-provided OPENAI_API_KEY.",
                "Only enabled when project configuration explicitly enables provider and model.",
            ),
        )
    )
    for provider, model_id in (
        (ProviderName.GEMINI.value, "gemini-default"),
        (ProviderName.ANTHROPIC.value, "anthropic-default"),
    ):
        registry.register(
            ModelCard(
                provider=provider,
                model_id=model_id,
                capabilities=frozenset({Capability.TEXT}),
                adapter_status=AdapterStatus.EXPERIMENTAL,
                source="Contract placeholder pending provider-specific verification",
                limitations=("No guaranteed runtime integration in V1 base install.",),
            )
        )
    for provider, model_id in (
        (ProviderName.XAI.value, "xai-default"),
        (ProviderName.DEEPSEEK.value, "deepseek-default"),
        (ProviderName.META.value, "meta-default"),
    ):
        registry.register(
            ModelCard(
                provider=provider,
                model_id=model_id,
                capabilities=frozenset({Capability.TEXT}),
                adapter_status=AdapterStatus.CONTRACT,
                source="Contract model card only",
                limitations=("Cannot execute as a real adapter.",),
            )
        )
    return registry
