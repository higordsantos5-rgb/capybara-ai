# Capybara AI

Build predictable AI agents with explicit model capabilities, safe provider routing,
multimodal validation, and MCP tool permissions.

Capybara AI helps Python developers build AI agents that know what each model can
do before execution. Instead of scattering provider configuration, model
assumptions, API keys, fallback behavior, and tool permissions across your
application, Capybara AI centralizes those decisions in a small, explicit
framework.

## Why Capybara AI?

Most AI integrations start as a direct SDK call. That is useful for a prototype,
but production code quickly needs answers to harder questions:

- Which models are allowed in this project?
- Which provider can satisfy this request?
- Does this model actually support image, PDF, streaming, or structured output?
- Can this agent call an external tool, and with which permissions?
- When something is rejected, can the application inspect a structured reason?

Capybara AI gives you a capability-first layer between your application and
provider SDKs. You configure the providers and models your project permits, then
the framework validates requests locally before calling anything external.

## Installation

Install Capybara AI from PyPI:

```bash
pip install capybara-ai
```

Optional provider integrations are installed as extras:

```bash
pip install "capybara-ai[openai]"
pip install "capybara-ai[mcp]"
```

Python 3.11+ is required.

## Development Install

Use a local editable install when contributing or running the repository from
source:

```bash
git clone https://github.com/higordsantos5-rgb/capybara-ai.git
cd capybara-ai
python -m venv .venv
# Activate .venv for your shell.
pip install -e ".[dev]"
```

## Quickstart

The Fake/Test provider runs locally and needs no API key.

```python
from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(AgentConfig(name="assistant"))
result = agent.run("Explain capability-based routing in one sentence.", fake_runner())

print(result.output)
print(result.metadata.to_dict())
```

The result includes both the model output and structured metadata about provider
selection, model selection, required capabilities, and validation decisions.

## Core Concepts

- **Agents** define the task identity: name, instructions, preferred model
  policy, accepted context types, and allowed tools.
- **Providers** are adapter-backed integrations such as Fake/Test or OpenAI.
  A provider adapter can exist without being active in your project.
- **Capability Registry** describes what each known model can do. Capabilities
  are declared, not guessed from model names.
- **Routing** selects an eligible model from your configured providers and
  enabled models.
- **Multimodal Context** represents text, markdown, code, images, PDFs, audio,
  video, files, MCP resources, and explicitly derived context.
- **MCP Tools** are external tool calls governed by explicit server
  configuration, allowlists, scopes, permissions, and trace metadata.

## Example: Your First Agent

```python
from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(
    AgentConfig(
        name="support_assistant",
        instructions="Answer clearly and briefly.",
    )
)

result = agent.run("What is capability-first routing?", fake_runner())

print(result.output)
print(result.metadata.provider_selected)
print(result.metadata.model_selected)
```

## Providers

Adapters declare their maturity so applications can choose an appropriate policy.

| Provider | Status | Notes |
|---|---|---|
| Fake/Test | `mock` | Local adapter for tests, examples, and CI. |
| OpenAI | `real` | Optional extra; requires a consumer-provided API key. |
| Gemini | `experimental` | Declared adapter surface with limited maturity. |
| Anthropic | `experimental` | Declared adapter surface with limited maturity. |
| xAI | `contract` | Contract only; not executed as a real adapter. |
| DeepSeek | `contract` | Contract only; not executed as a real adapter. |
| Meta | `contract` | Contract only; not executed as a real adapter. |

API keys belong to the consuming project. Capybara AI does not create, embed, or
log provider secrets.

## Capability-Based Routing

Every request is mapped to required capabilities before routing. Text requires
`text`; streaming requires `streaming`; structured output requires
`structured_output`; image context requires `image`.

The router considers only models that are known, enabled by project config,
attached to an enabled provider, allowed by policy, compatible with the request,
and available at runtime. Fallback between providers is opt-in.

## Multimodal Validation

Capybara AI treats multimodal input as a capability boundary. If a request
contains image, PDF, audio, or video context, the selected model must declare
native support for that context type. Projects can also define explicit,
traceable pipelines that transform context before routing.

```python
from capybara_ai.context import ContextItem
from capybara_ai.core.types import ContextType

image = ContextItem(type=ContextType.IMAGE, data=b"...", source="upload")
```

That context contributes an `image` capability requirement to the request.

## MCP Tools And Permissions

MCP integrations are configured as explicit tools with scopes and permissions.
This keeps external reads, writes, edits, executions, and state mutations visible
in application code and execution metadata.

```python
from capybara_ai.mcp import MCPPermissions, MCPToolConfig

read_note = MCPToolConfig(
    name="read_note",
    server_name="local",
    scope="notes",
    permissions=MCPPermissions(read=True),
    allowlisted=True,
)
```

Tools that need stronger permissions declare them in configuration before they
can be called.

## Examples

The `examples/` directory includes:

- a simple Fake/Test agent;
- capability-based routing;
- multimodal validation;
- MCP allowed and denied tool calls;
- provider/model configuration errors;
- structured error metadata;
- OpenAI configuration, streaming, and structured output examples.

## Documentation

Start here:

- [Quickstart](https://capybara-ai-xi.vercel.app/docs/getting-started/quickstart)
- [First Agent](https://capybara-ai-xi.vercel.app/docs/getting-started/first-agent)
- [Provider Configuration](https://capybara-ai-xi.vercel.app/docs/getting-started/provider-configuration)
- [MCP Tools](https://capybara-ai-xi.vercel.app/docs/getting-started/mcp-tools)
- [Capability Routing](https://capybara-ai-xi.vercel.app/docs/guides/capability-routing)
- [Multimodal Context](https://capybara-ai-xi.vercel.app/docs/guides/multimodal-context)
- [Reference](https://capybara-ai-xi.vercel.app/docs/reference/configuration)

## Project Status

Capybara AI is in its first public V1 release.

The core architecture is stable enough for experimentation, learning, and early
integrations. Provider adapters may have different maturity levels (`real`,
`experimental`, `contract`, or `mock`) depending on the provider API and
available tests.

## License

Capybara AI is licensed under the MIT License. See `LICENSE`.
