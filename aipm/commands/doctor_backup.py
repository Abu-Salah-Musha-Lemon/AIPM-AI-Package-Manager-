from __future__ import annotations

import platform

from rich.table import Table

from aipm.config import load_config
from aipm.utils.console import console
from aipm.logger import get_logger
from aipm.system.detector import detect_system

def run() -> None:
    """Display basic environment information."""

    log = get_logger(__name__)

    log.info("Doctor command started")

    cfg = load_config()

    log.info("Configuration loaded")

    system = detect_system()

    log.info("System detection completed")

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

    system_table = Table(title="System Information")

    system_table.add_column(
        "Property",
        style="cyan"
    )

    system_table.add_column(
        "Value",
        style="green"
    )


    system_table.add_row(
        "Operating System",
        system.operating_system
    )

    system_table.add_row(
        "Release",
        system.release
    )

    system_table.add_row(
        "Architecture",
        system.architecture
    )

    system_table.add_row(
        "Python",
        system.python_version
    )

    system_table.add_row(
        "CPU",
        system.cpu.name
    )

    system_table.add_row(
        "CPU Cores",
        str(system.cpu.cores)
    )

    system_table.add_row(
        "RAM",
        system.memory.total
    )

    system_table.add_row(
        "Disk Free",
        system.disk.free
    )

    system_table.add_row(
        "GPU",
        system.gpu.name
    )

    console.print(table)
    console.print(system_table)
    log.info("Doctor completed successfully")
