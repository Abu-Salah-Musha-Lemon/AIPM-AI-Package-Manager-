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
) -> None:
    """
    Download a file with progress bar.
    """

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    try:

        response = requests.get(
            url,
            stream=True,
            timeout=30,
        )

        response.raise_for_status()

        total = int(
            response.headers.get(
                "content-length",
                0,
            )
        )

        with Progress(
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
        ) as progress:

            task = progress.add_task(
                "Downloading",
                total=total,
            )

            with destination.open(
                "wb",
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

    except requests.exceptions.RequestException as error:

        raise RuntimeError(
            f"Download failed: {error}"
        ) from error
    """
    Download a file with a Rich progress bar.
    """

    destination.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    response = requests.get(
        url,
        stream=True,
        timeout=30,
    )

    response.raise_for_status()

    total = int(
        response.headers.get(
            "content-length",
            0,
        )
    )

    with Progress(
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
    ) as progress:

        task = progress.add_task(
            "Downloading",
            total=total,
        )

        with destination.open(
            "wb",
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