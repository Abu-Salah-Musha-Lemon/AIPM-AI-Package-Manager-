"""
Download queue.
"""

from __future__ import annotations

from queue import Queue

from aipm.download.models import DownloadTask


class DownloadQueue:
    """
    Thread-safe download queue.
    """

    def __init__(self) -> None:

        self._queue: Queue[
            DownloadTask
        ] = Queue()

    def add(
        self,
        task: DownloadTask,
    ) -> None:
        """
        Add task.
        """

        self._queue.put(
            task
        )

    def get(
        self,
    ) -> DownloadTask:
        """
        Get next task.
        """

        return self._queue.get()

    def empty(
        self,
    ) -> bool:
        """
        Queue empty?
        """

        return self._queue.empty()

    def size(
        self,
    ) -> int:
        """
        Queue size.
        """

        return self._queue.qsize()


download_queue = DownloadQueue()