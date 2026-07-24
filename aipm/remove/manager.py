"""
Model removal manager for AIPM.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from aipm.cache import cache_manager
from aipm.config import load_config
from aipm.logger import get_logger


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
    ) -> bool:
        """
        Remove an installed model.
        """

        model_path = self.models / name

        #
        # Remove model files
        #

        if model_path.exists():

            if model_path.is_dir():

                shutil.rmtree(model_path)

            else:

                model_path.unlink()

        #
        # Remove cache entry
        #

        cache_manager.remove(name)

        self.log.info(
            f"Removed model: {name}"
        )

        return True


remove_manager = RemoveManager()