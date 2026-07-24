"""
Remove CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from aipm.remove import remove_manager
from aipm.utils.console import console


app = typer.Typer(
    name="remove",
    help="Remove installed AI models.",
)


@app.command()
def model(
    name: str,
):
    """
    Remove an installed model.
    """

    console.print(
        f"[bold red]Removing model:[/bold red] {name}"
    )

    ok = remove_manager.remove(
        name
    )

    if ok:

        console.print(
            "[bold green]✓ Model removed successfully[/bold green]"
        )

    else:

        console.print(
            "[bold red]Model not found.[/bold red]"
        )

        raise typer.Exit(1)