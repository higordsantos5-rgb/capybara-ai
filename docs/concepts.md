# Concepts

## Capability-first

Every execution is validated against declared model capabilities before provider
execution. A missing capability means unsupported.

## Provider states

A provider can be:

- supported by framework architecture;
- enabled by project configuration;
- configured with credentials;
- allowed by policy;
- available at runtime.

These states are intentionally separate.

## Model states

A model can be:

- known in the registry;
- enabled by the consuming project;
- compatible with requested capabilities;
- allowed by policy;
- available at runtime.

Known never means enabled.

## Execution metadata

Every result includes metadata for agent, provider, model, routing decisions,
required capabilities, context, validations, blocks, MCP calls, and structured
errors. Secrets are redacted.

