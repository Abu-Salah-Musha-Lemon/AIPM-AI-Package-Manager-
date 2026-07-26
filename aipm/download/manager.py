"""
Download manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.cache import cache_manager
from aipm.cache.models import CacheEntry
from aipm.download.hash import calculate_sha256
from aipm.download.models import (
    DownloadResult,
    DownloadStatus,
    DownloadTask,
)
from aipm.download.queue import download_queue
from aipm.logger import get_logger
from aipm.storage import storage_manager


class DownloadManager:
    """
    Manage AI model downloads.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

        models = storage_manager.get_path(
            "models"
        )

        if models is None:

            raise RuntimeError(
                "Models storage is not configured."
            )

        self.models = models

        self.log.info(
            "Download manager initialized."
        )

    def download(
        self,
        name: str,
        url: str,
        sha256: str = "",
    ) -> Path:
        """
        Download a single model.
        """

        #
        # Check cache
        #

        cached = cache_manager.get(
            name
        )

        if (
            cached
            and Path(
                cached.path
            ).exists()
        ):

            self.log.info(
                "Using cached model."
            )

            return Path(
                cached.path
            )

        #
        # Create model directory
        #

        model_dir = (
            self.models / name
        )

        model_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # Destination
        #

        target = (
            model_dir
            / "model.bin"
        )

        #
        # Create download task
        #

        task = DownloadTask(
            name=name,
            url=url,
            destination=target,
            sha256=sha256,
            resume=True,
        )

        #
        # Execute download queue
        #

        results = download_queue.run(
            [task]
        )

        if not results:

            raise RuntimeError(
                "Download queue returned no result."
            )

        result = results[0]

        if (
            result.status
            != DownloadStatus.SUCCESS
        ):

            raise RuntimeError(
                result.message
            )

        if result.file is None:

            raise RuntimeError(
                "Download returned no file."
            )

        target = result.file

        self.log.info(
            "Download completed."
        )

        #
        # Verify checksum
        #

        if sha256:

            self.log.info(
                "Verifying SHA256..."
            )

            if not self.verify(
                target,
                sha256,
            ):

                target.unlink(
                    missing_ok=True,
                )

                raise ValueError(
                    "SHA256 verification failed."
                )

        #
        # Save cache entry
        #

        cache_manager.add(

            CacheEntry(

                name=name,

                sha256=calculate_sha256(
                    target
                ),

                size=target.stat().st_size,

                path=str(
                    target
                ),

            )

        )

        self.log.info(
            f"Cached model: {name}"
        )

        return target

    def download_many(
        self,
        tasks: list[DownloadTask],
    ) -> list[DownloadResult]:
        """
        Download multiple models.
        """

        return download_queue.run(
            tasks
        )

    def verify(
        self,
        file: Path,
        expected: str,
    ) -> bool:
        """
        Verify SHA256 checksum.
        """

        if not expected:

            return True

        actual = calculate_sha256(
            file
        )

        return (
            actual.lower()
            == expected.lower()
        )


download_manager = DownloadManager()