"""Capability validation helpers."""

from __future__ import annotations

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.core.errors import MissingCapabilityError
from capybara_ai.core.types import Capability


def require_capabilities(card: ModelCard, required: set[Capability]) -> None:
    """Validate required capabilities against an explicit model card."""

    missing = sorted(
        capability.value for capability in required if capability not in card.capabilities
    )
    if missing:
        raise MissingCapabilityError(
            "Required capability is absent and therefore unsupported.",
            details={"provider": card.provider, "model": card.model_id, "missing": missing},
        )
