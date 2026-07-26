"""
Remove CLI commands.
"""

from __future__ import annotations

import typer

from aipm.remove import remove_manager
from aipm.utils.console import console

app = typer.Typer(
    name="remove",
    help="Remove installed AI models.",
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    name: str = typer.Argument(
        ...,
        help="Model name",
    ),
) -> None:

    if ctx.invoked_subcommand:
        return

    console.print(
        f"[bold red]Removing:[/bold red] {name}"
    )

    result = remove_manager.remove(name)

    if not result.success:

        console.print(
            f"[bold red]{result.message}[/bold red]"
        )

        raise typer.Exit(1)

    console.print(
        "\n[bold green]✓ Model removed successfully[/bold green]"
    )

    console.print(
        f"Files removed : {result.removed_files}"
    )

    console.print(
        f"Bytes removed : {result.removed_bytes:,}"
    )