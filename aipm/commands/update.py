"""
Update CLI commands.
"""

from __future__ import annotations

import typer

from aipm.registry import registry_manager
from aipm.update import update_manager
from aipm.utils.console import console

app = typer.Typer(
    name="update",
    help="Update installed AI models.",
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
    Update an installed model.
    """

    if ctx.invoked_subcommand:
        return

    #
    # Registry lookup
    #

    try:

        registry_manager.require(
            name
        )

    except ValueError as error:

        console.print(
            f"[bold red]Error:[/bold red] {error}"
        )

        raise typer.Exit(1)

    console.print(
        f"[bold cyan]Updating:[/bold cyan] {name}"
    )

    result = update_manager.update(
        name
    )

    if not result.success:

        console.print(
            f"\n[bold red]{result.message}[/bold red]"
        )

        raise typer.Exit(1)

    if result.updated:

        console.print(
            "\n[bold green]✓ Update completed successfully[/bold green]"
        )

    else:

        console.print(
            "\n[bold yellow]Already up-to-date[/bold yellow]"
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