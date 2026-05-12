"""Provider configuration."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.config.secrets import SecretRef


@dataclass(frozen=True, slots=True)
class ProviderConfig:
    """Project-level provider configuration. Supported is not active."""

    provider: str
    enabled: bool = False
    credential: SecretRef | None = None
    available: bool = True

    def configured(self, *, requires_credentials: bool) -> bool:
        if not self.enabled or not self.available:
            return False
        return not (requires_credentials and self.credential is None)
