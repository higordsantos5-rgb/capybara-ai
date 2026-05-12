# Errors

Errors are structured and secret-safe.

Important error types include:

- `ConfigurationError`;
- `MissingCredentialError`;
- `ProviderNotConfiguredError`;
- `ModelNotEnabledError`;
- `MissingCapabilityError`;
- `UnsupportedModalityError`;
- `NoEligibleModelError`;
- `ProviderExecutionError`;
- `AdapterStatusError`;
- `MCPConfigurationError`;
- `MCPPermissionError`;
- `MCPExecutionError`;
- `PipelineRequiredError`;
- `SecretExposureError`.

Validation failures should block before external calls.

