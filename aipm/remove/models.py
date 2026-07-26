"""
Remove result models.
"""

from __future__ import annotations

from pydantic import BaseModel


class RemoveResult(BaseModel):
    """
    Remove operation result.
    """

    success: bool

    removed_files: int = 0

    removed_bytes: int = 0

    message: str = ""