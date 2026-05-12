# MCP

MCP is default deny.

A tool requires:

- MCP enabled;
- configured server/connector;
- allowlisted tool;
- declared scope;
- declared permissions;
- traceable execution.

Permissions:

- `read`;
- `write`;
- `edit`;
- `execute`;
- `mutates_external_state`.

Operations that mutate state must say so. Capybara AI records MCP calls in
execution metadata and redacts secrets.

GitHub operations must use `github-mcp`. Do not use
`mcp__codex_apps__github`.

