"""
File downloader utilities.
"""

from __future__ import annotations

import time
from pathlib import Path

import requests
from rich.progress import (
    Progress,
    BarColumn,
    DownloadColumn,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

from aipm.config import load_config
from aipm.logger import get_logger

from aipm.download.models import (
    DownloadResult,
    DownloadStatus,
)


class Downloader:
    """
    HTTP file downloader.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.log = get_logger(
            __name__
        )

        self.timeout = (
            cfg.download.timeout
        )

        self.chunk_size = 8192

    def download(
        self,
        url: str,
        destination: Path,
        resume: bool = True,
    ) -> DownloadResult:
        """
        Download a file.
        """

        start = time.time()

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        #
        # Partial download
        #

        partial = destination.with_suffix(
            destination.suffix + ".part"
        )

        downloaded = 0

        headers: dict[str, str] = {}

        #
        # Resume support
        #

        if (
            resume
            and partial.exists()
        ):

            downloaded = partial.stat().st_size

            headers["Range"] = (
                f"bytes={downloaded}-"
            )

        try:

            self.log.info(
                f"Downloading: {url}"
            )

            response = requests.get(
                url,
                stream=True,
                timeout=self.timeout,
                headers=headers,
            )

            #
            # Server doesn't support Range
            #

            if (
                downloaded > 0
                and response.status_code == 200
            ):

                downloaded = 0

                partial.unlink(
                    missing_ok=True,
                )

            response.raise_for_status()

            remaining = int(
                response.headers.get(
                    "content-length",
                    0,
                )
            )

            total = (
                downloaded
                + remaining
            )

            mode = (
                "ab"
                if downloaded
                else "wb"
            )

            with Progress(

                TextColumn(
                    "[bold cyan]{task.description}"
                ),

                BarColumn(),

                DownloadColumn(),

                TransferSpeedColumn(),

                TimeRemainingColumn(),

            ) as progress:

                task = progress.add_task(
                    "Downloading",
                    total=total,
                    completed=downloaded,
                )

                with partial.open(
                    mode,
                ) as file:

                    for chunk in response.iter_content(
                        chunk_size=self.chunk_size,
                    ):

                        if not chunk:
                            continue

                        file.write(
                            chunk
                        )

                        progress.update(
                            task,
                            advance=len(
                                chunk
                            ),
                        )

            #
            # Rename completed file
            #

            partial.replace(
                destination
            )

            elapsed = (
                time.time()
                - start
            )

            self.log.info(
                "Download completed."
            )

            return DownloadResult(

                status=DownloadStatus.SUCCESS,

                file=destination,

                bytes_downloaded=destination.stat().st_size,

                elapsed=elapsed,

                message="Download completed.",

            )

        except requests.exceptions.RequestException as error:

            self.log.error(
                str(error)
            )

            return DownloadResult(

                status=DownloadStatus.FAILED,

                file=destination,

                bytes_downloaded=downloaded,

                elapsed=time.time() - start,

                message=str(error),

            )

        except Exception as error:

            self.log.error(
                str(error)
            )

            return DownloadResult(

                status=DownloadStatus.FAILED,

                file=destination,

                bytes_downloaded=downloaded,

                elapsed=time.time() - start,

                message=str(error),

            )


downloader = Downloader()