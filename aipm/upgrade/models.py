"""
Upgrade result models.
"""

from __future__ import annotations

from pydantic import BaseModel


class UpgradeResult(BaseModel):
    """
    Result returned after upgrading
    an installed model.
    """

    success: bool

    upgraded: bool = False

    downloaded: bool = False

    verified: bool = False

    message: str = ""