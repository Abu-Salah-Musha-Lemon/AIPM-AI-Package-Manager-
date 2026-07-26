"""
History manager for AIPM.
"""

from __future__ import annotations

import json

from datetime import datetime
from pathlib import Path
from uuid import uuid4

from aipm.logger import get_logger

from .models import (
    HistoryDatabase,
    HistoryEntry,
    HistoryOperation,
    HistoryQuery,
    HistoryStatus,
)

from .storage import history_storage


class HistoryManager:
    """
    Manage operation history.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

    def add(
        self,
        operation: HistoryOperation,
        model: str,
        version: str = "",
        status: HistoryStatus = HistoryStatus.SUCCESS,
        duration: float = 0.0,
        size: int = 0,
        message: str = "",
    ) -> HistoryEntry:
        """
        Add history entry.
        """

        database = history_storage.load()

        now = datetime.now()

        entry = HistoryEntry(

            id=str(
                uuid4()
            ),

            operation=operation,

            model=model,

            version=version,

            status=status,

            started=now,

            finished=now,

            duration=duration,

            size=size,

            message=message,

        )

        database.entries.append(
            entry
        )

        history_storage.save(
            database
        )

        self.log.info(
            f"History added: {operation.value} {model}"
        )

        return entry

    def list(
        self,
    ) -> list[HistoryEntry]:
        """
        Return all history.
        """

        return history_storage.load().entries

    def last(
        self,
    ) -> HistoryEntry | None:
        """
        Return last history entry.
        """

        entries = self.list()

        if not entries:

            return None

        return entries[-1]

    def get(
        self,
        entry_id: str,
    ) -> HistoryEntry | None:
        """
        Get history entry by id.
        """

        for item in self.list():

            if item.id == entry_id:

                return item

        return None

    def clear(
        self,
    ) -> None:
        """
        Clear history.
        """

        history_storage.clear()

        self.log.info(
            "History cleared."
        )

    def statistics(
        self,
    ) -> dict[str, int]:
        """
        Return history statistics.
        """

        stats = {

            "total": 0,

            "success": 0,

            "failed": 0,

            "cancelled": 0,

        }

        for item in self.list():

            stats["total"] += 1

            if item.status == HistoryStatus.SUCCESS:

                stats["success"] += 1

            elif item.status == HistoryStatus.FAILED:

                stats["failed"] += 1

            elif item.status == HistoryStatus.CANCELLED:

                stats["cancelled"] += 1

        return stats

    def search(
        self,
        query: HistoryQuery,
    ) -> list[HistoryEntry]:
        """
        Search history.
        """

        entries = history_storage.load().entries

        if query.operation is not None:

            entries = [

                item

                for item in entries

                if item.operation == query.operation

            ]

        if query.status is not None:

            entries = [

                item

                for item in entries

                if item.status == query.status

            ]

        entries.sort(

            key=lambda item: item.started,

            reverse=True,

        )

        if query.limit is not None:

            entries = entries[: query.limit]

        return entries

    def export_json(
        self,
        path: Path,
    ) -> None:
        """
        Export history to JSON.
        """

        database = history_storage.load()

        data = [

            item.model_dump(
                mode="json"
            )

            for item in database.entries

        ]

        path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        path.write_text(

            json.dumps(

                data,

                indent=4,

                ensure_ascii=False,

            ),

            encoding="utf-8",

        )

        self.log.info(
            f"History exported to {path}"
        )


history_manager = HistoryManager()