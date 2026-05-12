"""Public API for Capybara AI."""

from capybara_ai.agents.agent import Agent
from capybara_ai.agents.config import AgentConfig
from capybara_ai.agents.runner import AgentRunner
from capybara_ai.capabilities.model_card import ModelCard
from capybara_ai.capabilities.registry import CapabilityRegistry, create_default_registry
from capybara_ai.config.models import ModelConfig
from capybara_ai.config.project import ProjectConfig
from capybara_ai.config.providers import ProviderConfig
from capybara_ai.context.items import ContextItem
from capybara_ai.core.execution import ExecutionRequest, ExecutionResult
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.core.types import AdapterStatus, Capability, ContextType, ProviderName
from capybara_ai.mcp.config import MCPClientConfig
from capybara_ai.mcp.tools import MCPToolConfig
from capybara_ai.routing.router import Router

__all__ = [
    "AdapterStatus",
    "Agent",
    "AgentConfig",
    "AgentRunner",
    "Capability",
    "CapabilityRegistry",
    "ContextItem",
    "ContextType",
    "ExecutionMetadata",
    "ExecutionRequest",
    "ExecutionResult",
    "MCPClientConfig",
    "MCPToolConfig",
    "ModelCard",
    "ModelConfig",
    "ProjectConfig",
    "ProviderConfig",
    "ProviderName",
    "Router",
    "create_default_registry",
]
