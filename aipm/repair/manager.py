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
        progress: bool = False,
    ) -> bool:
        """
        Repair a model.
        """

        #
        # Lookup registry
        #

        model = registry_manager.get(name)

        if progress:
            self.log.info(
                "Checking registry..."
            )

        model = registry_manager.get(name)

        if model is None:

            self.log.error(
                "Registry entry not found."
            )

            return False

        if progress:
            self.log.info(
                "Registry OK"
            )

        #
        # Verify model
        #

        if progress:
            self.log.info(
                "Verifying installation..."
            )

        healthy = verify_manager.verify(name)

        if healthy:

            self.log.info(
                "Model is healthy."
            )

            return True

        #
        # Remove broken model
        #

        self.log.warning(
            "Removing corrupted model..."
        )

        remove_manager.remove(name)

        #
        # Download again
        #

        self.log.info(
            "Downloading latest  model..."
        )

        download_manager.download(
            name=model.name,
            url=model.url,
            sha256=model.sha256,
        )

        #
        # Final verification
        #

        self.log.info(
            "Running final verification..."
        )

        result = verify_manager.verify(name)

        if result:

            self.log.info(
                "Repair completed."
            )

        else:

            self.log.error(
                "Repair failed."
            )

        return result


repair_manager = RepairManager()