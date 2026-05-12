# First Agent

Use the Fake/Test provider to learn the framework without credentials.

```python
from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(
    AgentConfig(
        name="support_assistant",
        instructions="Answer clearly and briefly.",
    )
)

result = agent.run("What is capability-first routing?", fake_runner())

print(result.output)
print(result.metadata.provider_selected)
print(result.metadata.model_selected)
```

The runner validates the request, selects `fake/fake-text`, executes the local
adapter, and returns structured metadata.

