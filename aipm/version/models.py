"""
Version models for AIPM.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class VersionStatus(
    str,
    Enum,
):
    """
    Version command status.
    """

    SUCCESS = "success"

    FAILED = "failed"


class VersionResult(BaseModel):
    """
    Version command result.
    """

    status: VersionStatus

    application: str = ""

    version: str = ""

    python: str = ""

    platform: str = ""

    message: str = ""