"""
Storage manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config import load_config
from aipm.logger import get_logger
from aipm.storage.models import (
    StorageInfo,
)

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
    def get(
    self,
    name: str,
    ) -> Path | None:
        """
        Alias of get_path().
        """

        return self.get_path(
            name
        )


    def list(
        self,
    ) -> dict[str, Path]:
        """
        Return all storage directories.
        """

        return dict(
            self.directories
        )


    def create(
        self,
        name: str,
    ) -> bool:
        """
        Create a storage directory.
        """

        path = self.get_path(
            name
        )

        if path is None:

            return False

        path.mkdir(
            parents=True,
            exist_ok=True,
        )

        return True


    def ensure(
        self,
        name: str,
    ) -> Path | None:
        """
        Ensure storage directory exists.
        """

        if self.create(
            name
        ):

            return self.get_path(
                name
            )

        return None


    def delete(
        self,
        name: str,
    ) -> bool:
        """
        Delete an empty storage directory.
        """

        path = self.get_path(
            name
        )

        if path is None:

            return False

        if not path.exists():

            return False

        if any(
            path.iterdir()
        ):

            return False

        path.rmdir()

        return True


    def size(
        self,
        name: str,
    ) -> int:
        """
        Return directory size in bytes.
        """

        path = self.get_path(
            name
        )

        if (
            path is None
            or not path.exists()
        ):

            return 0

        total = 0

        for file in path.rglob("*"):

            if file.is_file():

                total += (
                    file.stat().st_size
                )

        return total


    def is_empty(
        self,
        name: str,
    ) -> bool:
        """
        Check directory is empty.
        """

        path = self.get_path(
            name
        )

        if (
            path is None
            or not path.exists()
        ):

            return True

        return not any(
            path.iterdir()
        )


    def info(
        self,
        name: str,
    ) -> StorageInfo | None:
        """
        Return storage information.
        """

        from aipm.storage.models import (
            StorageInfo,
        )

        path = self.get_path(
            name
        )

        if path is None:

            return None

        return StorageInfo(

            name=name,

            path=path,

            exists=path.exists(),

            size=self.size(
                name
            ),

            empty=self.is_empty(
                name
            ),

        )



storage_manager = StorageManager()