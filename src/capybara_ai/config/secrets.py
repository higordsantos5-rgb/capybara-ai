"""Secret handling helpers."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecretRef:
    """Consumer-provided secret value that redacts itself in repr."""

    value: str
    source: str = "consumer_project"

    def reveal(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return "SecretRef(value='[REDACTED]', source='[REDACTED]')"

    def __str__(self) -> str:
        return "[REDACTED]"
