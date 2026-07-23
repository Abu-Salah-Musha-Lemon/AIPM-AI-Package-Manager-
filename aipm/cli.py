from __future__ import annotations

import typer

from aipm.commands.doctor import run as doctor
from aipm.commands.version import run as version
from aipm.commands import models

app = typer.Typer(
    name="aipm",
    help="Universal AI Package Manager",
    no_args_is_help=True,
    add_completion=False,
)
app.add_typer(
    models.app,
    name="models"
)

@app.command()
def doctor() -> None:
    """Check system information."""
    from aipm.commands.doctor import run
    run()


@app.command()
def version() -> None:
    """Show application version."""
    from aipm.commands.version import run
    run()


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
        version()
        raise typer.Exit()