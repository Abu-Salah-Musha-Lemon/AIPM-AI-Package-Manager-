"""
Upgrade CLI commands.
"""

from __future__ import annotations

import typer

from aipm.upgrade import upgrade_manager
from aipm.utils.console import console

app = typer.Typer(
    name="upgrade",
    help="Upgrade installed AI models.",
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
) -> None:
    """
    Upgrade all installed models.
    """

    if ctx.invoked_subcommand:
        return

    console.print(
        "[bold cyan]Checking for model updates...[/bold cyan]"
    )

    result = upgrade_manager.upgrade()

    if not result.success:

        console.print(
            f"\n[bold red]{result.message}[/bold red]"
        )

        raise typer.Exit(1)

    if result.upgraded:

        console.print(
            "\n[bold green]✓ Upgrade completed successfully[/bold green]"
        )

    else:

        console.print(
            "\n[yellow]Nothing to upgrade.[/yellow]"
        )

    console.print(
        f"Status      : {'Updated' if result.upgraded else 'No Updates'}"
    )

    console.print(
        f"Downloaded  : {'Yes' if result.downloaded else 'No'}"
    )

    console.print(
        f"Verified    : {'Yes' if result.verified else 'No'}"
    )

    console.print(
        f"Message     : {result.message}"
    )