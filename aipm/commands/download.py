"""
Download CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from aipm.download import download_manager
from aipm.registry import registry_manager
from aipm.utils.console import console

app = typer.Typer(
    name="download",
    help="Download AI models.",
)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    name: str = typer.Argument(...),
) -> None:

    if ctx.invoked_subcommand:
        return

    try:
        model = registry_manager.require(name)

    except ValueError as error:
        console.print(
            f"[bold red]Error:[/bold red] {error}"
        )
        raise typer.Exit(code=1)

    console.print(
        f"[bold cyan]Downloading:[/bold cyan] {model.name}"
    )

    path = download_manager.download(
        name=model.name,
        url=model.url,
        sha256=model.sha256,
    )

    console.print(
        "\n[bold green]✓ Download completed[/bold green]"
    )

    console.print(
        f"[cyan]Location:[/cyan] {path}"
    )