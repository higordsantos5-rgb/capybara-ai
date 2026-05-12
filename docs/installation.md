# Installation

Required baseline:

```bash
python -m venv .venv
# Activate .venv for your shell.
pip install -e ".[dev]"
```

Python 3.11+ is required. `.venv/` must stay in the repository root and must not
be versioned.

Optional extras:

```bash
pip install -e ".[openai]"
pip install -e ".[mcp]"
```

Poetry is not required. uv is optional for consuming projects but not the base
workflow.

Use `.env.example` as a template. Do not commit a real `.env`.

