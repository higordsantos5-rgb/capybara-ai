from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.testing import fake_runner

agent = Agent(AgentConfig(name="assistant", instructions="Answer concisely."))
result = agent.run("Hello from Capybara AI.", fake_runner())

print(result.to_dict())
