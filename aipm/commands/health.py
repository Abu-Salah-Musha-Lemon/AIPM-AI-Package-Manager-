"""
Health CLI commands for AIPM.
"""

from __future__ import annotations

import json

import typer
from rich.table import Table

from aipm.health import (
    HealthStatus,
    health_manager,
)
from aipm.utils.console import console

app = typer.Typer(
    name="health",
    help="Run AIPM health checks.",
)


@app.callback(
    invoke_without_command=True,
)
def run(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show detailed report.",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Output JSON.",
    ),
) -> None:
    """
    Run health checks.
    """

    if ctx.invoked_subcommand:
        return

    report = health_manager.run()

    #
    # JSON Output
    #

    if as_json:

        console.print(
            json.dumps(
                report.model_dump(
                    mode="json",
                ),
                indent=4,
            )
        )

        return

    #
    # Summary
    #

    if report.status == HealthStatus.SUCCESS:

        console.print(
            "[bold green]✔ System Healthy[/bold green]"
        )

    elif report.status == HealthStatus.WARNING:

        console.print(
            "[bold yellow]⚠ System Healthy with Warnings[/bold yellow]"
        )

    else:

        console.print(
            "[bold red]✘ System Failed[/bold red]"
        )

    #
    # Table
    #

    table = Table(
        title="Health Report"
    )

    table.add_column(
        "Check",
        style="cyan",
    )

    table.add_column(
        "Status",
        style="green",
    )

    if verbose:

        table.add_column(
            "Message",
            style="white",
        )

    for item in report.checks:

        status = item.status.value.upper()

        if verbose:

            table.add_row(
                item.name,
                status,
                item.message,
            )

        else:

            table.add_row(
                item.name,
                status,
            )

    console.print(
        table
    )