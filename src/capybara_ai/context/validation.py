"""Context validation and capability derivation."""

from __future__ import annotations

from capybara_ai.context.items import ContextItem
from capybara_ai.core.errors import InvalidContextError, PipelineRequiredError
from capybara_ai.core.types import Capability, ContextType

CONTEXT_CAPABILITY_MAP: dict[ContextType, Capability] = {
    ContextType.TEXT: Capability.TEXT,
    ContextType.MARKDOWN: Capability.MARKDOWN,
    ContextType.CODE: Capability.CODE,
    ContextType.IMAGE: Capability.IMAGE,
    ContextType.PDF: Capability.PDF,
    ContextType.AUDIO: Capability.AUDIO,
    ContextType.VIDEO: Capability.VIDEO,
    ContextType.FILE: Capability.FILE,
    ContextType.MCP_RESOURCE: Capability.MCP_COMPATIBLE,
}


def required_capabilities_for_context(items: list[ContextItem]) -> set[Capability]:
    """Derive required capabilities without performing conversions."""

    required: set[Capability] = set()
    for item in items:
        if item.type is ContextType.DERIVED:
            if not item.derived_from_pipeline or item.pipeline_id is None:
                raise InvalidContextError(
                    "Derived context requires an explicit pipeline trace.",
                    details={"context_type": item.type.value},
                )
            required.add(Capability.TEXT)
            continue
        capability = CONTEXT_CAPABILITY_MAP.get(item.type)
        if capability is None:
            raise InvalidContextError(
                "Unknown context type.",
                details={"context_type": item.type.value},
            )
        required.add(capability)
    return required


def require_pipeline_for_unsupported_context(item: ContextItem) -> None:
    """Raise the explicit pipeline error used by negative multimodal tests."""

    raise PipelineRequiredError(
        "This context type requires native capability or an explicit configured pipeline.",
        details={"context_type": item.type.value, "origin": item.origin},
    )
