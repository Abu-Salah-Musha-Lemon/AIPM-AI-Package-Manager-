from __future__ import annotations

import typer

from aipm.download import download_manager
from aipm.registry import registry_manager
from aipm.utils.console import console


def run(name: str) -> None:
    """
    Install model from registry.
    """

    model = registry_manager.get(name)

    if model is None:
        console.print(f"[red]Model '{name}' not found.[/red]")
        raise typer.Exit(code=1)

    console.print(f"[cyan]Installing {model.name}[/cyan]")

    path = download_manager.download(
        model.name,
        model.url,
        model.sha256,
    )

    console.print("[green]Installed successfully[/green]")
    console.print(path)