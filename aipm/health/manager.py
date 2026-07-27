"""
Health manager for AIPM.
"""

from __future__ import annotations

from aipm.logger import get_logger

from .checks import (
    check_cache,
    check_config,
    check_history,
    check_network,
    check_python,
    check_registry,
    check_storage,
)
from .models import (
    HealthCheck,
    HealthReport,
    HealthStatus,
)


class HealthManager:
    """
    Execute health checks.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

    def run(
        self,
    ) -> HealthReport:
        """
        Execute all health checks.
        """

        self.log.info(
            "Running health checks."
        )

        checks: list[
            HealthCheck
        ] = [

            check_config(),

            check_python(),

            check_storage(),

            check_registry(),

            check_cache(),

            check_history(),

            check_network(),

        ]

        overall = (
            self._overall_status(
                checks
            )
        )

        self.log.info(
            "Health checks completed."
        )

        return HealthReport(

            status=overall,

            checks=checks,

        )

    def _overall_status(
        self,
        checks: list[
            HealthCheck
        ],
    ) -> HealthStatus:
        """
        Determine overall health status.
        """

        if any(

            item.status
            == HealthStatus.FAILED

            for item in checks

        ):

            return (
                HealthStatus.FAILED
            )

        if any(

            item.status
            == HealthStatus.WARNING

            for item in checks

        ):

            return (
                HealthStatus.WARNING
            )

        return (
            HealthStatus.SUCCESS
        )


health_manager = HealthManager()