"""Configurable agent."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from capybara_ai.agents.config import AgentConfig
from capybara_ai.core.execution import ExecutionRequest, ExecutionResult
from capybara_ai.mcp.tools import MCPToolRequest


class AgentRunnerProtocol(Protocol):
    def run(self, agent: Agent, request: ExecutionRequest) -> ExecutionResult: ...


@dataclass(slots=True)
class Agent:
    """Application-facing agent object."""

    config: AgentConfig

    @property
    def name(self) -> str:
        return self.config.name

    def build_request(
        self,
        prompt: str,
        *,
        context: list[object] | None = None,
        stream: bool = False,
        structured_schema: dict[str, object] | None = None,
        mcp_tool_requests: list[MCPToolRequest] | None = None,
    ) -> ExecutionRequest:
        full_prompt = (
            prompt if not self.config.instructions else f"{self.config.instructions}\n\n{prompt}"
        )
        return ExecutionRequest(
            prompt=full_prompt,
            context=list(context or []),
            stream=stream,
            structured_schema=structured_schema,
            mcp_tool_requests=list(mcp_tool_requests or []),
            preferred_model=self.config.preferred_model,
        )

    def run(
        self,
        prompt: str,
        runner: AgentRunnerProtocol,
        *,
        context: list[object] | None = None,
        stream: bool = False,
        structured_schema: dict[str, object] | None = None,
        mcp_tool_requests: list[MCPToolRequest] | None = None,
    ) -> ExecutionResult:
        request = self.build_request(
            prompt,
            context=context,
            stream=stream,
            structured_schema=structured_schema,
            mcp_tool_requests=mcp_tool_requests,
        )
        return runner.run(self, request)
