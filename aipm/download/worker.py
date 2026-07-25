"""
Download worker.
"""

from __future__ import annotations

from aipm.download.downloader import downloader
from aipm.download.models import (
    DownloadResult,
    DownloadTask,
)


class DownloadWorker:
    """
    Execute download tasks.
    """

    def run(
        self,
        task: DownloadTask,
    ) -> DownloadResult:
        """
        Execute one download task.
        """

        return downloader.download(
            url=task.url,
            destination=task.destination,
            sha256=task.sha256,
            resume=task.resume,
        )


download_worker = DownloadWorker()