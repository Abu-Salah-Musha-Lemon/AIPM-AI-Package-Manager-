"""
Default configuration values for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config.models import (
    AppConfig,
    Config,
    DownloadConfig,
    StorageConfig,
)


def create_default_config() -> Config:
    """
    Create default AIPM configuration.

    Returns
    -------
    Config
        Default validated configuration object.
    """

    root = Path.home() / ".aipm"

    storage = StorageConfig(
        root=root,
        cache=root / "cache",
        models=root / "models",
        loras=root / "loras",
        workflows=root / "workflows",
        outputs=root / "outputs",
        logs=root / "logs",
    )

    return Config(
        app=AppConfig(),
        storage=storage,
        download=DownloadConfig(),
    )