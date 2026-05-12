# Provider Configuration

Provider configuration is explicit by design.

```python
from capybara_ai.config import ModelConfig, ProjectConfig, ProviderConfig, SecretRef

config = ProjectConfig(
    providers={
        "openai": ProviderConfig(
            provider="openai",
            enabled=True,
            credential=SecretRef("consumer-owned-key"),
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
```

Three things are separate:

- framework support for a provider;
- project configuration that enables it;
- runtime availability and credentials.

This prevents accidental usage of providers or models just because their adapter
or model card exists.

