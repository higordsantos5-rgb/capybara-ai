from capybara_ai.core.errors import CapybaraAIError
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.mcp import (
    MCPClient,
    MCPClientConfig,
    MCPPermissions,
    MCPServerConfig,
    MCPToolConfig,
    MCPToolRequest,
)

client = MCPClient(
    MCPClientConfig(
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
)
client.register_local_executor("read_note", lambda args: {"id": args["id"], "text": "hello"})

metadata = ExecutionMetadata(agent_name="mcp_example")
allowed = client.execute(
    MCPToolRequest(
        name="read_note",
        arguments={"id": "note-1"},
        required_permissions=MCPPermissions(read=True),
    ),
    metadata,
)

print("allowed output:", allowed.output)
print("trace:", metadata.to_dict()["mcp_calls"])

try:
    client.execute(MCPToolRequest(name="delete_note"), metadata)
except CapybaraAIError as error:
    print("denied error:", error.to_dict())
