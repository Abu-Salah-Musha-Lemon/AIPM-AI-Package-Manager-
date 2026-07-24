"""
Download manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config import load_config
from aipm.download.downloader import download_file
from aipm.logger import get_logger


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
    ) -> Path:
        """
        Download a model file.
        """

        model_dir = self.models / name

        model_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # TODO:
        # Future commits will detect the filename
        # automatically from the URL or headers.
        #

        target = model_dir / "model.bin"

        self.log.info(
            f"Downloading {name}"
        )

        download_file(
            url=url,
            destination=target,
        )

        self.log.info(
            "Download completed"
        )

        return target


download_manager = DownloadManager()