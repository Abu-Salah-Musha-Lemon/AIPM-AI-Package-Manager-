"""
Doctor CLI commands for AIPM.
"""

from __future__ import annotations

import platform

from rich.table import Table

from aipm.doctor import (
    doctor_manager,
    DoctorStatus,
)
from aipm.utils.console import console


def run() -> None:
    """
    Display diagnostic information.
    """

    result = doctor_manager.run()

    if result.status != DoctorStatus.SUCCESS:

        console.print(
            f"[bold red]Error:[/bold red] {result.message}"
        )

        return

    #
    # Application
    #

    app_table = Table(
        title="AIPM Doctor"
    )

    app_table.add_column(
        "Property",
        style="cyan",
    )

    app_table.add_column(
        "Value",
        style="green",
    )

    app_table.add_row(
        "Application",
        result.application,
    )

    app_table.add_row(
        "Version",
        result.version,
    )

    app_table.add_row(
        "Python",
        platform.python_version(),
    )

    app_table.add_row(
        "Platform",
        platform.system(),
    )

    app_table.add_row(
        "Release",
        platform.release(),
    )

    app_table.add_row(
        "Architecture",
        platform.machine(),
    )

    app_table.add_row(
        "Storage",
        result.storage_root,
    )

    #
    # System
    #

    system = result.system

    system_table = Table(
        title="System Information"
    )

    system_table.add_column(
        "Property",
        style="cyan",
    )

    system_table.add_column(
        "Value",
        style="green",
    )

    system_table.add_row(
        "Operating System",
        system.operating_system,
    )

    system_table.add_row(
        "Release",
        system.release,
    )

    system_table.add_row(
        "Architecture",
        system.architecture,
    )

    system_table.add_row(
        "Python",
        system.python_version,
    )

    system_table.add_row(
        "CPU",
        system.cpu.name,
    )

    system_table.add_row(
        "CPU Cores",
        str(system.cpu.cores),
    )

    system_table.add_row(
        "CPU Threads",
        str(system.cpu.threads),
    )

    system_table.add_row(
        "RAM",
        system.memory.total,
    )

    system_table.add_row(
        "Available RAM",
        system.memory.available,
    )

    system_table.add_row(
        "Disk Free",
        system.disk.free,
    )

    system_table.add_row(
        "GPU Vendor",
        system.gpu.vendor,
    )

    system_table.add_row(
        "GPU Name",
        system.gpu.name,
    )

    system_table.add_row(
        "GPU Memory",
        system.gpu.memory,
    )

    system_table.add_row(
        "GPU Driver",
        system.gpu.driver,
    )

    system_table.add_row(
        "CUDA Available",
        str(system.gpu.cuda_available),
    )

    system_table.add_row(
        "CUDA Version",
        system.gpu.cuda_version,
    )

    #
    # Storage
    #

    storage_table = Table(
        title="Storage Information"
    )

    storage_table.add_column(
        "Directory",
        style="cyan",
    )

    storage_table.add_column(
        "Status",
        style="green",
    )

    storage = result.storage

    storage_table.add_row(
        "Cache",
        "Ready" if storage.cache else "Missing",
    )

    storage_table.add_row(
        "Models",
        "Ready" if storage.models else "Missing",
    )

    storage_table.add_row(
        "Loras",
        "Ready" if storage.loras else "Missing",
    )

    storage_table.add_row(
        "Workflows",
        "Ready" if storage.workflows else "Missing",
    )

    storage_table.add_row(
        "Outputs",
        "Ready" if storage.outputs else "Missing",
    )

    storage_table.add_row(
        "Logs",
        "Ready" if storage.logs else "Missing",
    )

    console.print(app_table)
    console.print(system_table)
    console.print(storage_table)

    console.print(
        "\n[bold green]✓ Doctor completed successfully[/bold green]"
    )