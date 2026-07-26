"""
Install CLI command.
"""

from __future__ import annotations

import typer

from aipm.install import (
    install_manager,
    InstallStatus,
)

from aipm.utils.console import console


def run(
    name: str,
) -> None:
    """
    Install an AI model.
    """

    console.print(
        f"[bold cyan]Installing:[/bold cyan] {name}"
    )

    result = install_manager.install(
        name
    )

    #
    # Failed
    #

    if result.status == InstallStatus.FAILED:

        console.print(
            f"[bold red]Error:[/bold red] {result.message}"
        )

        raise typer.Exit(
            code=1
        )

    #
    # Already installed
    #

    if result.status == InstallStatus.SKIPPED:

        console.print(
            "[bold yellow]Already installed.[/bold yellow]"
        )

        console.print(
            f"Model   : {result.name}"
        )

        console.print(
            f"Version : {result.version}"
        )

        if result.path:

            console.print(
                f"Path    : {result.path}"
            )

        return

    #
    # Success
    #

    console.print(
        "\n[bold green]✓ Installation completed successfully[/bold green]"
    )

    console.print(
        f"Model   : {result.name}"
    )

    console.print(
        f"Version : {result.version}"
    )

    if result.path:

        console.print(
            f"Path    : {result.path}"
        )