# Agents Reference

`AgentConfig` fields include:

- `name`
- `instructions`
- `preferred_model`
- `allowed_providers`
- `allowed_models`
- `accepted_context_types`
- `allowed_tools`
- `allowed_mcp_tools`
- `max_steps`
- `error_policy`

`AgentRunner` validates context, executes authorized MCP requests, routes to an
eligible model, and calls the selected adapter.

