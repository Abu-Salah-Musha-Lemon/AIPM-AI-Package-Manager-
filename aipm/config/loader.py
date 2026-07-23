"""
Configuration loader for AIPM.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from aipm.config.defaults import create_default_config
from aipm.config.models import Config


CONFIG_PATH = (
    Path(__file__).resolve()
    .parents[2]
    / "configs"
    / "config.yaml"
)


def load_config() -> Config:
    """
    Load AIPM configuration.

    If configuration file does not exist,
    default configuration will be returned.
    """

    if not CONFIG_PATH.exists():
        return create_default_config()

    with CONFIG_PATH.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = yaml.safe_load(file) or {}

    return Config(**data)