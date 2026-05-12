from capybara_ai.agents import Agent, AgentConfig, AgentRunner
from capybara_ai.capabilities import create_default_registry
from capybara_ai.config import ProjectConfig
from capybara_ai.routing import Router

runner = AgentRunner(project_config=ProjectConfig(), router=Router(create_default_registry()))
result = Agent(AgentConfig(name="blocked")).run("This should not call a provider.", runner)

print(result.to_dict())
