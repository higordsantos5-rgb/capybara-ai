"""Meta adapter namespace."""

from capybara_ai.core.types import AdapterStatus, ProviderName
from capybara_ai.providers._contract import LimitedProviderAdapter

MetaProviderAdapter = LimitedProviderAdapter
default_adapter = LimitedProviderAdapter(
    provider=ProviderName.META.value,
    status=AdapterStatus.CONTRACT,
    limitations=("Contract only; cannot execute as real provider.",),
)

__all__ = ["MetaProviderAdapter", "default_adapter"]
