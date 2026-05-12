"""Model configuration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ModelConfig:
    """Project-level model authorization. Known is not enabled."""

    provider: str
    model_id: str
    enabled: bool = False
    available: bool = True
