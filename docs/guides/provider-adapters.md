# Provider Adapters

Adapters isolate provider SDKs from the core framework.

Adapter status values:

- `real`: runtime implementation exists and has contract tests/docs.
- `experimental`: shape exists, runtime maturity is limited.
- `contract`: interface exists but cannot execute as a real provider.
- `mock`: local/test adapter.

SDK imports belong inside adapters. The core stays provider-agnostic.

