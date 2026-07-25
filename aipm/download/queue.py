"""
Download task queue.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from aipm.config import load_config
from aipm.download.models import (
    DownloadResult,
    DownloadTask,
)
from aipm.download.worker import download_worker


class DownloadQueue:
    """
    Execute download tasks concurrently.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.workers = cfg.download.workers

    def run(
        self,
        tasks: list[DownloadTask],
    ) -> list[DownloadResult]:
        """
        Execute download tasks.
        """

        if not tasks:
            return []

        results: list[DownloadResult] = []

        with ThreadPoolExecutor(
            max_workers=self.workers,
        ) as executor:

            futures = [

                executor.submit(
                    download_worker.run,
                    task,
                )

                for task in tasks
            ]

            for future in as_completed(
                futures,
            ):

                results.append(
                    future.result()
                )

        return results


download_queue = DownloadQueue()