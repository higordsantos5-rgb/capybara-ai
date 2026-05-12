"""Gemini adapter namespace."""

from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers._contract import LimitedProviderAdapter

GeminiProviderAdapter = LimitedProviderAdapter
default_adapter = LimitedProviderAdapter(
    provider=ProviderName.GEMINI.value,
    status=AdapterStatus.EXPERIMENTAL,
    limitations=("Experimental placeholder; no SDK runtime in base install.",),
)

__all__ = ["GeminiProviderAdapter", "default_adapter"]
