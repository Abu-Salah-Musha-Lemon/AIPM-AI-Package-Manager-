"""
Registry CLI commands.
"""

from __future__ import annotations

import typer
from rich.table import Table

from aipm.registry import (
    registry_manager,
    registry_sync,
)
from aipm.utils.console import console

app = typer.Typer(
    name="registry",
    help="Browse AI model registry.",
)


@app.command("list")
def list_models() -> None:
    """
    List registry models.
    """

    models = registry_manager.list()

    if not models:

        console.print(
            "[yellow]Registry is empty.[/yellow]"
        )

        return

    table = Table(
        title=f"Registry Models ({registry_manager.count()})"
    )

    table.add_column(
        "Name",
        style="cyan",
    )

    table.add_column(
        "Version",
        style="green",
    )

    table.add_column(
        "Architecture",
        style="yellow",
    )

    table.add_column(
        "Type",
        style="magenta",
    )

    for model in models:

        table.add_row(
            model.name,
            model.version,
            model.architecture,
            model.type,
        )

    console.print(table)


@app.command()
def info(
    name: str,
) -> None:
    """
    Show registry model details.
    """

    model = registry_manager.get(name)

    if model is None:

        console.print(
            f"[bold red]Model not found:[/bold red] {name}"
        )

        raise typer.Exit(1)

    table = Table(
        title=f"Registry Model: {model.name}"
    )

    table.add_column(
        "Property",
        style="cyan",
    )

    table.add_column(
        "Value",
        style="green",
    )

    table.add_row("Name", model.name)
    table.add_row("Version", model.version)
    table.add_row("Architecture", model.architecture)
    table.add_row("Type", model.type)
    table.add_row("Framework", model.framework)
    table.add_row("Format", model.format)
    table.add_row("Size", model.size)
    table.add_row("Description", model.description)
    table.add_row("URL", model.url)

    console.print(table)


@app.command()
def search(
    keyword: str,
) -> None:
    """
    Search registry.
    """

    models = registry_manager.search(
        keyword
    )

    if not models:

        console.print(
            "[yellow]No matching models found.[/yellow]"
        )

        return

    table = Table(
        title=f"Search Results ({len(models)})"
    )

    table.add_column(
        "Name",
        style="cyan",
    )

    table.add_column(
        "Version",
        style="green",
    )

    table.add_column(
        "Architecture",
        style="yellow",
    )

    table.add_column(
        "Type",
        style="magenta",
    )

    for model in models:

        table.add_row(
            model.name,
            model.version,
            model.architecture,
            model.type,
        )

    console.print(table)


@app.command()
def sync() -> None:
    """
    Synchronize registry.
    """

    try:

        size = registry_sync.sync()

    except Exception as error:

        console.print(
            f"[bold red]Registry sync failed:[/bold red] {error}"
        )

        raise typer.Exit(1)

    #
    # Reload registry cache
    #

    registry_manager.reload()

    console.print(
        "[bold green]✓ Registry synchronized successfully[/bold green]"
    )

    console.print(
        f"Downloaded {size:,} bytes."
    )