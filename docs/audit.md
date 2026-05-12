# Final Adherence Audit

Audit date: 2026-05-12.

## Confirmed By Static Review

- Official names are used: Capybara AI, `capybara-ai`, `capybara_ai`.
- `pyproject.toml` exists and requires Python 3.11+.
- Runtime dependencies are empty.
- Provider/MCP SDKs are optional extras and imported only inside adapters/connectors.
- `.gitignore` ignores `.venv/`, `.env`, caches, build output, and package metadata.
- `.env.example` exists without real secret values.
- Core modules do not import OpenAI SDK or MCP SDK.
- Capability registry exists and treats missing capabilities as unsupported.
- Multimodal context exists and does not implement automatic OCR, PDF parsing, transcription, or conversion.
- Providers declare status: `mock`, `real`, `experimental`, or `contract`.
- Router only selects eligible models after configuration and capability checks.
- MCP has default deny, allowlist, permissions, and trace metadata.
- Streaming and structured output are capabilities and are not simulated by the Fake/Test adapter.
- README, docs, examples, and tests exist.
- License remains pending and is not invented.

## Local Validation Results

- Python 3.12.10 is available.
- Git 2.54.0 is available.
- `.venv` was created.
- Editable install succeeded with `python -m pip install -e ".[dev]"`.
- `pytest` passed: 12 tests.
- `ruff check .` passed.
- `ruff format --check .` passed.
- `mypy src` passed with no issues in 52 source files.
- Git repository was initialized locally.
- GitHub remote operations were not requested or authorized in this run. If used later, they must use `github-mcp`.

## Remaining Release Gate

Do not declare a mature public release until:

- license is defined if a public release requires it.
- remote GitHub publication is explicitly authorized, if desired.
