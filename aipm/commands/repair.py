"""
Repair CLI commands.
"""

from __future__ import annotations

import typer

from aipm.registry import registry_manager
from aipm.repair import repair_manager
from aipm.utils.console import console

app = typer.Typer(
    name="repair",
    help="Repair installed AI models.",
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
    Repair an installed AI model.
    """

    if ctx.invoked_subcommand:
        return

    #
    # Registry lookup
    #

    try:

        registry_manager.require(name)

    except ValueError as error:

        console.print(
            f"[bold red]Error:[/bold red] {error}"
        )

        raise typer.Exit(1)

    console.print(
        f"[bold cyan]Repairing:[/bold cyan] {name}"
    )

    result = repair_manager.repair(
        name=name,
        progress=True,
    )

    if not result.success:

        console.print()

        console.print(
            f"[bold red]{result.message}[/bold red]"
        )

        raise typer.Exit(1)

    console.print()

    if result.repaired:

        console.print(
            "[bold green]✓ Repair completed successfully[/bold green]"
        )

    else:

        console.print(
            "[bold green]✓ Model is already healthy[/bold green]"
        )

    console.print(
        f"Downloaded : {'Yes' if result.downloaded else 'No'}"
    )

    console.print(
        f"Verified  : {'Yes' if result.verified else 'No'}"
    )

    if result.message:

        console.print(
            f"Message   : {result.message}"
        )