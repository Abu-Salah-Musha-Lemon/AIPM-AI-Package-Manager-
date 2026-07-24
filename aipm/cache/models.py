"""
Cache models.
"""

from __future__ import annotations
from aipm.logger import get_logger

from pydantic import BaseModel


class CacheEntry(BaseModel):
    name: str
    sha256: str
    size: int
    path: str


class CacheDatabase(BaseModel):
    models: list[CacheEntry] = []