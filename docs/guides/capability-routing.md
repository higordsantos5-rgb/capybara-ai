# Capability Routing

Capability routing is the main mental model in Capybara AI.

Every request has required capabilities. The router compares those requirements
against explicit model cards and project configuration.

Examples:

- plain text requires `text`;
- streaming requires `streaming`;
- structured output requires `structured_output`;
- image context requires `image`;
- MCP participation requires `mcp_compatible`.

If a model does not declare a required capability, it is not eligible. Capybara AI
does not infer support from provider name or model name.

