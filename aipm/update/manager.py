"""
Update manager for AIPM.
"""

from __future__ import annotations

from aipm.logger import get_logger

from aipm.registry import registry_manager
from aipm.models import model_manager
from aipm.download import download_manager
from aipm.verify import verify_manager
from aipm.utils.version import (
    compare_versions,
)

class UpdateManager:
    """
    Update installed AI models.
    """

    def __init__(self) -> None:

        self.log = get_logger(
            __name__
        )

    def update(
        self,
        name: str,
    ) -> bool:
        """
        Update an installed model.
        """

        #
        # Lookup registry
        #

        registry_model = registry_manager.get(
            name
        )

        if registry_model is None:

            self.log.error(
                "Registry entry not found."
            )

            return False

        #
        # Check installation
        #

        if not model_manager.exists(
            name
        ):

            self.log.error(
                "Model is not installed."
            )

            return False

        #
        # Installed metadata
        #

        installed = model_manager.get_metadata(
            name
        )

        #
        # Compare version
        #

        installed_version = installed.version

        latest_version = (
            registry_model.version
        )


        result = compare_versions(
            installed_version,
            latest_version,
        )

        if result == 0:

            self.log.info(
                f"Updating {installed_version} -> {latest_version}"
            )

            return True

        if result > 0:

            self.log.warning(
                "Installed version is newer than registry."
            )

            return True


        #
        # Download latest
        #

        self.log.info(
            f"Updating {installed_version} -> {latest_version}"
        )

        download_manager.download(
            name=name,
            url=registry_model.url,
            sha256=registry_model.sha256,
        )

        #
        # Verify
        #

        return verify_manager.verify(
            name
        )


update_manager = UpdateManager()