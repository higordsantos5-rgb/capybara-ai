from examples.openai_provider_config import agent, runner

result = agent.run("Stream one short sentence.", runner, stream=True)
print(result.to_dict())
