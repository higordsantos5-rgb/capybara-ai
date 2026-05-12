"""Agent result aliases."""

from __future__ import annotations

from dataclasses import dataclass

from capybara_ai.core.execution import ExecutionResult


@dataclass(frozen=True, slots=True)
class AgentRunResult:
    """Thin wrapper for a normalized execution result."""

    execution: ExecutionResult
