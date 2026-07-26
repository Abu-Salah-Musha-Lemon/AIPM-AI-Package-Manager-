"""
Model removal manager for AIPM.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from aipm.cache import cache_manager
from aipm.config import load_config
from aipm.logger import get_logger

from .models import RemoveResult


class RemoveManager:
    """
    Remove installed AI models.
    """

    def __init__(self) -> None:

        cfg = load_config()

        self.log = get_logger(__name__)

        self.models = cfg.storage.models

    def remove(
        self,
        name: str,
    ) -> RemoveResult:
        """
        Remove installed model.
        """

        model_path = self.models / name

        if not model_path.exists():

            return RemoveResult(
                success=False,
                message="Model is not installed.",
            )

        removed_files = 0
        removed_bytes = 0

        if model_path.is_dir():

            for file in model_path.rglob("*"):

                if file.is_file():

                    removed_files += 1
                    removed_bytes += file.stat().st_size

            shutil.rmtree(model_path)

        else:

            removed_files = 1
            removed_bytes = model_path.stat().st_size

            model_path.unlink()

        cache_manager.remove(name)

        self.log.info(
            f"Removed model: {name}"
        )

        return RemoveResult(
            success=True,
            removed_files=removed_files,
            removed_bytes=removed_bytes,
            message="Model removed successfully.",
        )


remove_manager = RemoveManager()