"""
SHA256 utilities.
"""

from __future__ import annotations

import hashlib

from pathlib import Path


def calculate_sha256(
    path: Path,
) -> str:

    sha = hashlib.sha256()

    with path.open(
        "rb",
    ) as file:

        while True:

            chunk = file.read(
                1024 * 1024
            )

            if not chunk:
                break

            sha.update(chunk)

    return sha.hexdigest()