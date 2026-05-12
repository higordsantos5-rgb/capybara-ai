# Testing

Run:

```bash
pytest
ruff check .
mypy src/capybara_ai
```

The default test suite must not require API keys or external services.

Required negative tests include provider not configured, model not enabled,
missing capability, incompatible multimodal context, no automatic OCR/PDF
parsing/transcription, no unauthorized fallback, MCP default deny, tool not
allowlisted, secret redaction, contract adapter non-execution, no streaming
simulation, and no structured output without capability.

