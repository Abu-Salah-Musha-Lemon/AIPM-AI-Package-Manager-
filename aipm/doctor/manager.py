"""
Doctor manager for AIPM.
"""

from __future__ import annotations

from aipm.config import load_config
from aipm.logger import get_logger
from aipm.storage import storage_manager
from aipm.system.detector import detect_system

from aipm.doctor.models import (
    DoctorResult,
    DoctorStatus,
    StorageStatus,
)


class DoctorManager:
    """
    Perform system diagnostics.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

    def run(
        self,
    ) -> DoctorResult:
        """
        Run doctor diagnostics.
        """

        self.log.info(
            "Doctor started."
        )

        try:

            #
            # Load configuration
            #

            cfg = load_config()

            #
            # Initialize storage
            #

            storage_manager.initialize()

            #
            # Detect system
            #

            system = detect_system()

            #
            # Storage status
            #

            storage = StorageStatus(

                cache=storage_manager.exists(
                    "cache"
                ),

                models=storage_manager.exists(
                    "models"
                ),

                loras=storage_manager.exists(
                    "loras"
                ),

                workflows=storage_manager.exists(
                    "workflows"
                ),

                outputs=storage_manager.exists(
                    "outputs"
                ),

                logs=storage_manager.exists(
                    "logs"
                ),

            )

            self.log.info(
                "Doctor completed successfully."
            )

            return DoctorResult(

                status=DoctorStatus.SUCCESS,

                application=cfg.app.name,

                version=cfg.app.version,

                storage_root=str(
                    cfg.storage.root
                ),

                system=system,

                storage=storage,

                message="System is healthy.",

            )

        except Exception as error:

            self.log.exception(
                "Doctor failed."
            )

            return DoctorResult(

                status=DoctorStatus.FAILED,

                storage=StorageStatus(),

                message=str(error),

            )


doctor_manager = DoctorManager()