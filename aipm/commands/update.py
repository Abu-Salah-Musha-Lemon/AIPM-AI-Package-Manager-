"""
Update CLI commands.
"""

from __future__ import annotations

import typer

from aipm.update import update_manager
from aipm.utils.console import console


app = typer.Typer(
    name="update",
    help="Update a single installed model.",
)


@app.command()
def model(
    name: str,
):
    """
    Update one model.
    """

    result = update_manager.update(name)

    console.print(result.message)