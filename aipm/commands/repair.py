"""
Repair CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from aipm.repair import repair_manager
from aipm.utils.console import console


app = typer.Typer(
    name="repair",
    help="Repair installed AI models.",
)


@app.command()
def model(
    name: str,
):
    """
    Repair an installed AI model.
    """

    console.print(
        f"[bold cyan]Repairing model:[/bold cyan] {name}"
    )

    success = repair_manager.repair(
        name=name,
        progress=True,
    )

    if success:

        console.print(
            "[bold green]✓ Repair completed successfully[/bold green]"
        )

    else:

        console.print(
            "[bold red]✗ Repair failed[/bold red]"
        )

        raise typer.Exit(1)