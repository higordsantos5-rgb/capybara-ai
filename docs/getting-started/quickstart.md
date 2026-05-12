# Quickstart

This quickstart moves from a local agent to the shape of a real provider and MCP
tool setup. The first example runs entirely offline with the Fake/Test provider.

## 1. Install

```bash
pip install capybara-ai
```

For local development from source:

```bash
git clone https://github.com/higordsantos5-rgb/capybara-ai.git
cd capybara-ai
python -m venv .venv
pip install -e ".[dev]"
```

## 2. Create A Local Agent

```python
from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(AgentConfig(name="assistant"))
result = agent.run("Summarize Capybara AI in one sentence.", fake_runner())

print(result.output)
print(result.metadata.to_dict())
```

The Fake/Test provider never calls an external service, so it is useful for
learning, tests, and CI.

## 3. Configure A Real Provider

```python
import os

from capybara_ai.agents import Agent, AgentConfig, AgentRunner
from capybara_ai.capabilities import create_default_registry
from capybara_ai.config import ModelConfig, ProjectConfig, ProviderConfig, SecretRef
from capybara_ai.routing import Router

config = ProjectConfig(
    providers={
        "openai": ProviderConfig(
            provider="openai",
            enabled=True,
            credential=SecretRef(os.environ["OPENAI_API_KEY"]),
        )
    },
    models={
        ("openai", "gpt-5"): ModelConfig(
            provider="openai",
            model_id="gpt-5",
            enabled=True,
        )
    },
)

runner = AgentRunner(project_config=config, router=Router(create_default_registry()))
agent = Agent(AgentConfig(name="assistant"))
```

Provider support, project configuration, and runtime credentials are separate.
Your project decides which providers and models are eligible.

## 4. Let Capabilities Drive Routing

```python
result = agent.run(
    "Return a JSON object with a message.",
    runner,
    structured_schema={
        "type": "object",
        "properties": {"message": {"type": "string"}},
        "required": ["message"],
        "additionalProperties": False,
    },
)
```

Structured output adds the `structured_output` capability to the request. The
router selects only a configured model that declares the capability.

## 5. Add An MCP Tool With An Allowlist

```python
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
metadata = ExecutionMetadata(agent_name="assistant")
result = client.execute(
    MCPToolRequest(
        name="read_note",
        arguments={"id": "note-1"},
        required_permissions=MCPPermissions(read=True),
    ),
    metadata,
)
```

Execution metadata records the tool name, server, and permissions used.
