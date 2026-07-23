"""
Model CLI commands for AIPM.
"""

from __future__ import annotations

import typer

from rich.table import Table

from aipm.models import model_manager
from aipm.utils.console import console


app = typer.Typer(
    name="models",
    help="Manage AI models.",
)



@app.command("list")
def list_models():
    """
    List installed models.
    """

    model_manager.initialize()

    models = model_manager.list_models()


    table = Table(
        title="Installed Models"
    )

    table.add_column(
        "Name",
        style="cyan"
    )

    table.add_column(
        "Format",
        style="green"
    )

    table.add_column(
        "Size",
        style="yellow"
    )


    if not models:

        console.print(
            "No models installed."
        )

        return



    for model in models:

        info = (
            model_manager
            .get_metadata(model)
        )

        table.add_row(
            info.name,
            info.format,
            info.size,
        )


    console.print(table)



@app.command()
def info(
    name: str,
):
    """
    Show model information.
    """

    if not model_manager.exists(name):

        console.print(
            f"Model not found: {name}"
        )

        raise typer.Exit()



    info = (
        model_manager
        .get_metadata(name)
    )


    table = Table(
        title=f"Model: {name}"
    )


    table.add_column(
        "Property",
        style="cyan"
    )

    table.add_column(
        "Value",
        style="green"
    )


    table.add_row(
        "Name",
        info.name
    )

    table.add_row(
        "Format",
        info.format
    )

    table.add_row(
        "Size",
        info.size
    )

    table.add_row(
        "Path",
        str(info.path)
    )


    console.print(table)



@app.command()
def scan():
    """
    Scan model directory.
    """

    model_manager.initialize()

    models = (
        model_manager
        .list_models()
    )


    console.print(
        f"Found {len(models)} model(s)"
    )