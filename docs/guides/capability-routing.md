# Capability Routing

Capability routing is the main mental model in Capybara AI: describe what the
request needs, then route only to a model that is configured and capable.

Every request produces a set of required capabilities. For example:

- plain text requires `text`;
- streaming requires `streaming`;
- structured output requires `structured_output`;
- image context requires `image`;
- MCP tool participation requires `mcp_compatible`.

The router compares those requirements with explicit model cards and project
configuration. A model is eligible only when it is known, enabled, allowed by
policy, attached to a configured provider, and compatible with the request.

```python
result = agent.run(
    "Return a JSON object with a message.",
    runner,
    structured_schema={
        "type": "object",
        "properties": {"message": {"type": "string"}},
        "required": ["message"],
    },
)
```

Because this request asks for structured output, models without the
`structured_output` capability are skipped before any provider call.
