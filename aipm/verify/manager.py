"""
Model verification manager.
"""

from __future__ import annotations

from pathlib import Path

from aipm.cache import cache_manager
from aipm.download.hash import calculate_sha256
from aipm.logger import get_logger
from aipm.verify.models import VerifyResult
from datetime import datetime

from aipm.history import history_manager
from aipm.history.models import (
    HistoryEntry,
    HistoryOperation,
    HistoryStatus,
)

class VerifyManager:
    """
    Verify installed AI models.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )
    started = datetime.now()
    def verify(
        self,
        name: str,
    ) -> VerifyResult:
        """
        Verify an installed model.
        """

        self.log.info(
            f"Verifying model: {name}"
        )

        #
        # Lookup cache
        #

        cached = cache_manager.get(
            name
        )

        if cached is None:

            self.log.warning(
                "Model not found in cache."
            )

            return VerifyResult(
                name=name,
                exists=False,
                checksum_valid=False,
                metadata_valid=False,
                message="Model not found in cache.",
            )

        #
        # Check file
        #

        path = Path(
            cached.path
        )

        if not path.exists():

            self.log.warning(
                "Model file is missing."
            )

            history_manager.add(

                HistoryEntry(

                    operation=HistoryOperation.VERIFY,

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

            return VerifyResult(
                name=name,
                exists=False,
                checksum_valid=False,
                metadata_valid=False,
                message="Model file is missing.",
            )

        #
        # Verify checksum
        #

        checksum_valid = (
            calculate_sha256(
                path
            )
            == cached.sha256
        )

        if checksum_valid:

            self.log.info(
                "Verification successful."
            )

        else:

            self.log.error(
                "SHA256 checksum mismatch."
            )

        #
        # Result
        #
            history_manager.add(

            HistoryEntry(

                operation=HistoryOperation.VERIFY,

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
        return VerifyResult(
            name=name,
            exists=True,
            checksum_valid=checksum_valid,
            metadata_valid=True,
            message=(
                "Verification successful."
                if checksum_valid
                else "SHA256 mismatch."
            ),
        )


verify_manager = VerifyManager()