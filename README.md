# Capybara AI

Capybara AI is a capability-first Python microframework for configurable AI agents,
provider routing, multimodal context validation, and explicit MCP tool execution.

It is designed for Python developers who need AI integrations without scattering
provider rules, model assumptions, fallback behavior, API keys, and tool
permissions across application code.

## Status

This repository contains the V1 implementation track. V1 is complete in identity:
core contracts, capability registry, routing, agents, multimodal context, provider
adapters, MCP policy, tests, examples, README, and docs are part of the same V1.

Some adapters are intentionally not real. Adapter status is explicit.

## Installation

```bash
python -m venv .venv
# Activate .venv for your shell.
pip install -e ".[dev]"
```

Optional provider/connectors:

```bash
pip install -e ".[openai]"
pip install -e ".[mcp]"
```

Python 3.11+ is required. Poetry and uv are not required.

## Quick Example

```python
from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(AgentConfig(name="assistant"))
result = agent.run("Hello.", fake_runner())

print(result.output)
print(result.metadata.to_dict())
```

The Fake/Test provider runs without external APIs or API keys.

## Architecture

Capybara AI follows Ports and Adapters:

- application-facing API;
- agents and runner;
- routing and validation;
- capability registry;
- context and MCP policy;
- provider adapter ports;
- external providers and MCP servers.

The core does not import provider SDKs, MCP SDKs, web frameworks, OCR libraries,
PDF parsers, or transcription tools.

## Providers

Provider support has three separate states:

- supported by framework architecture;
- enabled/configured by the consuming project;
- available at runtime.

Known V1 adapter statuses:

| Provider | Status | Notes |
|---|---|---|
| Fake/Test | `mock` | Functional local adapter for tests and examples. |
| OpenAI | `real` | Optional `capybara-ai[openai]`; requires consumer API key. |
| Gemini | `experimental` | Declared placeholder, no runtime SDK in base install. |
| Anthropic | `experimental` | Declared placeholder, no runtime SDK in base install. |
| xAI | `contract` | Contract only; cannot execute as real. |
| DeepSeek | `contract` | Contract only; cannot execute as real. |
| Meta | `contract` | Contract only; cannot execute as real. |

No provider is active by default.

## Capability Registry

The registry is the internal source of truth for model capabilities. A missing
capability means unsupported. Capybara AI does not infer capability from a model
name or provider name.

Capabilities include text, image, PDF, audio, video, MCP compatibility,
streaming, and structured output.

## Routing

The router only selects models that are:

- known in the registry;
- enabled by project configuration;
- attached to an enabled/configured provider;
- allowed by adapter status policy;
- compatible with required capabilities;
- available at runtime.

Fallback only happens when explicitly allowed.

## Multimodal Context

Capybara AI does not fake multimodal support. It does not perform automatic OCR,
PDF parsing, transcription, video analysis, or hidden fallback to text.

Unsupported context is blocked before provider execution unless the consuming
project supplies an explicit, traceable pipeline.

## MCP

MCP is default deny. A tool can execute only when MCP is configured, the server
is enabled, the tool is allowlisted, scope is declared, permissions are declared,
and the call is traceable.

GitHub operations, when authorized, must use `github-mcp`. The
`mcp__codex_apps__github` connector is prohibited.

## API Keys

API keys belong to the consuming project. Capybara AI does not create, embed,
load, log, or expose provider secrets. Missing credentials produce structured
errors.

## Examples

See `examples/` for:

- a simple Fake/Test agent;
- capability routing;
- multimodal blocking;
- MCP allowlist;
- provider configuration errors;
- OpenAI configuration;
- streaming and structured output with a compatible real provider.

## License

License is pending. This project does not currently declare a public release
license.

