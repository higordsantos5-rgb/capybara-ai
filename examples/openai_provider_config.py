import os

from capybara_ai.agents import Agent, AgentConfig, AgentRunner
from capybara_ai.capabilities import create_default_registry
from capybara_ai.config import ModelConfig, ProjectConfig, ProviderConfig, SecretRef
from capybara_ai.routing import Router

# The API key belongs to the consuming project. Do not commit a real .env file.
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Set OPENAI_API_KEY before running this example.")

config = ProjectConfig(
    providers={
        "openai": ProviderConfig(provider="openai", enabled=True, credential=SecretRef(api_key))
    },
    models={("openai", "gpt-5"): ModelConfig(provider="openai", model_id="gpt-5", enabled=True)},
)

runner = AgentRunner(project_config=config, router=Router(create_default_registry()))
agent = Agent(AgentConfig(name="openai_example"))

result = agent.run("Return one short sentence about capability-first routing.", runner)
print(result.to_dict())
