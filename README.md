# Capybara AI

Build predictable AI agents with explicit model capabilities, safe provider routing,
multimodal validation, and MCP tool permissions.

Capybara AI is a small Python framework for teams who want AI integrations to be
easy to reason about. Instead of scattering provider-specific SDK calls,
capability checks, fallback rules, credentials, and tool permissions across an
application, you describe what your project allows and let Capybara AI validate
before anything external runs.

## Why Capybara AI?

Direct SDK integrations are quick at first, but they often grow hidden assumptions:

- a model is used because its name was hardcoded, not because it was authorized;
- image, PDF, audio, or video input reaches a model that cannot handle it;
- fallback happens silently across providers;
- API keys leak into logs or error payloads;
- external tools run without a clear permission boundary.

Capybara AI gives those decisions names. Providers must be configured, models
must be enabled, capabilities must be declared, and MCP tools are denied unless
allowlisted.

## Install

Capybara AI is preparing its first public package release. The intended user
installation command is:

```bash
pip install capybara-ai
```

Optional provider integrations are installed as extras:

```bash
pip install "capybara-ai[openai]"
pip install "capybara-ai[mcp]"
```

From source:

```bash
git clone https://github.com/higordsantos5-rgb/capybara-ai.git
cd capybara-ai
python -m venv .venv
# Activate .venv for your shell.
pip install -e ".[dev]"
```

Python 3.11+ is required.

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

Output is structured: you get the response plus metadata about the selected
provider, model, required capabilities, and validation path.

## Design Principles

Capybara AI follows four principles:

1. Explicit over implicit.
2. Validate before execution.
3. Capabilities are declared, never guessed.
4. External tools are denied by default.

These principles keep the framework predictable when you add real providers,
multimodal context, streaming, structured output, or MCP tools.

## Core Concepts

`ProjectConfig` is the center of the application contract. It says which
providers are enabled, which models are allowed, where credentials come from,
which adapter statuses are acceptable, and whether fallback is allowed.

`CapabilityRegistry` is the source of truth for what models can do. A known
model is not automatically enabled. A supported provider is not automatically
active.

`AgentRunner` validates context, routes to an eligible model, checks MCP policy,
and calls the selected adapter only after local checks pass.

## Providers And Adapter Status

Adapters are honest about maturity:

| Provider | Status | Notes |
|---|---|---|
| Fake/Test | `mock` | Local adapter for tests, examples, and CI. |
| OpenAI | `real` | Optional extra; requires a consumer-provided API key. |
| Gemini | `experimental` | Declared placeholder in the base package. |
| Anthropic | `experimental` | Declared placeholder in the base package. |
| xAI | `contract` | Contract only; does not execute as real. |
| DeepSeek | `contract` | Contract only; does not execute as real. |
| Meta | `contract` | Contract only; does not execute as real. |

API keys belong to the consuming project. Capybara AI does not create, embed, or
log provider secrets.

## Capability-Based Routing

Every request produces required capabilities. Text requires `text`; streaming
requires `streaming`; structured output requires `structured_output`; image
context requires `image`.

The router selects only models that are:

- known in the registry;
- enabled by project config;
- attached to an enabled and configured provider;
- allowed by policy;
- compatible with required capabilities;
- available at runtime.

Fallback is opt-in.

## Multimodal Validation

Multimodal input is treated as a real capability boundary. If a model does not
declare native support for an input type, the request is blocked before provider
execution unless the project configures an explicit, traceable pipeline.

This makes image/PDF/audio/video handling visible instead of accidental.

## MCP Tools And Permissions

MCP tools use default deny. A tool call needs:

- MCP enabled;
- configured server/connector;
- allowlisted tool name;
- declared scope;
- declared permissions such as `read`, `write`, `edit`, or `execute`;
- trace metadata.

This allows useful integrations without turning tools into ambient authority.

## Examples

See `examples/` for:

- a simple Fake/Test agent;
- capability-based routing;
- multimodal blocking;
- MCP allowed and denied tools;
- provider/model configuration errors;
- structured error metadata;
- OpenAI configuration, streaming, and structured output examples.

## Documentation

Start here:

- [Quickstart](docs/getting-started/quickstart.md)
- [First Agent](docs/getting-started/first-agent.md)
- [Provider Configuration](docs/getting-started/provider-configuration.md)
- [MCP Tools](docs/getting-started/mcp-tools.md)
- [Capability Routing](docs/guides/capability-routing.md)
- [Multimodal Context](docs/guides/multimodal-context.md)
- [Reference](docs/reference/configuration.md)

Internal compliance and release checks live under `docs/internal/` and
`docs/audit.md`.

## Project Status

Capybara AI V1 is implemented and locally validated. The package is preparing
its first public package release. The intended installation command is
`pip install capybara-ai`.

Real PyPI publication will use an explicit release checklist and should prefer
Trusted Publishing via GitHub Actions.

## License

Capybara AI is licensed under the MIT License. See `LICENSE`.
