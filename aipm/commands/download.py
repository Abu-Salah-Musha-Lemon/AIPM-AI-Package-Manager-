"""
Download CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from aipm.download import download_manager
from aipm.utils.console import console


app = typer.Typer(
    name="download",
    help="Download AI models.",
)


@app.command()
def model(
    name: str,
    url: str = typer.Option(
        ...,
        "--url",
        help="Download URL",
    ),
):
    """
    Download AI model.
    """

    console.print(
        f"[bold cyan]Downloading model:[/bold cyan] {name}"
    )

    path = download_manager.download(
        name=name,
        url=url,
    )

    console.print()

    console.print(
        "[bold green]✓ Model is ready[/bold green]"
    )

    console.print(
        f"[cyan]Location:[/cyan] {path}"
    )