"""Agent runner."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.agents.agent import Agent
from capybara_ai.config.project import ProjectConfig
from capybara_ai.context.items import ContextItem
from capybara_ai.context.validation import required_capabilities_for_context
from capybara_ai.core.errors import CapybaraAIError, InvalidContextError
from capybara_ai.core.execution import ExecutionRequest, ExecutionResult
from capybara_ai.core.metadata import ExecutionMetadata
from capybara_ai.mcp.client import MCPClient
from capybara_ai.mcp.tools import MCPToolRequest
from capybara_ai.routing.router import Router


@dataclass(slots=True)
class AgentRunner:
    """Orchestrates validation, routing, MCP policy, and provider execution."""

    project_config: ProjectConfig
    router: Router
    mcp_client: MCPClient | None = None

    def run(self, agent: Agent, request: ExecutionRequest) -> ExecutionResult:
        metadata = ExecutionMetadata(agent_name=agent.name)
        try:
            self._validate_agent_context(agent, request)
            self._execute_mcp_requests(agent, request, metadata)
            context_capabilities = required_capabilities_for_context(
                [item for item in request.context if isinstance(item, ContextItem)]
            )
            request.required_capabilities.update(context_capabilities)
            metadata.context_items = [
                {
                    "type": item.type.value,
                    "origin": item.origin,
                    "derived_from_pipeline": item.derived_from_pipeline,
                    "pipeline_id": item.pipeline_id,
                }
                for item in request.context
                if isinstance(item, ContextItem)
            ]
            selection = self.router.route(request, self.project_config, metadata)
            if (
                agent.config.allowed_providers
                and selection.card.provider not in agent.config.allowed_providers
            ):
                raise InvalidContextError(
                    "Selected provider is not allowed by agent configuration.",
                    details={"provider": selection.card.provider, "agent": agent.name},
                )
            if (
                agent.config.allowed_models
                and selection.card.model_id not in agent.config.allowed_models
            ):
                raise InvalidContextError(
                    "Selected model is not allowed by agent configuration.",
                    details={"model": selection.card.model_id, "agent": agent.name},
                )
            provider_config = self.project_config.require_provider_configured(
                selection.card.provider,
                requires_credentials=selection.adapter.requires_credentials,
            )
            credential = provider_config.credential.reveal() if provider_config.credential else None
            response = selection.adapter.execute(request, selection.card, credential, metadata)
        except CapybaraAIError as exc:
            return ExecutionResult.block(exc, metadata)
        except Exception as exc:  # noqa: BLE001
            error = CapybaraAIError(
                "Unexpected execution failure.",
                details={"error_type": type(exc).__name__},
            )
            return ExecutionResult.fail(error, metadata)
        return ExecutionResult.ok(response.output, metadata)

    def _validate_agent_context(self, agent: Agent, request: ExecutionRequest) -> None:
        for item in request.context:
            if (
                isinstance(item, ContextItem)
                and item.type not in agent.config.accepted_context_types
            ):
                raise InvalidContextError(
                    "Context type is not accepted by this agent.",
                    details={"context_type": item.type.value, "agent": agent.name},
                )

    def _execute_mcp_requests(
        self,
        agent: Agent,
        request: ExecutionRequest,
        metadata: ExecutionMetadata,
    ) -> None:
        if not request.mcp_tool_requests:
            return
        if self.mcp_client is None:
            raise InvalidContextError(
                "Agent requested MCP tools but no MCP client was supplied.",
                details={"agent": agent.name},
            )
        for tool_request in request.mcp_tool_requests:
            if not isinstance(tool_request, MCPToolRequest):
                raise InvalidContextError(
                    "MCP tool request is malformed.",
                    details={"agent": agent.name},
                )
            if tool_request.name not in agent.config.allowed_mcp_tools:
                raise InvalidContextError(
                    "MCP tool is not allowed by agent configuration.",
                    details={"tool": tool_request.name, "agent": agent.name},
                )
            self.mcp_client.execute(tool_request, metadata)
