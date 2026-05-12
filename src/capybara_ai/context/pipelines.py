"""Explicit multimodal pipeline contracts."""

from __future__ import annotations

from dataclasses import dataclass, field

from capybara_ai.core.types import Capability, ContextType


@dataclass(frozen=True, slots=True)
class PipelineTrace:
    """Trace that proves a context item came from an explicit pipeline."""

    pipeline_id: str
    input_type: ContextType
    output_type: ContextType
    transformation: str
    origin: str
    tool_or_model: str | None = None
    performed_reading: bool = False
    performed_extraction: bool = False
    performed_transcription: bool = False
    performed_conversion: bool = False
    performed_summary: bool = False
    resulting_capabilities: frozenset[Capability] = field(default_factory=frozenset)
    limitations: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ExplicitPipeline:
    """Configured pipeline. Pipelines never become native model support."""

    pipeline_id: str
    input_type: ContextType
    output_type: ContextType
    resulting_capabilities: frozenset[Capability]
    transformation: str
    limitations: tuple[str, ...] = ()
