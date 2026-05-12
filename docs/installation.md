# Installation

Install Capybara AI from PyPI:

```bash
pip install capybara-ai
```

Optional provider integrations are available as extras:

```bash
pip install "capybara-ai[openai]"
pip install "capybara-ai[mcp]"
```

Python 3.11+ is required.

## Development Install

Use a local editable install when contributing or running the repository from
source:

```bash
git clone https://github.com/higordsantos5-rgb/capybara-ai.git
cd capybara-ai
python -m venv .venv
# Activate .venv for your shell.
pip install -e ".[dev]"
```

For development, copy `.env.example` to your own `.env` file and fill in
project-owned credentials. Keep real `.env` files out of version control.
