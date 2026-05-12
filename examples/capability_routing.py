from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(AgentConfig(name="routing_example"))

result = agent.run("Write one sentence about explicit model capabilities.", fake_runner())

print("success:", result.success)
print("provider:", result.metadata.provider_selected)
print("model:", result.metadata.model_selected)
print("required:", result.metadata.required_capabilities)
print("output:", result.output)
