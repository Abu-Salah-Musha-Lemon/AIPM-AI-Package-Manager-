from __future__ import annotations

from pydantic import BaseModel, Field

from .app import AppConfig
from .storage import StorageConfig
from .download import DownloadConfig
from .registry import RegistryConfig


class Config(BaseModel):
    """
    Root configuration.
    """

    app: AppConfig = Field(
        default_factory=AppConfig
    )

    storage: StorageConfig = Field(
        default_factory=StorageConfig
    )

    registry: RegistryConfig = Field(
        default_factory=RegistryConfig
    )

    download: DownloadConfig = Field(
        default_factory=DownloadConfig
    )