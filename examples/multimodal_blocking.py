from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.context import ContextItem
from capybara_ai.core.types import ContextType
from capybara_ai.testing import fake_runner

agent = Agent(
    AgentConfig(
        name="multimodal_guard",
        accepted_context_types=frozenset({ContextType.IMAGE}),
    )
)

result = agent.run(
    "Describe this image.",
    fake_runner(),
    context=[ContextItem.image("https://example.test/diagram.png")],
)

print("success:", result.success)
print("error:", result.error.to_dict() if result.error else None)
print("routing decisions:")
for decision in result.metadata.routing_decisions:
    print("-", decision.provider, decision.model, decision.accepted, decision.reason)
