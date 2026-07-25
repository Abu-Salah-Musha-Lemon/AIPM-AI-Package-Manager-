"""
Remote registry synchronization.
"""

from __future__ import annotations

from pathlib import Path

import requests
import yaml

from aipm.config import load_config
from aipm.logger import get_logger
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

        #
        # Registry files
        #

        self.registry = (
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
        Download and safely replace the local registry.
        Returns downloaded bytes.
        """

        self.log.info(
            "Downloading registry..."
        )

        try:

            #
            # Download
            #

            response = requests.get(
                self.url,
                timeout=self.timeout,
            )

            response.raise_for_status()

            #
            # Detect HTML instead of RAW YAML
            #

            content_type = response.headers.get(
                "Content-Type",
                "",
            )

            if "text/html" in content_type.lower():

                raise RuntimeError(
                    "Registry URL returned HTML instead of registry.yaml. "
                    "Use a raw.githubusercontent.com URL."
                )

            #
            # Save to temporary file
            #

            self.temp.write_text(
                response.text,
                encoding="utf-8",
            )

            #
            # Validate YAML
            #

            with self.temp.open(
                "r",
                encoding="utf-8",
            ) as file:

                data = yaml.safe_load(file) or {}

            Registry.model_validate(
                data
            )

            #
            # Backup current registry
            #

            if self.registry.exists():

                if self.backup.exists():

                    self.backup.unlink()

                self.registry.replace(
                    self.backup
                )

            #
            # Replace registry
            #

            self.temp.replace(
                self.registry
            )

            #
            # Cleanup backup
            #

            if self.backup.exists():

                self.backup.unlink()

            self.log.info(
                "Registry synchronized."
            )

            return len(response.text.encode("utf-8"))

        except Exception as error:

            #
            # Remove temp file
            #

            if self.temp.exists():

                self.temp.unlink(
                    missing_ok=True,
                )

            #
            # Restore backup
            #

            if (
                self.backup.exists()
                and not self.registry.exists()
            ):

                self.backup.replace(
                    self.registry
                )

            raise RuntimeError(
                f"Registry sync failed: {error}"
            ) from error


registry_sync = RegistrySync()