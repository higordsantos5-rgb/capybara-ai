"""Capability-first router."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.capabilities.registry import CapabilityRegistry
from capybara_ai.config.project import ProjectConfig
from capybara_ai.core.errors import NoEligibleModelError
from capybara_ai.core.execution import ExecutionRequest
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import AdapterStatus, Capability
from capybara_ai.providers.base import ProviderAdapter
from capybara_ai.providers.registry import create_default_adapters
from capybara_ai.routing.policies import RoutingSelection


@dataclass(slots=True)
class Router:
    """Select models only after explicit eligibility checks."""

    registry: CapabilityRegistry
    adapters: dict[str, ProviderAdapter] = field(default_factory=create_default_adapters)

    def route(
        self,
        request: ExecutionRequest,
        config: ProjectConfig,
        metadata: ExecutionMetadata,
    ) -> RoutingSelection:
        required = request.all_required_capabilities()
        metadata.required_capabilities = sorted(capability.value for capability in required)
        eligible: list[RoutingSelection] = []
        for card in self.registry.all_cards():
            accepted, reason = self._is_eligible(card, required, request, config)
            metadata.add_decision(card.provider, card.model_id, accepted, reason)
            if accepted:
                adapter = self.adapters[card.provider]
                eligible.append(RoutingSelection(card=card, adapter=adapter))
        if not eligible:
            raise NoEligibleModelError(
                "No enabled model satisfied provider, policy, runtime, and capability checks.",
                details={"required_capabilities": metadata.required_capabilities},
            )
        selection = eligible[0]
        metadata.provider_selected = selection.card.provider
        metadata.model_selected = selection.card.model_id
        metadata.satisfied_capabilities = sorted(
            capability.value for capability in selection.card.capabilities if capability in required
        )
        return selection

    def _is_eligible(
        self,
        card: ModelCard,
        required: set[Capability],
        request: ExecutionRequest,
        config: ProjectConfig,
    ) -> tuple[bool, str]:
        adapter = self.adapters.get(card.provider)
        if adapter is None:
            return False, "provider_not_supported_by_framework"
        provider_config = config.provider_config(card.provider)
        if provider_config is None or not provider_config.enabled:
            return False, "provider_not_enabled_by_project"
        if not provider_config.configured(requires_credentials=adapter.requires_credentials):
            return False, "provider_not_configured_or_unavailable"
        if not config.routing_policy.allows_status(adapter.status):
            return False, "adapter_status_not_allowed_by_policy"
        if adapter.status is AdapterStatus.CONTRACT:
            return False, "contract_adapter_cannot_execute"
        if not adapter.is_available():
            return False, "adapter_runtime_unavailable"
        model_config = config.model_config(card.provider, card.model_id)
        if model_config is None or not model_config.enabled:
            return False, "model_not_enabled_by_project"
        if not model_config.available:
            return False, "model_unavailable_at_runtime"
        if (
            request.preferred_model
            and request.preferred_model != card.model_id
            and not config.routing_policy.allow_fallback
        ):
            return False, "preferred_model_mismatch_and_fallback_disabled"
        missing = required.difference(card.capabilities)
        if missing:
            return False, "missing_capabilities:" + ",".join(sorted(item.value for item in missing))
        if (Capability.STREAMING in required or Capability.STRUCTURED_OUTPUT in required) and (
            adapter.status is not AdapterStatus.REAL
        ):
            return False, "streaming_or_structured_output_requires_real_adapter"
        return True, "eligible"
