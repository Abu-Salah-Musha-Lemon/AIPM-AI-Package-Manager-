"""
Cache manager.
"""

from __future__ import annotations

from pathlib import Path
from aipm.logger import get_logger

import json

from aipm.config import load_config
from aipm.cache.models import (
    CacheDatabase,
    CacheEntry,
)


class CacheManager:

    def __init__(self):

        cfg = load_config()

        self.path = (
            cfg.storage.root
            / "cache.json"
        )

    def load(self) -> CacheDatabase:

        if not self.path.exists():

            return CacheDatabase()

        return CacheDatabase.model_validate_json(
            self.path.read_text(
                encoding="utf-8"
            )
        )

    def save(
        self,
        db: CacheDatabase,
    ) -> None:

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

        db = self.load()

        db.models = [
            x
            for x in db.models
            if x.name != entry.name
        ]

        db.models.append(entry)

        self.save(db)

    def get(
        self,
        name: str,
    ) -> CacheEntry | None:

        db = self.load()

        for item in db.models:

            if item.name == name:
                return item

        return None
    def remove(
        self,
        name: str,
    ) -> bool:
        """
        Remove a model from cache.
        """

        cache = self.load()

        original_count = len(cache.models)

        cache.models = [
            model
            for model in cache.models
            if model.name.lower() != name.lower()
        ]

        if len(cache.models) == original_count:
            self.log.info(
                f"Cache entry not found: {name}"
            )
            return False

        self.save(cache)

        self.log.info(
            f"Removed cache entry: {name}"
        )

        return True

cache_manager = CacheManager()