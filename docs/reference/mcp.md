# MCP Reference

MCP support lets Capybara AI call external tools through explicit configuration.
Tools are described with server identity, scope, permissions, allowlist status,
and trace metadata.

Key objects:

- `MCPClientConfig`
- `MCPServerConfig`
- `MCPToolConfig`
- `MCPPermissions`
- `MCPToolRequest`
- `MCPToolResult`

Permissions:

- `read`
- `write`
- `edit`
- `execute`
- `mutates_external_state`

Tools start unavailable. Add them to configuration, allowlist them, and declare
the permissions required for each call.
