from examples.openai_provider_config import agent, runner

schema = {
    "type": "object",
    "additionalProperties": False,
    "properties": {"message": {"type": "string"}},
    "required": ["message"],
}

result = agent.run("Return a JSON object with a message.", runner, structured_schema=schema)
print(result.to_dict())
