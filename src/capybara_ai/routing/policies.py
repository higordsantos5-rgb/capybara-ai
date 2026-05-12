"""Routing policy result contracts."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.providers.base import ProviderAdapter


@dataclass(frozen=True, slots=True)
class RoutingSelection:
    """Selected model and provider adapter."""

    card: ModelCard
    adapter: ProviderAdapter
