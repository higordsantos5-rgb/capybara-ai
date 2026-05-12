"""Default provider adapter registry."""

from __future__ import annotations

from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers._contract import LimitedProviderAdapter
from capybara_ai.providers.base import ProviderAdapter
from capybara_ai.providers.fake import FakeProviderAdapter
from capybara_ai.providers.openai import OpenAIProviderAdapter


def create_default_adapters() -> dict[str, ProviderAdapter]:
    """Create adapters without activating any provider by default."""

    return {
        ProviderName.FAKE.value: FakeProviderAdapter(),
        ProviderName.OPENAI.value: OpenAIProviderAdapter(),
        ProviderName.GEMINI.value: LimitedProviderAdapter(
            provider=ProviderName.GEMINI.value,
            status=AdapterStatus.EXPERIMENTAL,
            limitations=("Experimental placeholder; no SDK runtime in base install.",),
        ),
        ProviderName.ANTHROPIC.value: LimitedProviderAdapter(
            provider=ProviderName.ANTHROPIC.value,
            status=AdapterStatus.EXPERIMENTAL,
            limitations=("Experimental placeholder; no SDK runtime in base install.",),
        ),
        ProviderName.XAI.value: LimitedProviderAdapter(
            provider=ProviderName.XAI.value,
            status=AdapterStatus.CONTRACT,
            limitations=("Contract only; cannot execute as real provider.",),
        ),
        ProviderName.DEEPSEEK.value: LimitedProviderAdapter(
            provider=ProviderName.DEEPSEEK.value,
            status=AdapterStatus.CONTRACT,
            limitations=("Contract only; cannot execute as real provider.",),
        ),
        ProviderName.META.value: LimitedProviderAdapter(
            provider=ProviderName.META.value,
            status=AdapterStatus.CONTRACT,
            limitations=("Contract only; cannot execute as real provider.",),
        ),
    }
