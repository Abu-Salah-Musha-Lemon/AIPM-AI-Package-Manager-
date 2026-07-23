from aipm import APP_NAME, __version__
from aipm.utils.console import console


def run() -> None:
    """Display AIPM version."""

    console.print(
        f"[bold cyan]{APP_NAME}[/bold cyan] "
        f"[green]v{__version__}[/green]"
    )