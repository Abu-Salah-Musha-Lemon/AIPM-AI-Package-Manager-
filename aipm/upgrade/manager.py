"""
Upgrade manager for AIPM.
"""

from __future__ import annotations

from aipm.logger import get_logger

from aipm.models import model_manager
from aipm.update import update_manager


class UpgradeManager:
    """
    Upgrade all installed AI models.
    """

    def __init__(self) -> None:

        self.log = get_logger(
            __name__
        )

    def upgrade(
        self,
    ) -> dict[str, int]:
        """
        Upgrade all installed models.

        Returns:

            {
                "updated": int,
                "skipped": int,
                "failed": int,
            }
        """

        stats = {
            "updated": 0,
            "skipped": 0,
            "failed": 0,
        }

        models = model_manager.list_models()

        if not models:

            self.log.info(
                "No installed models found."
            )

            return stats

        for name in models:

            self.log.info(
                f"Checking {name}"
            )

            try:

                result = update_manager.update(
                    name
                )

                if result:

                    stats["updated"] += 1

                else:

                    stats["failed"] += 1

            except Exception as error:

                self.log.error(
                    f"{name}: {error}"
                )

                stats["failed"] += 1

        return stats


upgrade_manager = UpgradeManager()