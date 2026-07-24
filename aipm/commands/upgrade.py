"""
Upgrade CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from rich.table import Table

from aipm.upgrade import upgrade_manager
from aipm.utils.console import console


app = typer.Typer(
    name="upgrade",
    help="Upgrade installed AI models.",
)


@app.command()
def all():
    """
    Upgrade all installed AI models.
    """

    console.print(
        "[bold cyan]Checking installed models...[/bold cyan]"
    )

    stats = upgrade_manager.upgrade()

    table = Table(
        title="Upgrade Summary"
    )

    table.add_column(
        "Status",
        style="cyan",
    )

    table.add_column(
        "Count",
        justify="right",
    )

    table.add_row(
        "Updated",
        str(stats["updated"]),
    )

    table.add_row(
        "Skipped",
        str(stats["skipped"]),
    )

    table.add_row(
        "Failed",
        str(stats["failed"]),
    )

    console.print(table)