"""
AIPM Command Line Interface.
"""

from __future__ import annotations

import typer

#
# Command Groups
#

from aipm.commands import (
    download,
    models,
    registry,
    verify,
    remove,
    repair,
    upgrade,
    update,
)

#
# Single Command Implementations
#

from aipm.commands.install import run as install_run
from aipm.commands.search import run as search_run
from aipm.commands import (
    history,
)
from aipm.commands.health import app as health_app
app = typer.Typer(
    help="Universal AI Package Manager",
)

# ----------------------------------------------------------------------
# Command Groups
# ----------------------------------------------------------------------

app.add_typer(
    models.app,
    name="models",
)

app.add_typer(
    registry.app,
    name="registry",
)

app.add_typer(
    download.app,
    name="download",
)

app.add_typer(
    verify.app,
    name="verify",
)

app.add_typer(
    remove.app,
    name="remove",
)

app.add_typer(
    repair.app,
    name="repair",
)

app.add_typer(
    upgrade.app,
    name="upgrade",
)

app.add_typer(
    update.app,
    name="update",
)
app.add_typer(
    history.app,
    name="history",
)
app.add_typer(
    health_app,
    name="health",
)

# ----------------------------------------------------------------------
# Single Commands
# ----------------------------------------------------------------------

@app.command("install")
def install(
    name: str,
) -> None:
    """
    Install an AI model.
    """

    install_run(name)


@app.command("search")
def search(
    keyword: str,
) -> None:
    """
    Search AI models.
    """

    search_run(keyword)


@app.command("doctor")
def doctor() -> None:
    """
    Check system information.
    """

    from aipm.commands.doctor import run

    run()


@app.command("version")
def version() -> None:
    """
    Show application version.
    """

    from aipm.commands.version import run

    run()


# ----------------------------------------------------------------------
# Global Options
# ----------------------------------------------------------------------

@app.callback(
    invoke_without_command=True,
)
def main(
    version_flag: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show version information.",
    ),
) -> None:
    """
    Universal AI Package Manager.
    """

    if version_flag:

        version()

        raise typer.Exit()