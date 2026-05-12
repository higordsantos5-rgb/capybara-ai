# Provider Adapters

Provider adapters isolate external SDKs from the provider-agnostic core. Your
application configures which adapters are usable in a given project.

Adapter status communicates maturity:

- `mock`: local adapter for tests and examples;
- `real`: backed by an implemented provider integration;
- `experimental`: available surface with limited maturity;
- `contract`: declared interface that should not execute as a real provider.

Use adapter status in project policy to match your risk tolerance. For example,
tests can rely on Fake/Test, internal experiments can allow experimental
adapters, and production code can restrict routing to real adapters.
