"""
Update manager for AIPM.
"""

from __future__ import annotations

from aipm.download import download_manager
from aipm.logger import get_logger
from aipm.registry import registry_manager
from aipm.remove import remove_manager
from aipm.verify import verify_manager

from aipm.update.models import (
    UpdateResult,
)
from datetime import datetime

from aipm.history import history_manager
from aipm.history.models import (
    HistoryEntry,
    HistoryOperation,
    HistoryStatus,
)

class UpdateManager:
    """
    Update installed AI models.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )
    started = datetime.now()
    def update(
        self,
        name: str,
    ) -> UpdateResult:
        """
        Update one installed model.
        """

        #
        # Registry lookup
        #

        model = registry_manager.get(
            name
        )

        if model is None:

            self.log.error(
                "Registry entry not found."
            )

            return UpdateResult(

                success=False,

                message=(
                    "Registry entry not found."
                ),

            )

        #
        # Verify installation
        #

        verify = verify_manager.verify(
            name
        )

        if not verify.exists:

            self.log.error(
                "Model is not installed."
            )

            history_manager.add(

            HistoryEntry(

                operation=HistoryOperation.UPDATE,

                model=name,

                version="",

                status=HistoryStatus.FAILED,

                started=started,

                finished=datetime.now(),

                duration=(
                    datetime.now() - started
                ).total_seconds(),

                message="SHA256 mismatch.",

            )

        )
            return UpdateResult(

                success=False,

                message="Model is not installed.",

            )

        #
        # Already latest?
        #

        if (
            verify.checksum_valid
            and verify.metadata_valid
        ):

            self.log.info(
                "Already up-to-date."
            )

            return UpdateResult(

                success=True,

                updated=False,

                downloaded=False,

                verified=True,

                message="Already up-to-date.",

            )
        #
        # Remove old installation
        #

        self.log.info(
            "Removing old installation..."
        )

        remove_result = remove_manager.remove(
            name
        )

        if not remove_result.success:

            self.log.error(
                remove_result.message
            )

            return UpdateResult(

                success=False,

                message=remove_result.message,

            )

        #
        # Download latest model
        #

        self.log.info(
            "Downloading latest model..."
        )

        try:

            download_manager.download(

                name=model.name,

                url=model.url,

                sha256=model.sha256,

            )

        except Exception as error:

            self.log.error(
                str(error)
            )

            return UpdateResult(

                success=False,

                downloaded=False,

                message=str(error),

            )
                #
        # Final verification
        #

        self.log.info(
            "Running verification..."
        )

        verify = verify_manager.verify(
            name
        )

        if (
            not verify.exists
            or not verify.checksum_valid
            or not verify.metadata_valid
        ):

            self.log.error(
                verify.message
            )

            return UpdateResult(

                success=False,

                updated=False,

                downloaded=True,

                verified=False,

                message=verify.message,

            )

        #
        # Update completed
        #

        self.log.info(
            "Update completed successfully."
        )
        
        history_manager.add(

            HistoryEntry(

                operation=HistoryOperation.UPDATE,

                model=name,

                version="",

                status=HistoryStatus.SUCCESS,

                started=started,

                finished=datetime.now(),

                duration=(
                    datetime.now() - started
                ).total_seconds(),

                message="Verification successful.",

            )

        )

        return UpdateResult(

            success=True,

            updated=True,

            downloaded=True,

            verified=True,

            message="Update completed successfully.",

        )
    #
# Singleton
#

update_manager = UpdateManager()