"""
Verify CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from rich.table import Table

from aipm.utils.console import console
from aipm.verify import verify_manager


app = typer.Typer(
    name="verify",
    help="Verify installed AI models.",
)


@app.command()
def model(
    name: str,
):
    """
    Verify an installed model.
    """

    console.print(
        f"[bold cyan]Verifying model:[/bold cyan] {name}"
    )

    result = verify_manager.verify(
        name
    )

    table = Table(
        title="Verification Result"
    )

    table.add_column(
        "Check",
        style="cyan",
    )

    table.add_column(
        "Status",
        style="green",
    )

    table.add_row(
        "File Exists",
        "✔ Yes" if result.exists else "✘ No",
    )

    table.add_row(
        "SHA256",
        "✔ Valid"
        if result.checksum_valid
        else "✘ Invalid",
    )

    table.add_row(
        "Metadata",
        "✔ Valid"
        if result.metadata_valid
        else "✘ Invalid",
    )

    console.print(table)

    if result.checksum_valid:

        console.print(
            "[bold green]✓ Model is valid[/bold green]"
        )

    else:

        console.print(
            f"[bold red]{result.message}[/bold red]"
        )

        raise typer.Exit(1)