"""
Version CLI command for AIPM.
"""

from __future__ import annotations

from rich.table import Table

from aipm.version import (
    version_manager,
    VersionStatus,
)
from aipm.utils.console import console


def run() -> None:
    """
    Display AIPM version information.
    """

    result = version_manager.get_version()

    if result.status != VersionStatus.SUCCESS:

        console.print(
            f"[bold red]Error:[/bold red] {result.message}"
        )

        return

    table = Table(
        title="AIPM Version"
    )

    table.add_column(
        "Property",
        style="cyan",
    )

    table.add_column(
        "Value",
        style="green",
    )

    table.add_row(
        "Application",
        result.application,
    )

    table.add_row(
        "Version",
        result.version,
    )

    table.add_row(
        "Python",
        result.python,
    )

    table.add_row(
        "Platform",
        result.platform,
    )

    console.print(table)