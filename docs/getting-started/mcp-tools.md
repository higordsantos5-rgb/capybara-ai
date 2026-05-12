# MCP Tools

MCP tools are useful when agents need to read or act on external systems.
Capybara AI makes that boundary explicit.

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

A tool that is not allowlisted is denied. A tool that needs `write`, `edit`, or
`execute` must declare those permissions before it can run.

