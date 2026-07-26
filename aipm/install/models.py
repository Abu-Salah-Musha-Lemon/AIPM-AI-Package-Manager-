"""
Installation models for AIPM.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path

from pydantic import BaseModel


class InstallStatus(
    str,
    Enum,
):
    """
    Installation status.
    """

    SUCCESS = "success"

    SKIPPED = "skipped"

    FAILED = "failed"


class InstallResult(BaseModel):
    """
    Installation result.
    """

    status: InstallStatus

    name: str = ""

    version: str = ""

    path: Path | None = None

    message: str = ""