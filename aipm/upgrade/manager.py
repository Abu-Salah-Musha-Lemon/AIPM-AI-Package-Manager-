"""
Upgrade manager for AIPM.
"""

from __future__ import annotations

from aipm.logger import get_logger

from aipm.models import model_manager
from aipm.update import update_manager
from aipm.upgrade.models import UpgradeResult


class UpgradeManager:
    """
    Upgrade installed AI models.
    """

    def __init__(self) -> None:

        self.log = get_logger(
            __name__
        )

    def upgrade(
        self,
    ) -> UpgradeResult:
        """
        Upgrade all installed models.
        """

        models = (
            model_manager.list_models()
        )

        #
        # Nothing installed
        #

        if not models:

            self.log.info(
                "No installed models found."
            )

            return UpgradeResult(

                success=True,

                upgraded=False,

                downloaded=False,

                verified=False,

                message="No installed models found.",

            )

        updated = 0

        skipped = 0

        failed = 0

        for name in models:

            self.log.info(
                f"Checking {name}"
            )

            try:

                result = (
                    update_manager.update(
                        name
                    )
                )

                #
                # update() returns bool
                #

                if result:

                    updated += 1

                else:

                    skipped += 1
            except Exception as error:

                self.log.error(
                    f"{name}: {error}"
                )

                failed += 1

        #
        # Final summary
        #

        message = (
            f"Updated={updated}, "
            f"Skipped={skipped}, "
            f"Failed={failed}"
        )

        self.log.info(
            message
        )

        return UpgradeResult(

            success=(failed == 0),

            upgraded=(updated > 0),

            downloaded=(updated > 0),

            verified=(failed == 0),

            message=message,

        )


upgrade_manager = UpgradeManager()