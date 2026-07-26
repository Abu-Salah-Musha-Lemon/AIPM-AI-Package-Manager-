"""
Update result models.
"""

from __future__ import annotations

from pydantic import BaseModel


class UpdateResult(BaseModel):
    """
    Result of a model update.
    """

    success: bool

    updated: bool = False

    downloaded: bool = False

    verified: bool = False

    message: str = ""