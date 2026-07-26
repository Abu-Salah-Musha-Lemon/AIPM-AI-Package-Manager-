"""
History storage for AIPM.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from aipm.config import load_config
from aipm.logger import get_logger

from .models import HistoryDatabase


class HistoryStorage:
    """
    Persistent history storage.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.log = get_logger(
            __name__
        )

        self.path = (
            cfg.storage.root
            / "history.yaml"
        )

    def load(
        self,
    ) -> HistoryDatabase:
        """
        Load history database.
        """

        if not self.path.exists():

            return HistoryDatabase()

        try:

            with self.path.open(
                "r",
                encoding="utf-8",
            ) as file:

                data = (
                    yaml.safe_load(file)
                    or {}
                )

            return HistoryDatabase(
                **data
            )

        except Exception as error:

            self.log.error(
                f"Failed to load history: {error}"
            )

            return HistoryDatabase()

    def save(
        self,
        database: HistoryDatabase,
    ) -> None:
        """
        Save history database.
        """

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:

            yaml.safe_dump(

                database.model_dump(
                    mode="json",
                ),

                file,

                sort_keys=False,

                allow_unicode=True,

            )

        self.log.info(
            "History saved."
        )

    def clear(
        self,
    ) -> None:
        """
        Clear history database.
        """

        self.save(
            HistoryDatabase()
        )

        self.log.info(
            "History cleared."
        )


history_storage = HistoryStorage()