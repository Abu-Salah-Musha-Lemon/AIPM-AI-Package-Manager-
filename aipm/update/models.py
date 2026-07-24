"""
Update models.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class UpdateStatus(
    str,
    Enum,
):

    UPDATED = "updated"

    SKIPPED = "skipped"

    FAILED = "failed"


class UpdateResult(BaseModel):

    status: UpdateStatus

    old_version: str = ""

    new_version: str = ""

    message: str = ""