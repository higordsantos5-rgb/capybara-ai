"""Provider adapter registry."""

from capybara_ai.providers.base import ProviderAdapter, ProviderResponse
from capybara_ai.providers.fake import FakeProviderAdapter
from capybara_ai.providers.registry import create_default_adapters

__all__ = ["FakeProviderAdapter", "ProviderAdapter", "ProviderResponse", "create_default_adapters"]
