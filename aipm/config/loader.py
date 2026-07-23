"""
Configuration loader for AIPM.
"""

from __future__ import annotations

from aipm.config.manager import config_manager
from aipm.config.models import Config


def load_config() -> Config:
    """
    Load application configuration.

    Delegates configuration handling
    to ConfigManager.
    """

    return config_manager.load()