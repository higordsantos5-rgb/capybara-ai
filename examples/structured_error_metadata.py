from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.config import ProjectConfig
from capybara_ai.testing import fake_runner

runner = fake_runner()
runner.project_config = ProjectConfig()

result = Agent(AgentConfig(name="error_example")).run(
    "This cannot run because no provider is configured.",
    runner,
)

print("success:", result.success)
print("blocked:", result.blocked)
print("error:", result.error.to_dict() if result.error else None)
print("metadata:", result.metadata.to_dict())
