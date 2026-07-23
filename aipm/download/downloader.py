"""
File downloader utilities.
"""

from __future__ import annotations

from pathlib import Path

import requests


def download_file(
    url: str,
    destination: Path,
) -> None:
    """
    Download a file.
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


    with destination.open(
        "wb"
    ) as file:

        for chunk in response.iter_content(
            chunk_size=8192
        ):

            if chunk:
                file.write(chunk)