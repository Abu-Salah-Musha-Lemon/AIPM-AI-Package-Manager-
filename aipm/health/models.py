"""
Health models for AIPM.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class HealthStatus(
    str,
    Enum,
):
    """
    Health check status.
    """

    SUCCESS = "success"

    WARNING = "warning"

    FAILED = "failed"


class HealthCheck(BaseModel):
    """
    Single health check result.
    """

    name: str

    status: HealthStatus

    message: str = ""

    details: dict[str, str] = Field(
        default_factory=dict,
    )


class HealthReport(BaseModel):
    """
    Complete health report.
    """

    status: HealthStatus

    checks: list[HealthCheck] = Field(
        default_factory=list,
    )

    @property
    def successful(self) -> int:
        """
        Number of successful checks.
        """

        return sum(
            item.status == HealthStatus.SUCCESS
            for item in self.checks
        )

    @property
    def warnings(self) -> int:
        """
        Number of warning checks.
        """

        return sum(
            item.status == HealthStatus.WARNING
            for item in self.checks
        )

    @property
    def failures(self) -> int:
        """
        Number of failed checks.
        """

        return sum(
            item.status == HealthStatus.FAILED
            for item in self.checks
        )

    @property
    def total(self) -> int:
        """
        Total checks.
        """

        return len(
            self.checks
        )