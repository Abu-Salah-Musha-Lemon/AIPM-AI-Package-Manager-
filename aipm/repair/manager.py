"""
Repair manager for AIPM.
"""

from __future__ import annotations

from aipm.download import download_manager
from aipm.logger import get_logger
from aipm.registry import registry_manager
from aipm.remove import remove_manager
from aipm.repair.models import RepairResult
from aipm.verify import verify_manager
from datetime import datetime

from aipm.history import history_manager
from aipm.history.models import (
    HistoryEntry,
    HistoryOperation,
    HistoryStatus,
)

class RepairManager:
    """
    Repair installed AI models.
    """

    def __init__(self) -> None:

        self.log = get_logger(__name__)
    started = datetime.now()
    def repair(
        self,
        name: str,
        progress: bool = False,
    ) -> RepairResult:
        """
        Repair an installed model.
        """

        #
        # Lookup registry
        #

        try:

            model = registry_manager.require(
                name
            )

        except ValueError as error:

            return RepairResult(

                success=False,

                message=str(error),

            )

        if progress:

            self.log.info(
                "Checking registry..."
            )

        #
        # Verify installation
        #

        if progress:

            self.log.info(
                "Verifying installation..."
            )

        verify_result = (
            verify_manager.verify(
                name
            )
        )

        #
        # Already healthy
        #

        if (

            verify_result.exists

            and verify_result.checksum_valid

            and verify_result.metadata_valid

        ):

            self.log.info(
                "Model is healthy."
            )

            return RepairResult(

                success=True,

                repaired=False,

                downloaded=False,

                verified=True,

                message="Model is already healthy.",

            )

        #
        # Remove corrupted files
        #

        self.log.warning(
            "Removing corrupted model..."
        )

        remove_result = (
            remove_manager.remove(
                name
            )
        )

        if not remove_result.success:

            return RepairResult(

                success=False,

                repaired=False,

                downloaded=False,

                verified=False,

                message=remove_result.message,

            )

        if progress:

            self.log.info(
                "Downloading latest model..."
            )
                #
        # Download latest model
        #

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

            return RepairResult(

                success=False,

                repaired=True,

                downloaded=False,

                verified=False,

                message=str(error),

            )

        #
        # Final verification
        #

        if progress:
            
            history_manager.add(

                HistoryEntry(

                    operation=HistoryOperation.REPAIR,

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
            self.log.info(
                "Running final verification..."
            )

        verify_result = (
            verify_manager.verify(
                name
            )
        )

        if (

            verify_result.exists

            and verify_result.checksum_valid

            and verify_result.metadata_valid

        ):

            self.log.info(
                "Repair completed."
            )
            
            history_manager.add(

                HistoryEntry(

                    operation=HistoryOperation.REPAIR,

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

            return RepairResult(

                success=True,

                repaired=True,

                downloaded=True,

                verified=True,

                message="Repair completed successfully.",

            )

        self.log.error(
            "Repair failed."
        )

        return RepairResult(

            success=False,

            repaired=True,

            downloaded=True,

            verified=False,

            message=verify_result.message,

        )


repair_manager = RepairManager()