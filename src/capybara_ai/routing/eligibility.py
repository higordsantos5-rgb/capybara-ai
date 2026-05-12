"""Eligibility checks."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.capabilities.model_card import ModelCard


@dataclass(frozen=True, slots=True)
class EligibilityResult:
    """One router eligibility decision."""

    card: ModelCard
    accepted: bool
    reason: str
