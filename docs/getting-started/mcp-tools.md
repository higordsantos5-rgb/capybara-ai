# MCP Tools

MCP tools let agents interact with external systems while keeping the operational
boundary visible in code. A tool declares where it runs, what scope it belongs
to, and which permissions it needs.

```python
from capybara_ai.mcp import MCPPermissions, MCPToolConfig

tool = MCPToolConfig(
    name="read_note",
    server_name="local",
    scope="notes",
    permissions=MCPPermissions(read=True),
    allowlisted=True,
)
```

Use `read` for lookup-style tools, `write` for creation, `edit` for updates,
`execute` for external actions, and `mutates_external_state` when a call changes
state outside the process. Execution metadata records the tool call so your app
can explain what happened.
