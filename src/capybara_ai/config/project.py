"""Central project configuration."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.config.models import ModelConfig
from capybara_ai.config.policies import RoutingPolicy
from capybara_ai.config.providers import ProviderConfig
from capybara_ai.core.errors import MissingCredentialError, ProviderNotConfiguredError


@dataclass(slots=True)
class ProjectConfig:
    """Explicit configuration controlled by the consuming project."""

    providers: dict[str, ProviderConfig] = field(default_factory=dict)
    models: dict[tuple[str, str], ModelConfig] = field(default_factory=dict)
    routing_policy: RoutingPolicy = field(default_factory=RoutingPolicy)
    mcp_enabled: bool = False

    def provider_config(self, provider: str) -> ProviderConfig | None:
        return self.providers.get(provider)

    def model_config(self, provider: str, model_id: str) -> ModelConfig | None:
        return self.models.get((provider, model_id))

    def require_provider_configured(
        self, provider: str, *, requires_credentials: bool
    ) -> ProviderConfig:
        config = self.provider_config(provider)
        if config is None or not config.enabled:
            raise ProviderNotConfiguredError(
                "Provider is supported by the framework but not enabled by project config.",
                details={"provider": provider},
            )
        if requires_credentials and config.credential is None:
            raise MissingCredentialError(
                "Provider credential is missing from project config.",
                details={"provider": provider},
            )
        if not config.available:
            raise ProviderNotConfiguredError(
                "Provider is configured but marked unavailable at runtime.",
                details={"provider": provider},
            )
        return config

    def enabled_models(self) -> list[ModelConfig]:
        return [config for config in self.models.values() if config.enabled and config.available]
