"""Context item representations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from capybara_ai.core.types import ContextType


@dataclass(frozen=True, slots=True)
class ContextItem:
    """One explicit context item supplied by the consuming project."""

    type: ContextType
    content: Any
    origin: str
    metadata: dict[str, Any] = field(default_factory=dict)
    derived_from_pipeline: bool = False
    pipeline_id: str | None = None

    @classmethod
    def text(cls, content: str, *, origin: str = "user") -> ContextItem:
        return cls(type=ContextType.TEXT, content=content, origin=origin)

    @classmethod
    def image(cls, content: Any, *, origin: str = "user") -> ContextItem:
        return cls(type=ContextType.IMAGE, content=content, origin=origin)
