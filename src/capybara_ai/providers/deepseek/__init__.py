"""DeepSeek adapter namespace."""

from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers._contract import LimitedProviderAdapter

DeepSeekProviderAdapter = LimitedProviderAdapter
default_adapter = LimitedProviderAdapter(
    provider=ProviderName.DEEPSEEK.value,
    status=AdapterStatus.CONTRACT,
    limitations=("Contract only; cannot execute as real provider.",),
)

__all__ = ["DeepSeekProviderAdapter", "default_adapter"]
