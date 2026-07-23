from __future__ import annotations

import platform
from rich.table import Table

from aipm.utils.console import console


def run() -> None:
    """Display basic environment information."""

    table = Table(title="AIPM Doctor")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Python", platform.python_version())
    table.add_row("Platform", platform.system())
    table.add_row("Release", platform.release())
    table.add_row("Architecture", platform.machine())

    console.print(table)