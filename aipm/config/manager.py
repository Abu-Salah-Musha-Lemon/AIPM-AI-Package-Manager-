"""
Configuration manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from aipm.config.defaults import create_default_config
from aipm.config.models import Config
from aipm.logger import get_logger

class ConfigManager:
    """
    Manage AIPM configuration lifecycle.
    """

    def __init__(self, path: Path | None = None) -> None:

        self.path = (
            path
            if path
            else (
                Path(__file__)
                .resolve()
                .parents[2]
                / "configs"
                / "config.yaml"
            )
        )
        self.log = get_logger(__name__)
    def exists(self) -> bool:
        """
        Check configuration file exists.
        """

        return self.path.exists()

    def create_default(self) -> Config:
        """
        Create default configuration file.
        """

        config = create_default_config()

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:

            yaml.safe_dump(
                config.model_dump(mode="json"),
                file,
                sort_keys=False,
            )

        return config

    def load(self) -> Config:
        """
        Load existing config or create new one.
        """

        if not self.exists():
            self.log.info(
                "Config file not found. Creating default config."
            )

            return self.create_default()

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = yaml.safe_load(file) or {}

        self.log.info(
            "Config loaded from config.yaml"
        )

        return Config(**data)


config_manager = ConfigManager()