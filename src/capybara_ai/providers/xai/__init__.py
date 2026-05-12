"""xAI adapter namespace."""

from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers._contract import LimitedProviderAdapter

XAIProviderAdapter = LimitedProviderAdapter
default_adapter = LimitedProviderAdapter(
    provider=ProviderName.XAI.value,
    status=AdapterStatus.CONTRACT,
    limitations=("Contract only; cannot execute as real provider.",),
)

__all__ = ["XAIProviderAdapter", "default_adapter"]
