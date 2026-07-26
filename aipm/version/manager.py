"""
Version manager for AIPM.
"""

from __future__ import annotations

import platform

from aipm import (
    APP_NAME,
    __version__,
)
from aipm.logger import get_logger

from aipm.version.models import (
    VersionResult,
    VersionStatus,
)


class VersionManager:
    """
    Version information manager.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

    def get_version(
        self,
    ) -> VersionResult:
        """
        Get application version information.
        """

        self.log.info(
            "Collecting version information."
        )

        try:

            return VersionResult(

                status=VersionStatus.SUCCESS,

                application=APP_NAME,

                version=__version__,

                python=platform.python_version(),

                platform=platform.platform(),

                message="Version information loaded.",

            )

        except Exception as error:

            self.log.exception(
                "Failed to load version."
            )

            return VersionResult(

                status=VersionStatus.FAILED,

                message=str(error),

            )


version_manager = VersionManager()