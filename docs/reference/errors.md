# Errors Reference

Capybara AI uses structured errors for configuration, routing, provider, context,
and MCP failures.

Common error families:

- `ConfigurationError`
- `MissingCredentialError`
- `ProviderNotConfiguredError`
- `ModelNotEnabledError`
- `MissingCapabilityError`
- `UnsupportedModalityError`
- `NoEligibleModelError`
- `ProviderExecutionError`
- `AdapterStatusError`
- `MCPConfigurationError`
- `MCPPermissionError`
- `MCPExecutionError`
- `PipelineRequiredError`

Structured errors expose stable codes and safe details. Sensitive values such as
API keys, tokens, and secret environment values are redacted.
