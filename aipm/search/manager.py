"""
Search models for AIPM.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class SearchStatus(
    str,
    Enum,
):
    """
    Search operation status.
    """

    SUCCESS = "success"

    EMPTY = "empty"

    FAILED = "failed"


class SearchItem(BaseModel):
    """
    One search result.
    """

    name: str

    version: str = ""

    architecture: str = ""

    type: str = ""

    installed: bool = False

    source: str = ""

    description: str = ""


class SearchResult(BaseModel):
    """
    Search results.
    """

    status: SearchStatus

    items: list[SearchItem] = []

    message: str = ""