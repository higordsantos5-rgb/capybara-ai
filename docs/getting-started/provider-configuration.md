# Provider Configuration

Capybara AI keeps provider setup in project configuration so your application
has one clear place for allowed providers, enabled models, credentials, adapter
status policy, and fallback behavior.

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

Three states are intentionally separate:

- the framework has an adapter for a provider;
- your project enables and configures that provider;
- the provider is available at runtime with valid credentials.

The same split applies to models. A model can be known in the capability
registry without being enabled for your project.
