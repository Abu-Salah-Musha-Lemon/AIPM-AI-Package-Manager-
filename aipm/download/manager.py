"""
Download manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config import load_config
from aipm.logger import get_logger

from aipm.download.downloader import (
    download_file,
)


class DownloadManager:
    """
    Manage AI model downloads.
    """


    def __init__(self):

        cfg = load_config()

        self.log = get_logger(
            __name__,
        )

        self.models = (
            cfg.storage.models
        )


    def download(
        self,
        name: str,
        url: str,
    ) -> Path:
        """
        Download model file.
        """


        model_dir = (
            self.models / name
        )


        model_dir.mkdir(
            parents=True,
            exist_ok=True,
        )


        target = (
            model_dir / "model.bin"
        )


        self.log.info(
            f"Downloading {name}"
        )


        download_file(
            url,
            target,
        )


        self.log.info(
            "Download completed"
        )


        return target