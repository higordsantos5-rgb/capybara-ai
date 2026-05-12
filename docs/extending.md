# Extending

## Add a provider

1. Create an adapter in `capybara_ai.providers`.
2. Keep SDK imports inside the adapter.
3. Declare adapter status and limitations.
4. Add model cards to the registry.
5. Add config/docs/tests.
6. Do not activate by default.

## Add a context type

1. Add a context type.
2. Map it to an explicit capability.
3. Add tests for supported and unsupported models.
4. Do not add implicit conversion.

## Add an MCP integration

1. Configure server/connector.
2. Declare tools and scopes.
3. Declare permissions.
4. Add allowlist.
5. Record traces.
6. Test denied and allowed paths.

