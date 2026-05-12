from pathlib import Path

from capybara_ai.agents import Agent, AgentConfig
from capybara_ai.capabilities import create_default_registry
from capybara_ai.config import ModelConfig, ProjectConfig, ProviderConfig, SecretRef
from capybara_ai.context import ContextItem
from capybara_ai.core.errors import ConfigurationError
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import ContextType
from capybara_ai.mcp import (
    MCPClient,
    MCPClientConfig,
    MCPPermissions,
    MCPServerConfig,
    MCPToolConfig,
    MCPToolRequest,
)
from capybara_ai.testing import fake_runner


def test_fake_agent_runs_without_api_key():
    agent = Agent(AgentConfig(name="tester"))
    result = agent.run("hello", fake_runner())

    assert result.success is True
    assert result.output == "fake: hello"
    assert result.metadata.provider_selected == "fake"
    assert result.metadata.model_selected == "fake-text"


def test_supported_provider_not_configured_cannot_be_used():
    runner = fake_runner()
    runner.project_config = ProjectConfig()
    agent = Agent(AgentConfig(name="tester"))

    result = agent.run("hello", runner)

    assert result.success is False
    assert result.blocked is True
    assert result.error is not None
    assert result.error.code == "no_eligible_model"


def test_known_model_not_enabled_cannot_be_routed():
    config = ProjectConfig(
        providers={"fake": ProviderConfig(provider="fake", enabled=True)},
        models={},
    )
    runner = fake_runner()
    runner.project_config = config
    result = Agent(AgentConfig(name="tester")).run("hello", runner)

    assert result.success is False
    assert result.error is not None
    assert result.error.code == "no_eligible_model"
    assert any(
        d.reason == "model_not_enabled_by_project" for d in result.metadata.routing_decisions
    )


def test_missing_capability_blocks_execution_before_provider():
    agent = Agent(AgentConfig(name="tester", accepted_context_types=frozenset({ContextType.IMAGE})))
    result = agent.run(
        "describe", fake_runner(), context=[ContextItem.image("https://example.test/a.png")]
    )

    assert result.success is False
    assert result.blocked is True
    assert result.error is not None
    assert result.error.code == "no_eligible_model"
    assert any("missing_capabilities:image" in d.reason for d in result.metadata.routing_decisions)


def test_pdf_audio_video_incompatible_block_without_parsing_or_transcription():
    agent = Agent(
        AgentConfig(
            name="tester",
            accepted_context_types=frozenset(
                {ContextType.PDF, ContextType.AUDIO, ContextType.VIDEO}
            ),
        )
    )
    for context_type in (ContextType.PDF, ContextType.AUDIO, ContextType.VIDEO):
        item = ContextItem(type=context_type, content="opaque-ref", origin="test")
        result = agent.run("inspect", fake_runner(), context=[item])
        assert result.success is False
        assert result.error is not None
        assert result.error.code == "no_eligible_model"


def test_fallback_not_authorized_does_not_route_other_model():
    config = ProjectConfig(
        providers={"fake": ProviderConfig(provider="fake", enabled=True)},
        models={
            ("fake", "fake-text"): ModelConfig(provider="fake", model_id="fake-text", enabled=True)
        },
    )
    runner = fake_runner()
    runner.project_config = config
    agent = Agent(AgentConfig(name="tester", preferred_model="not-enabled"))

    result = agent.run("hello", runner)

    assert result.success is False
    assert any(
        d.reason == "preferred_model_mismatch_and_fallback_disabled"
        for d in result.metadata.routing_decisions
    )


def test_secret_is_redacted_from_errors_and_metadata():
    secret = SecretRef("sk-test-secret")
    assert "sk-test-secret" not in repr(secret)
    error = ConfigurationError(
        "redaction check",
        details={"api_key": secret.reveal(), "nested": {"token": secret.reveal()}},
    )

    assert "sk-test-secret" not in str(error.to_dict())


def test_contract_adapter_does_not_execute_as_real():
    config = ProjectConfig(
        providers={"xai": ProviderConfig(provider="xai", enabled=True, credential=SecretRef("x"))},
        models={
            ("xai", "xai-default"): ModelConfig(
                provider="xai", model_id="xai-default", enabled=True
            )
        },
    )
    runner = fake_runner()
    runner.project_config = config

    result = Agent(AgentConfig(name="tester")).run("hello", runner)

    assert result.success is False
    assert any(
        d.reason == "adapter_status_not_allowed_by_policy"
        for d in result.metadata.routing_decisions
    )


def test_adapter_statuses_are_declared_honestly():
    registry = create_default_registry()
    statuses = {
        (card.provider, card.model_id): card.adapter_status.value for card in registry.all_cards()
    }

    assert statuses[("fake", "fake-text")] == "mock"
    assert statuses[("openai", "gpt-5")] == "real"
    assert statuses[("gemini", "gemini-default")] == "experimental"
    assert statuses[("anthropic", "anthropic-default")] == "experimental"
    assert statuses[("xai", "xai-default")] == "contract"


def test_streaming_and_structured_output_are_not_simulated_by_fake_adapter():
    agent = Agent(AgentConfig(name="tester"))

    streaming = agent.run("hello", fake_runner(), stream=True)
    structured = agent.run("hello", fake_runner(), structured_schema={"type": "object"})

    assert streaming.success is False
    assert structured.success is False
    assert any(
        d.reason == "streaming_or_structured_output_requires_real_adapter"
        or "missing_capabilities:streaming" in d.reason
        for d in streaming.metadata.routing_decisions
    )
    assert any(
        d.reason == "streaming_or_structured_output_requires_real_adapter"
        or "missing_capabilities:structured_output" in d.reason
        for d in structured.metadata.routing_decisions
    )


def test_mcp_default_deny_and_allowlist():
    client = MCPClient(MCPClientConfig())
    request = MCPToolRequest(name="read_notes", required_permissions=MCPPermissions(read=True))

    try:
        client.execute(request, ExecutionMetadata(agent_name="tester"))
    except Exception as exc:
        assert getattr(exc, "code", "") == "mcp_configuration_error"
    else:
        raise AssertionError("MCP without configuration must be denied")

    mcp_config = MCPClientConfig(
        enabled=True,
        servers={"local": MCPServerConfig(name="local", transport="local", enabled=True)},
        tools={
            "read_notes": MCPToolConfig(
                name="read_notes",
                server_name="local",
                scope="notes",
                permissions=MCPPermissions(read=True),
                allowlisted=True,
            )
        },
    )
    client = MCPClient(mcp_config)
    client.register_local_executor("read_notes", lambda args: {"ok": args["id"]})

    exec_metadata = ExecutionMetadata(agent_name="tester")
    result = client.execute(
        MCPToolRequest(
            name="read_notes", arguments={"id": 1}, required_permissions=MCPPermissions(read=True)
        ),
        exec_metadata,
    )

    assert result.output == {"ok": 1}
    assert exec_metadata.mcp_calls[0].read is True


def test_packaging_names_and_gitignore():
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    gitignore = Path(".gitignore").read_text(encoding="utf-8")

    assert 'name = "capybara-ai"' in pyproject
    assert ".venv/" in gitignore
    assert ".env" in gitignore
    assert "mcp__codex_apps__github" not in pyproject
