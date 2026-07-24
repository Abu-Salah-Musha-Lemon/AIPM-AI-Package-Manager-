"""
Update manager for AIPM.
"""

from __future__ import annotations

from aipm.logger import get_logger

from aipm.registry import registry_manager
from aipm.models import model_manager
from aipm.download import download_manager
from aipm.verify import verify_manager

from aipm.utils.version import compare_versions

from aipm.update.models import (
    UpdateResult,
    UpdateStatus,
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
    ) -> UpdateResult:
        """
        Update an installed AI model.
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

            return UpdateResult(
                status=UpdateStatus.FAILED,
                message="Registry entry not found.",
            )

        #
        # Check installation
        #

        if not model_manager.exists(
            name
        ):

            self.log.error(
                "Model is not installed."
            )

            return UpdateResult(
                status=UpdateStatus.FAILED,
                message="Model is not installed.",
            )

        #
        # Installed metadata
        #

        installed = model_manager.get_metadata(
            name
        )

        installed_version = installed.version

        latest_version = (
            registry_model.version
        )

        #
        # Compare versions
        #

        comparison = compare_versions(
            installed_version,
            latest_version,
        )

        #
        # Already latest
        #

        if comparison == 0:

            self.log.info(
                "Already up-to-date."
            )

            return UpdateResult(
                status=UpdateStatus.SKIPPED,
                old_version=installed_version,
                new_version=latest_version,
                message="Already up-to-date.",
            )

        #
        # Installed newer than registry
        #

        if comparison > 0:

            self.log.warning(
                "Installed version is newer than registry."
            )

            return UpdateResult(
                status=UpdateStatus.SKIPPED,
                old_version=installed_version,
                new_version=latest_version,
                message="Installed version is newer.",
            )

        #
        # Update required
        #

        self.log.info(
            f"Updating {installed_version} -> {latest_version}"
        )

        try:

            download_manager.download(
                name=name,
                url=registry_model.url,
                sha256=registry_model.sha256,
            )

        except Exception as error:

            self.log.error(
                str(error)
            )

            return UpdateResult(
                status=UpdateStatus.FAILED,
                old_version=installed_version,
                new_version=latest_version,
                message=str(error),
            )

        #
        # Verify installation
        #

        verified = verify_manager.verify(
            name
        )

        if verified:

            self.log.info(
                "Update completed successfully."
            )

            return UpdateResult(
                status=UpdateStatus.UPDATED,
                old_version=installed_version,
                new_version=latest_version,
                message="Updated successfully.",
            )

        self.log.error(
            "Verification failed."
        )

        return UpdateResult(
            status=UpdateStatus.FAILED,
            old_version=installed_version,
            new_version=latest_version,
            message="Verification failed.",
        )


update_manager = UpdateManager()