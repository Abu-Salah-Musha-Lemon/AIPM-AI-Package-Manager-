from __future__ import annotations

from pathlib import Path


class StorageManager:
    """
    Central storage manager for AIPM.

    All application directories are created automatically
    under the user's home directory.
    """

    DIRECTORIES = (
        "logs",
        "models",
        "loras",
        "workflows",
        "downloads",
        "cache",
        "plugins",
        "temp",
        "registry",
        "providers",
        "configs",
        "backups",
    )

    def __init__(self) -> None:
        self.root = Path.home() / ".aipm"

        for directory in self.DIRECTORIES:
            setattr(self, directory, self.root / directory)

    def initialize(self) -> None:
        """Create all required directories."""

        self.root.mkdir(parents=True, exist_ok=True)

        for directory in self.DIRECTORIES:
            getattr(self, directory).mkdir(
                parents=True,
                exist_ok=True,
            )


storage = StorageManager()