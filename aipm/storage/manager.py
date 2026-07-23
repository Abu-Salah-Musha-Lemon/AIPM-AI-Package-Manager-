"""
Storage manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config import load_config
from aipm.logger import get_logger


class StorageManager:
    """
    Manage AIPM storage directories.
    """

    def __init__(
        self,
        root: Path | None = None,
    ) -> None:

        cfg = load_config()

        self.log = get_logger(
            __name__,
            cfg.storage.logs,
        )

        self.root = (
            root
            if root
            else cfg.storage.root
        )

        self.directories = {
            "cache": cfg.storage.cache,
            "models": cfg.storage.models,
            "loras": cfg.storage.loras,
            "workflows": cfg.storage.workflows,
            "outputs": cfg.storage.outputs,
            "logs": cfg.storage.logs,
        }


    def initialize(self) -> None:
        """
        Create required storage folders.
        """

        self.root.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.log.info(
            "Initializing AIPM storage"
        )

        for name, path in self.directories.items():

            path.mkdir(
                parents=True,
                exist_ok=True,
            )

            self.log.info(
                "Storage initialized: %s",
                name,
            )


    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check storage directory exists.
        """

        if name not in self.directories:
            return False

        return self.directories[name].exists()


    def get_path(
        self,
        name: str,
    ) -> Path | None:
        """
        Return storage path.
        """

        return self.directories.get(name)



storage_manager = StorageManager()