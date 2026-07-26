"""
Verify CLI commands for AIPM.
"""

from __future__ import annotations

import typer
from rich.table import Table

from aipm.registry import registry_manager
from aipm.utils.console import console
from aipm.verify import verify_manager

app = typer.Typer(
    name="verify",
    help="Verify installed AI models.",
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    name: str = typer.Argument(
        ...,
        help="Model name",
    ),
) -> None:
    """
    Verify an installed model.
    """

    if ctx.invoked_subcommand:
        return

    #
    # Check registry first
    #

    try:
        registry_manager.require(name)

    except ValueError as error:

        console.print(
            f"[bold red]Error:[/bold red] {error}"
        )

        raise typer.Exit(1)

    console.print(
        f"[bold cyan]Verifying:[/bold cyan] {name}"
    )

    #
    # Verify installed files
    #

    try:

        result = verify_manager.verify(
            name
        )

    except Exception as error:

        console.print(
            f"[bold red]Error:[/bold red] {error}"
        )

        raise typer.Exit(1)

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
        "✔ Yes"
        if result.exists
        else "✘ No",
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

    #
    # Final status
    #

    if (
        result.exists
        and result.checksum_valid
        and result.metadata_valid
    ):

        console.print(
            "\n[bold green]✓ Verification successful[/bold green]"
        )

        raise typer.Exit(0)

    console.print(
        f"\n[bold red]{result.message}[/bold red]"
    )

    raise typer.Exit(1)