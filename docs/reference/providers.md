# Providers Reference

Capybara AI separates provider support from project activation. An adapter can
ship with the framework, but routing can use it only when the project enables
the provider, enables a compatible model, supplies required credentials, and
allows the adapter status.

## Adapter Status

| Provider | Status | Description |
|---|---|---|
| Fake/Test | `mock` | Local adapter for tests, examples, and CI. |
| OpenAI | `real` | Optional extra with consumer-provided credentials. |
| Gemini | `experimental` | Declared adapter surface with limited maturity. |
| Anthropic | `experimental` | Declared adapter surface with limited maturity. |
| xAI | `contract` | Contract only; not executed as a real adapter. |
| DeepSeek | `contract` | Contract only; not executed as a real adapter. |
| Meta | `contract` | Contract only; not executed as a real adapter. |

## Runtime Requirements

Provider execution depends on all of these being true:

- the provider is supported by an adapter;
- the project enables the provider;
- credentials are configured when required;
- the model is enabled in project config;
- required capabilities match the model card;
- policy allows the adapter status;
- the provider is available at runtime.
