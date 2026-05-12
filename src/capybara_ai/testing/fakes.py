"""Reusable fake configurations."""

from __future__ import annotations

from capybara_ai.agents.runner import AgentRunner
from capybara_ai.capabilities.registry import create_default_registry
from capybara_ai.config.models import ModelConfig
from capybara_ai.config.project import ProjectConfig
from capybara_ai.config.providers import ProviderConfig
from capybara_ai.core.types import ProviderName
from capybara_ai.routing.router import Router


def fake_project_config() -> ProjectConfig:
    return ProjectConfig(
        providers={
            ProviderName.FAKE.value: ProviderConfig(provider=ProviderName.FAKE.value, enabled=True)
        },
        models={
            (ProviderName.FAKE.value, "fake-text"): ModelConfig(
                provider=ProviderName.FAKE.value,
                model_id="fake-text",
                enabled=True,
            )
        },
    )


def fake_runner() -> AgentRunner:
    registry = create_default_registry()
    return AgentRunner(project_config=fake_project_config(), router=Router(registry=registry))
