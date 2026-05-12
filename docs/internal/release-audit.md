# Release Audit

Before a public package release:

- run `pytest`;
- run `ruff check .`;
- run `ruff format --check .`;
- run `mypy src`;
- run `python -m build`;
- run `python -m twine check dist/*`;
- install the wheel in a clean environment;
- verify no `.env`, `.venv/`, tokens, or build caches are versioned;
- verify license metadata;
- verify GitHub is current.

Use TestPyPI before PyPI. Prefer Trusted Publishing via GitHub Actions for real
PyPI.

