from __future__ import annotations

import platform

from rich.table import Table

from aipm.config import load_config
from aipm.utils.console import console


def run() -> None:
    """Display basic environment information."""

    cfg = load_config()

    table = Table(title="AIPM Doctor")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Application", cfg.app.name)
    table.add_row("Version", cfg.app.version)
    table.add_row("Python", platform.python_version())
    table.add_row("Platform", platform.system())
    table.add_row("Release", platform.release())
    table.add_row("Architecture", platform.machine())
    table.add_row("Storage", str(cfg.storage.root))

    console.print(table)