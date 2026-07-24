"""
File downloader utilities.
"""

from __future__ import annotations

from pathlib import Path

import requests

from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
)


def download_file(
    url: str,
    destination: Path,
    resume: bool = True,
) -> None:
    """
    Download a file with resume support and Rich progress bar.
    """

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    #
    # Partial download file
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
        print("=" * 60)
        print("URL =", url)
        print("Headers =", headers)
        print("=" * 60)
        response = requests.get(
            url,
            stream=True,
            timeout=30,
            headers=headers,
        )

        #
        # Some servers don't support Range requests.
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

        total = downloaded + remaining

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
                    chunk_size=8192,
                ):

                    if not chunk:
                        continue

                    file.write(chunk)

                    progress.update(
                        task,
                        advance=len(chunk),
                    )

        #
        # Rename completed file
        #

        partial.replace(
            destination
        )

    except requests.exceptions.RequestException as error:

        raise RuntimeError(
            f"Download failed: {error}"
        ) from error