"""
Model metadata definitions for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class ModelMetadata(BaseModel):
    """
    AI model metadata.
    """

    name: str

    type: str = "unknown"

    format: str = "unknown"

    architecture: str = "unknown"

    size: str = "unknown"

    source: str = "unknown"

    path: Path | None = None