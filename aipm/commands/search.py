"""
Global search command.
"""

from __future__ import annotations

from rich.table import Table

from aipm.registry import registry_manager
from aipm.utils.console import console


def run(
    keyword: str,
) -> None:
    """
    Search registry models.
    """

    keyword = keyword.lower()

    models = [
        model
        for model in registry_manager.all_models()
        if (
            keyword in model.name.lower()
            or keyword in model.description.lower()
            or keyword in model.architecture.lower()
            or keyword in model.type.lower()
        )
    ]

    if not models:
        console.print(
            f"No models found matching '{keyword}'."
        )
        return

    table = Table(
        title=f"Search Results ({len(models)})"
    )

    table.add_column("Name", style="cyan")
    table.add_column("Version", style="green")
    table.add_column("Architecture", style="yellow")
    table.add_column("Type", style="magenta")

    for model in models:
        table.add_row(
            model.name,
            model.version,
            model.architecture,
            model.type,
        )

    console.print(table)