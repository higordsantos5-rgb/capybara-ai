# Configuration

Configuration is explicit and owned by the consuming project.

```python
from capybara_ai.config import ModelConfig, ProjectConfig, ProviderConfig, SecretRef

config = ProjectConfig(
    providers={
        "openai": ProviderConfig(
            provider="openai",
            enabled=True,
            credential=SecretRef("consumer-provided-key"),
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

Capybara AI does not magically read `.env`, create keys, use author credentials,
or activate providers by import.

