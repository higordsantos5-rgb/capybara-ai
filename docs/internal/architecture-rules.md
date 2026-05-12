# Architecture Rules

This page is for maintainers.

Capybara AI follows Ports and Adapters. The core must not import provider SDKs,
MCP SDKs, web frameworks, OCR/PDF parsing libraries, or transcription libraries.

Public docs may explain behavior in user-friendly language, but the normative
rules remain in `system_spec.md`, `technical_spec.md`, `implementation_plan.md`,
`change_log.md`, and `AGENTS.md`.

