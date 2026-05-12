# Structured Errors

Capybara AI returns structured failures so applications can decide what to show
users, what to retry, and what to log safely.

```python
result = agent.run("Use a provider that is not configured.", runner)

if not result.success and result.error is not None:
    print(result.error.code)
    print(result.error.message)
    print(result.error.details)
```

Errors include stable codes and safe details. Metadata also records routing
decisions, discarded models, required capabilities, and validation steps when
they apply.

Sensitive values such as API keys, tokens, and `.env` contents are redacted from
structured errors and metadata.
