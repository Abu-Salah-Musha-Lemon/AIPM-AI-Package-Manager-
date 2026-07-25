"""
Download result models.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path

from pydantic import BaseModel


class DownloadStatus(
    str,
    Enum,
):
    """
    Download status.
    """

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"


class DownloadResult(BaseModel):
    """
    Download result.
    """

    status: DownloadStatus

    file: Path | None = None

    bytes_downloaded: int = 0

    elapsed: float = 0.0

    message: str = ""