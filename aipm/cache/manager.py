"""
Cache manager.
"""

from __future__ import annotations

from pathlib import Path

from aipm.logger import get_logger
from aipm.config import load_config
from aipm.cache.models import (
    CacheDatabase,
    CacheEntry,
)


class CacheManager:
    """
    Manage local cache database.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.log = get_logger(__name__)

        self.path = (
            cfg.storage.root
            / "cache.json"
        )

    def load(
        self,
    ) -> CacheDatabase:
        """
        Load cache database.
        """

        if not self.path.exists():

            return CacheDatabase()

        return CacheDatabase.model_validate_json(
            self.path.read_text(
                encoding="utf-8",
            )
        )

    def save(
        self,
        db: CacheDatabase,
    ) -> None:
        """
        Save cache database.
        """

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.path.write_text(
            db.model_dump_json(
                indent=4,
            ),
            encoding="utf-8",
        )

    def add(
        self,
        entry: CacheEntry,
    ) -> None:
        """
        Add or update cache entry.
        """

        db = self.load()

        db.models = [
            model
            for model in db.models
            if model.name.lower()
            != entry.name.lower()
        ]

        db.models.append(entry)

        self.save(db)

        self.log.info(
            f"Cached model: {entry.name}"
        )

    def get(
        self,
        name: str,
    ) -> CacheEntry | None:
        """
        Get cache entry.
        """

        db = self.load()

        for model in db.models:

            if (
                model.name.lower()
                == name.lower()
            ):
                return model

        return None

    def remove(
        self,
        name: str,
    ) -> bool:
        """
        Remove a model from cache.
        """

        db = self.load()

        original_count = len(
            db.models
        )

        db.models = [
            model
            for model in db.models
            if (
                model.name.lower()
                != name.lower()
            )
        ]

        if (
            len(db.models)
            == original_count
        ):

            self.log.info(
                f"Cache entry not found: {name}"
            )

            return False

        self.save(db)

        self.log.info(
            f"Removed cache entry: {name}"
        )

        return True


cache_manager = CacheManager()