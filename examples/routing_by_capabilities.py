from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.context import ContextItem
from capybara_ai.core.types import ContextType
from capybara_ai.testing import fake_runner

agent = Agent(
    AgentConfig(
        name="image_agent",
        accepted_context_types=frozenset({ContextType.IMAGE}),
    )
)

result = agent.run(
    "Describe this image.",
    fake_runner(),
    context=[ContextItem.image("https://example.test/image.png")],
)

print(result.to_dict())
