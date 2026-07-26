"""
Model removal manager for AIPM.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from aipm.cache import cache_manager
from aipm.logger import get_logger
from aipm.storage import storage_manager

from .models import RemoveResult


class RemoveManager:
    """
    Remove installed AI models.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

        models = storage_manager.get(
            "models"
        )

        if models is None:

            raise RuntimeError(
                "Models storage is not configured."
            )

        self.models = models

    def remove(
        self,
        name: str,
    ) -> RemoveResult:
        """
        Remove an installed model.
        """

        self.log.info(
            f"Removing model: {name}"
        )

        #
        # Model path
        #

        model_path = (
            self.models / name
        )

        #
        # Check installation
        #

        if not model_path.exists():

            self.log.warning(
                "Model is not installed."
            )

            return RemoveResult(
                success=False,
                message="Model is not installed.",
            )

        removed_files = 0
        removed_bytes = 0

        #
        # Remove directory
        #

        if model_path.is_dir():

            for file in model_path.rglob("*"):

                if file.is_file():

                    removed_files += 1

                    removed_bytes += (
                        file.stat().st_size
                    )

            shutil.rmtree(
                model_path
            )

        #
        # Remove single file
        #

        else:

            removed_files = 1

            removed_bytes = (
                model_path.stat().st_size
            )

            model_path.unlink()

        #
        # Remove cache entry
        #

        self.log.info(
            "Removing cache entry."
        )

        cache_manager.remove(
            name
        )

        self.log.info(
            f"Removed model: {name}"
        )

        self.log.info(
            f"Removed {removed_files} file(s), "
            f"{removed_bytes} bytes."
        )

        return RemoveResult(
            success=True,
            removed_files=removed_files,
            removed_bytes=removed_bytes,
            message="Model removed successfully.",
        )


remove_manager = RemoveManager()