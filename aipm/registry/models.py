"""
Registry models.
"""

from __future__ import annotations

from pydantic import BaseModel


class RegistryEntry(BaseModel):
    """
    AI model registry entry.
    """

    name: str
    version: str
    architecture: str
    type: str
    framework: str
    format: str
    size: str
    sha256: str
    url: str
    description: str


class Registry(BaseModel):
    """
    Registry database.
    """

    models: list[RegistryEntry]