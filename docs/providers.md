# Providers

Adapters declare one status:

- `real`;
- `experimental`;
- `contract`;
- `mock`.

Adapter status is not the same as provider activation.

| Provider | Status | Runtime |
|---|---|---|
| Fake/Test | `mock` | Local, no API key. |
| OpenAI | `real` | Optional SDK and consumer API key. |
| Gemini | `experimental` | Placeholder without base runtime SDK. |
| Anthropic | `experimental` | Placeholder without base runtime SDK. |
| xAI | `contract` | Cannot execute as real. |
| DeepSeek | `contract` | Cannot execute as real. |
| Meta | `contract` | Cannot execute as real. |

SDKs are restricted to adapters. The core must not import provider SDKs.

To add a provider, implement the provider adapter port, declare status,
capabilities, limitations, credentials, tests, and docs. Do not mark an adapter
`real` without official documentation, dependency, credential handling, contract
tests, examples/docs, and no false streaming or structured output.

