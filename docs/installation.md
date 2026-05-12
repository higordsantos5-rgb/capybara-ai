# Installation

The intended public installation command is:

```bash
pip install capybara-ai
```

Capybara AI is preparing its first public package release. Until the package is
available on PyPI, install from source:

```bash
git clone https://github.com/higordsantos5-rgb/capybara-ai.git
cd capybara-ai
python -m venv .venv
# Activate .venv for your shell.
pip install -e ".[dev]"
```

Optional extras:

```bash
pip install "capybara-ai[openai]"
pip install "capybara-ai[mcp]"
```

Python 3.11+ is required. Poetry and uv are not required.

Use `.env.example` as a template. Do not commit a real `.env`.

