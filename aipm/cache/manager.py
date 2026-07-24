"""
Cache manager.
"""

from __future__ import annotations

from pathlib import Path

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


cache_manager = CacheManager()