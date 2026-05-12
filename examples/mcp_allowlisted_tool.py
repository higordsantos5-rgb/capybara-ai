from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.mcp import (
    MCPClient,
    MCPClientConfig,
    MCPPermissions,
    MCPServerConfig,
    MCPToolConfig,
    MCPToolRequest,
)

config = MCPClientConfig(
    enabled=True,
    servers={"local": MCPServerConfig(name="local", transport="local", enabled=True)},
    tools={
        "read_note": MCPToolConfig(
            name="read_note",
            server_name="local",
            scope="notes",
            permissions=MCPPermissions(read=True),
            allowlisted=True,
        )
    },
)

client = MCPClient(config)
client.register_local_executor(
    "read_note", lambda args: {"note_id": args["id"], "title": "Example"}
)

metadata = ExecutionMetadata(agent_name="example")
result = client.execute(
    MCPToolRequest(
        name="read_note",
        arguments={"id": "note-1"},
        required_permissions=MCPPermissions(read=True),
    ),
    metadata,
)

print(result)
print(metadata.to_dict())
