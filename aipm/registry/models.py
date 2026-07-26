"""
Registry models.
"""

from __future__ import annotations

from enum import Enum

from pydantic import (
    BaseModel,
    Field,
)


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

    size: str = "Unknown"

    sha256: str | None = None

    url: str

    description: str = ""


class Registry(BaseModel):
    """
    Registry database.
    """

    models: list[RegistryEntry] = Field(
        default_factory=list
    )


#
# Result Models
#

class RegistryStatus(
    str,
    Enum,
):

    SUCCESS = "success"

    EMPTY = "empty"

    FAILED = "failed"


class RegistryResult(BaseModel):
    """
    Generic registry result.
    """

    status: RegistryStatus

    models: list[RegistryEntry] = Field(
        default_factory=list
    )

    message: str = ""