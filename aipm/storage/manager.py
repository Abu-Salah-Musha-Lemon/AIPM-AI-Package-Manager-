from __future__ import annotations

from pathlib import Path


class StorageManager:
    """
    Central storage manager.

    Every module should obtain directories from this class.
    """

    def __init__(self) -> None:

        self.root = Path.home() / ".aipm"

        self.logs = self.root / "logs"
        self.models = self.root / "models"
        self.loras = self.root / "loras"
        self.workflows = self.root / "workflows"
        self.downloads = self.root / "downloads"
        self.cache = self.root / "cache"
        self.plugins = self.root / "plugins"
        self.temp = self.root / "temp"
        self.registry = self.root / "registry"
        self.providers = self.root / "providers"
        self.configs = self.root / "configs"

    def initialize(self) -> None:
        """
        Create all directories.
        """

        directories = (
            self.root,
            self.logs,
            self.models,
            self.loras,
            self.workflows,
            self.downloads,
            self.cache,
            self.plugins,
            self.temp,
            self.registry,
            self.providers,
            self.configs,
        )

        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)


storage = StorageManager()