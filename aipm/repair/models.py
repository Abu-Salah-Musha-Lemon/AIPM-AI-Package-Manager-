"""
Repair result models.
"""

from __future__ import annotations

from pydantic import BaseModel


class RepairResult(BaseModel):
    """
    Result returned after attempting
    to repair a model.
    """

    success: bool

    repaired: bool = False

    downloaded: bool = False

    verified: bool = False

    message: str = ""