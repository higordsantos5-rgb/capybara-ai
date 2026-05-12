"""Routing and execution policies."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.core.types import AdapterStatus


@dataclass(frozen=True, slots=True)
class RoutingPolicy:
    """Explicit routing policy for a consuming project."""

    name: str = "first_compatible"
    allow_fallback: bool = False
    allowed_adapter_statuses: frozenset[AdapterStatus] = field(
        default_factory=lambda: frozenset({AdapterStatus.REAL, AdapterStatus.MOCK})
    )

    def allows_status(self, status: AdapterStatus) -> bool:
        return status in self.allowed_adapter_statuses
