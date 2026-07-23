from __future__ import annotations

import typer

from aipm.commands import models
from aipm.commands import download

app = typer.Typer(
    help="Universal AI Package Manager"
)

#
# Command Groups
#

app.add_typer(
    models.app,
    name="models",
)

app.add_typer(
    download.app,
    name="download",
)

#
# Single Commands
#

@app.command("doctor")
def doctor_command() -> None:
    """
    Check system information.
    """

    from aipm.commands.doctor import run

    run()


@app.command("version")
def version_command() -> None:
    """
    Show application version.
    """

    from aipm.commands.version import run

    run()


#
# Global Options
#

@app.callback(invoke_without_command=True)
def main(
    version_flag: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version information.",
    ),
) -> None:
    if version_flag:
        version_command()
        raise typer.Exit()