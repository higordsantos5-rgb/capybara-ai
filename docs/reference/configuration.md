# Configuration Reference

Configuration is the contract between your application and Capybara AI.

Primary objects:

- `ProjectConfig`
- `ProviderConfig`
- `ModelConfig`
- `RoutingPolicy`
- `SecretRef`

`ProjectConfig` controls provider availability, model enablement, credentials,
fallback policy, adapter status policy, and MCP availability.

`ProviderConfig` enables a provider for the project and points to credentials
owned by the consuming application.

`ModelConfig` enables a known model for routing. A model card can exist in the
capability registry without being enabled here.

`SecretRef` carries credentials while keeping representations and structured
errors redacted.

## Development Environment

For repository development, use:

```bash
python -m venv .venv
pip install -e ".[dev]"
```

Runtime users install the package with `pip install capybara-ai`.
