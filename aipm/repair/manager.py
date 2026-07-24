"""
Repair manager for AIPM.
"""

from __future__ import annotations

from aipm.logger import get_logger

from aipm.download import download_manager
from aipm.registry import registry_manager
from aipm.remove import remove_manager
from aipm.verify import verify_manager


class RepairManager:
    """
    Repair installed AI models.
    """

    def __init__(self) -> None:

        self.log = get_logger(__name__)

    def repair(
        self,
        name: str,
    ) -> bool:
        """
        Repair a model.
        """

        #
        # Lookup registry
        #

        model = registry_manager.get(name)

        if model is None:

            self.log.error(
                f"Registry entry not found: {name}"
            )

            return False

        #
        # Verify model
        #

        if verify_manager.verify(name):

            self.log.info(
                "Model is healthy."
            )

            return True

        #
        # Remove broken model
        #

        self.log.warning(
            "Removing broken model..."
        )

        remove_manager.remove(name)

        #
        # Download again
        #

        self.log.info(
            "Downloading model..."
        )

        download_manager.download(
            name=model.name,
            url=model.url,
            sha256=model.sha256,
        )

        #
        # Final verification
        #

        return verify_manager.verify(name)


repair_manager = RepairManager()