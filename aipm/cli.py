from __future__ import annotations

import typer

from aipm.commands import models
from aipm.commands import download
from aipm.commands import registry
from aipm.commands import install
from aipm.commands.install import run as install_run
from aipm.commands import verify
from aipm.commands import remove
from aipm.commands import repair
from aipm.commands import upgrade

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
app.add_typer(
    verify.app,
    name="verify",
)

app.add_typer(
    registry.app,
    name="registry",
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



@app.command("install")
def install(
    name: str,
) -> None:
    """
    Install AI model.
    """

    install_run(name)

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