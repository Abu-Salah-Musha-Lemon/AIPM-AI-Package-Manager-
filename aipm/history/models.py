"""
History models for AIPM.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import (
    BaseModel,
    Field,
)


class HistoryOperation(
    str,
    Enum,
):
    """
    Supported history operations.
    """

    INSTALL = "install"

    REMOVE = "remove"

    UPDATE = "update"

    VERIFY = "verify"

    REPAIR = "repair"

    DOWNLOAD = "download"


class HistoryStatus(
    str,
    Enum,
):
    """
    History status.
    """

    SUCCESS = "success"

    FAILED = "failed"

    CANCELLED = "cancelled"


class HistoryEntry(BaseModel):
    """
    One history record.
    """

    id: str

    operation: HistoryOperation

    model: str

    version: str = ""

    status: HistoryStatus

    started: datetime

    finished: datetime

    duration: float = 0.0

    size: int = 0

    message: str = ""


class HistoryDatabase(BaseModel):
    """
    History database.
    """

    entries: list[HistoryEntry] = Field(
        default_factory=list
    )


class HistoryQuery(BaseModel):
    """
    History search filter.
    """

    operation: HistoryOperation | None = None

    status: HistoryStatus | None = None

    limit: int | None = None