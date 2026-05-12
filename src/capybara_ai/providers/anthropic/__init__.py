"""Anthropic adapter namespace."""

from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers._contract import LimitedProviderAdapter

AnthropicProviderAdapter = LimitedProviderAdapter
default_adapter = LimitedProviderAdapter(
    provider=ProviderName.ANTHROPIC.value,
    status=AdapterStatus.EXPERIMENTAL,
    limitations=("Experimental placeholder; no SDK runtime in base install.",),
)

__all__ = ["AnthropicProviderAdapter", "default_adapter"]
