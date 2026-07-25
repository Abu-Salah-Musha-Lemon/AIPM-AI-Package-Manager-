"""
Remote registry synchronization.
"""

from __future__ import annotations

from pathlib import Path

import requests

from aipm.config import load_config
from aipm.logger import get_logger


class RegistrySync:
    """
    Synchronize local registry with remote registry.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.log = get_logger(__name__)

        self.url = cfg.registry.url

        self.timeout = cfg.registry.timeout

        self.destination = (
            Path(__file__).parent
            / "registry.yaml"
        )

        self.temp = (
            Path(__file__).parent
            / "registry.tmp"
        )

        self.backup = (
            Path(__file__).parent
            / "registry.yaml.bak"
        )

    def sync(self) -> int:
        """
        Download the latest registry.
        Returns the number of downloaded bytes.
        """

        self.log.info(
            "Downloading registry..."
        )

        response = requests.get(
            self.url,
            timeout=self.timeout,
        )

        response.raise_for_status()

        self.temp.write_text(
            response.text,
            encoding="utf-8",
        )

        self.log.info(
            "Registry synchronized."
        )

        return len(response.text)
   


registry_sync = RegistrySync()