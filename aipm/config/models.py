from pathlib import Path

from pydantic import BaseModel


class AppConfig(BaseModel):
    name: str
    version: str


class StorageConfig(BaseModel):
    root: Path
    cache: Path
    models: Path
    loras: Path
    workflows: Path
    outputs: Path
    logs: Path


class DownloadConfig(BaseModel):
    workers: int
    timeout: int
    retries: int
    verify_sha256: bool


class Config(BaseModel):
    app: AppConfig
    storage: StorageConfig
    download: DownloadConfig