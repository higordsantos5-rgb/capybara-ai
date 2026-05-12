# Structured Errors

Capybara AI returns structured errors instead of turning validation failures into
successful text.

```python
result = agent.run("Describe this image", runner, context=[image_item])

if not result.success:
    print(result.error.to_dict())
    print(result.metadata.to_dict())
```

Metadata includes routing decisions, missing capabilities, context items,
validation blocks, and MCP tool traces when relevant. Secrets are redacted.

