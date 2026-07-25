"""
Download models.
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

    PENDING = "pending"

    RUNNING = "running"

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"


class DownloadTask(BaseModel):
    """
    Download request.
    """

    name: str

    url: str

    destination: Path

    sha256: str = ""

    resume: bool = True


class DownloadResult(BaseModel):
    """
    Download result.
    """

    status: DownloadStatus

    file: Path | None = None

    bytes_downloaded: int = 0

    elapsed: float = 0.0

    message: str = ""