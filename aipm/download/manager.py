"""
Download manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.cache import cache_manager
from aipm.cache.models import CacheEntry
from aipm.config import load_config
from aipm.download.downloader import downloader
from aipm.download.hash import calculate_sha256
from aipm.download.models import DownloadStatus
from aipm.logger import get_logger
from aipm.utils.hash import sha256_file


class DownloadManager:
    """
    Manage AI model downloads.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.log = get_logger(__name__)

        self.models = cfg.storage.models

    def download(
        self,
        name: str,
        url: str,
        sha256: str = "",
    ) -> Path:
        """
        Download a model file.
        """

        #
        # Check cache
        #

        cached = cache_manager.get(name)

        if (
            cached
            and Path(cached.path).exists()
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
        # Destination file
        #

        target = (
            model_dir
            / "model.bin"
        )

        self.log.info(
            f"Downloading {name}"
        )

        result = downloader.download(
            url=url,
            destination=target,
            resume=True,
        )

        if (
            result.status
            != DownloadStatus.SUCCESS
        ):

            raise RuntimeError(
                result.message
            )

        self.log.info(
            "Download completed."
        )

        #
        # Verify SHA256
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
        # Save cache
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

        return target

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

        actual = sha256_file(
            file
        )

        return (
            actual.lower()
            == expected.lower()
        )


download_manager = DownloadManager()