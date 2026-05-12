"""Structured errors used across Capybara AI."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from capybara_ai.core.types import SENSITIVE_KEYS


def redact_value(value: Any) -> Any:
    """Return a secret-safe representation of nested values."""

    if isinstance(value, Mapping):
        return {
            str(key): "[REDACTED]" if str(key).lower() in SENSITIVE_KEYS else redact_value(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [redact_value(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_value(item) for item in value)
    return value


class CapybaraAIError(Exception):
    """Base class for structured, secret-safe Capybara AI errors."""

    code = "capybara_ai_error"

    def __init__(self, message: str, *, details: Mapping[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = redact_value(dict(details or {}))

    def to_dict(self) -> dict[str, Any]:
        return {"code": self.code, "message": self.message, "details": self.details}


class ConfigurationError(CapybaraAIError):
    code = "configuration_error"


class MissingCredentialError(ConfigurationError):
    code = "missing_credential"


class ProviderNotConfiguredError(ConfigurationError):
    code = "provider_not_configured"


class ModelNotEnabledError(ConfigurationError):
    code = "model_not_enabled"


class MissingCapabilityError(CapybaraAIError):
    code = "missing_capability"


class UnsupportedModalityError(CapybaraAIError):
    code = "unsupported_modality"


class NoEligibleModelError(CapybaraAIError):
    code = "no_eligible_model"


class RoutingPolicyError(CapybaraAIError):
    code = "routing_policy_error"


class ProviderExecutionError(CapybaraAIError):
    code = "provider_execution_error"


class ProviderUnavailableError(ProviderExecutionError):
    code = "provider_unavailable"


class AdapterStatusError(CapybaraAIError):
    code = "adapter_status_error"


class InvalidContextError(CapybaraAIError):
    code = "invalid_context"


class MCPConfigurationError(CapybaraAIError):
    code = "mcp_configuration_error"


class MCPPermissionError(CapybaraAIError):
    code = "mcp_permission_error"


class MCPExecutionError(CapybaraAIError):
    code = "mcp_execution_error"


class PipelineRequiredError(CapybaraAIError):
    code = "pipeline_required"


class SecretExposureError(CapybaraAIError):
    code = "secret_exposure"


class DependencyPolicyError(CapybaraAIError):
    code = "dependency_policy_error"
