from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    """
    Application metadata configuration.
    """

    name: str = "AIPM"
    version: str = "0.1.0-alpha.1"


class StorageConfig(BaseModel):
    """
    Application storage configuration.
    """

    root: Path = Field(
        default_factory=lambda: Path.home() / ".aipm"
    )

    cache: Path | None = None
    models: Path | None = None
    loras: Path | None = None
    workflows: Path | None = None
    outputs: Path | None = None
    logs: Path | None = None


class DownloadConfig(BaseModel):
    """
    Download engine configuration.
    """

    workers: int = 4
    timeout: int = 60
    retries: int = 3
    verify_sha256: bool = True


class Config(BaseModel):
    """
    Root AIPM configuration model.
    """

    app: AppConfig = Field(
        default_factory=AppConfig
    )

    storage: StorageConfig = Field(
        default_factory=StorageConfig
    )

    download: DownloadConfig = Field(
        default_factory=DownloadConfig
    )