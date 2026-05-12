# Troubleshooting

## No eligible model

Check provider enabled, model enabled, credential configured, adapter status
allowed, runtime availability, and required capabilities.

## Missing credential

Provide a consumer-owned credential through project configuration. Capybara AI
does not create or load secrets automatically.

## Multimodal context blocked

The selected model does not declare native capability and no explicit pipeline
was configured.

## MCP tool blocked

Check MCP enabled, server enabled, tool allowlisted, and permissions declared.

## Git/GitHub

Local Git requires `git` in PATH. GitHub remote operations, when authorized, must
use `github-mcp`.

