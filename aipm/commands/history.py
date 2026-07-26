"""
History CLI commands for AIPM.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.table import Table

from aipm.history import history_manager
from aipm.history.models import (
    HistoryOperation,
    HistoryQuery,
    HistoryStatus,
)
from aipm.utils.console import console

app = typer.Typer(
    name="history",
    help="View AIPM operation history.",
)


def render_table(entries) -> None:
    """
    Render history table.
    """

    if not entries:

        console.print(
            "[yellow]History is empty.[/yellow]"
        )

        return

    table = Table(
        title="Operation History"
    )

    table.add_column(
        "Time",
        style="cyan",
    )

    table.add_column(
        "Operation",
        style="green",
    )

    table.add_column(
        "Model",
        style="yellow",
    )

    table.add_column(
        "Status",
        style="magenta",
    )

    table.add_column(
        "Duration",
        justify="right",
    )

    for item in entries:

        table.add_row(

            item.started.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            item.operation.value,

            item.model,

            item.status.value,

            f"{item.duration:.2f}s",

        )

    console.print(table)


@app.command("list")
def list_history() -> None:
    """
    List all history.
    """

    render_table(
        history_manager.list()
    )


@app.command("last")
def last() -> None:
    """
    Show last operation.
    """

    item = history_manager.last()

    if item is None:

        console.print(
            "[yellow]History is empty.[/yellow]"
        )

        return

    table = Table(
        title="Last Operation"
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
        "ID",
        item.id,
    )

    table.add_row(
        "Operation",
        item.operation.value,
    )

    table.add_row(
        "Model",
        item.model,
    )

    table.add_row(
        "Version",
        item.version,
    )

    table.add_row(
        "Status",
        item.status.value,
    )

    table.add_row(
        "Duration",
        f"{item.duration:.2f}s",
    )

    table.add_row(
        "Message",
        item.message,
    )

    console.print(table)


@app.command("stats")
def stats() -> None:
    """
    Show statistics.
    """

    stats = history_manager.statistics()

    table = Table(
        title="History Statistics"
    )

    table.add_column(
        "Metric",
        style="cyan",
    )

    table.add_column(
        "Value",
        style="green",
    )

    table.add_row(
        "Total",
        str(stats["total"]),
    )

    table.add_row(
        "Success",
        str(stats["success"]),
    )

    table.add_row(
        "Failed",
        str(stats["failed"]),
    )

    table.add_row(
        "Cancelled",
        str(stats["cancelled"]),
    )

    console.print(table)


@app.command("search")
def search(
    operation: str = typer.Option(
        "",
        "--operation",
    ),
    status: str = typer.Option(
        "",
        "--status",
    ),
    limit: int = typer.Option(
        20,
        "--limit",
    ),
) -> None:
    """
    Search history.
    """

    query = HistoryQuery(

        operation=(
            HistoryOperation(
                operation
            )
            if operation
            else None
        ),

        status=(
            HistoryStatus(
                status
            )
            if status
            else None
        ),

        limit=limit,

    )

    render_table(
        history_manager.search(
            query
        )
    )


@app.command("export")
def export(
    path: str,
) -> None:
    """
    Export history to JSON.
    """

    history_manager.export_json(
        Path(path)
    )

    console.print(
        "[green]History exported successfully.[/green]"
    )


@app.command("clear")
def clear() -> None:
    """
    Clear history.
    """

    history_manager.clear()

    console.print(
        "[green]History cleared.[/green]"
    )