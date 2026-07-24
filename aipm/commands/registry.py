"""
Registry CLI commands.
"""

from __future__ import annotations

import typer
from rich.table import Table

from aipm.registry import registry_manager
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

    models = registry_manager.all_models()

    table = Table(
        title="Registry Models"
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

    if not models:

        console.print(
            "Registry is empty."
        )

        return

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

    model = registry_manager.get(
        name
    )

    if model is None:

        console.print(
            f"Model not found: {name}"
        )

        raise typer.Exit()

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

    table.add_row(
        "Name",
        model.name,
    )

    table.add_row(
        "Version",
        model.version,
    )

    table.add_row(
        "Architecture",
        model.architecture,
    )

    table.add_row(
        "Type",
        model.type,
    )

    table.add_row(
        "Framework",
        model.framework,
    )

    table.add_row(
        "Format",
        model.format,
    )

    table.add_row(
        "Size",
        model.size,
    )

    table.add_row(
        "Description",
        model.description,
    )

    table.add_row(
        "URL",
        model.url,
    )

    console.print(table)


@app.command()
def search(
    keyword: str,
) -> None:
    """
    Search registry.
    """

    keyword = keyword.lower()

    models = [

        model

        for model in registry_manager.all_models()

        if (
            keyword in model.name.lower()
            or keyword in model.description.lower()
            or keyword in model.architecture.lower()
        )
    ]

    if not models:

        console.print(
            "No matching models found."
        )

        return

    table = Table(
        title=f"Search: {keyword}"
    )

    table.add_column(
        "Name",
        style="cyan",
    )

    table.add_column(
        "Architecture",
        style="green",
    )

    table.add_column(
        "Type",
        style="yellow",
    )

    for model in models:

        table.add_row(
            model.name,
            model.architecture,
            model.type,
        )

    console.print(table)