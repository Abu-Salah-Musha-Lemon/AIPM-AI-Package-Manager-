"""
Remote registry synchronization.
"""

from __future__ import annotations

from pathlib import Path

import requests

from aipm.config import load_config
from aipm.logger import get_logger
import yaml

from aipm.registry.models import Registry


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
        #
        # Validate downloaded registry
        #

        try:

            with self.temp.open(
                "r",
                encoding="utf-8",
            ) as file:

                data = yaml.safe_load(file) or {}

            Registry.model_validate(
                data
            )

        except Exception as error:

            # self.temp.unlink(
            #     missing_ok=True,
            # )

            content_type = response.headers.get("Content-Type", "")

            if "text/html" in content_type.lower():
                raise RuntimeError(
                    "Registry URL returned HTML instead of registry.yaml. "
                    "Use a raw.githubusercontent.com URL."
                )

        self.log.info(
            "Registry synchronized."
        )

        return len(response.text)
   


registry_sync = RegistrySync()