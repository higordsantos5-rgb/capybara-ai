"""Model card contract."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.core.types import AdapterStatus, Capability


@dataclass(frozen=True, slots=True)
class ModelCard:
    """Declared source of truth for one model's capabilities."""

    provider: str
    model_id: str
    capabilities: frozenset[Capability]
    adapter_status: AdapterStatus
    source: str
    limitations: tuple[str, ...] = ()
    metadata: dict[str, str] = field(default_factory=dict)

    def supports(self, capability: Capability) -> bool:
        return capability in self.capabilities
