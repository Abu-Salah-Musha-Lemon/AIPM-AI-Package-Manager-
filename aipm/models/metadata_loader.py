"""
Model metadata YAML loader.
"""

from __future__ import annotations

from pathlib import Path

import yaml


def load_model_metadata(
    path: Path,
) -> dict:
    """
    Load metadata.yaml file.
    """

    metadata_file = (
        path / "metadata.yaml"
    )


    if not metadata_file.exists():
        return {}


    with metadata_file.open(
        "r",
        encoding="utf-8",
    ) as file:

        data = yaml.safe_load(file)


    return data or {}