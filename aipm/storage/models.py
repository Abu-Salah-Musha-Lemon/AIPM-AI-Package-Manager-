"""
Storage models for AIPM.
"""

from __future__ import annotations

from enum import Enum

from pathlib import Path

from pydantic import BaseModel


class StorageStatus(
    str,
    Enum,
):
    """
    Storage operation status.
    """

    SUCCESS = "success"

    FAILED = "failed"

    NOT_FOUND = "not_found"


class StorageInfo(BaseModel):
    """
    Information about a storage directory.
    """

    name: str

    path: Path

    exists: bool

    size: int = 0

    empty: bool = True


class StorageResult(BaseModel):
    """
    Storage operation result.
    """

    status: StorageStatus

    message: str = ""

    info: StorageInfo | None = None