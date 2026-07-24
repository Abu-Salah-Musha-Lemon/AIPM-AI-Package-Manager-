"""
Download manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config import load_config
from aipm.download.downloader import download_file
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
            resume=True,
        )

        self.log.info(
            "Download completed"
        )

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

        actual = sha256_file(file)

        return (
            actual.lower()
            == expected.lower()
        )

download_manager = DownloadManager()