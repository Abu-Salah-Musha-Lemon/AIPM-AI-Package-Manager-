from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field


class StorageConfig(BaseModel):
    """
    Storage configuration.
    """

    root: Path = Field(
        default_factory=lambda: Path.home() / ".aipm"
    )

    cache: Path | None = None
    models: Path | None = None
    loras: Path | None = None
    workflows: Path | None = None
    outputs: Path | None = None
    logs: Path | None = None