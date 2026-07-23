from aipm import APP_NAME, __version__
from aipm.utils.console import console
from aipm.logger import get_logger

def run() -> None:
    """Display AIPM version."""

    log = get_logger(__name__)

    log.info("Version command executed")

    console.print(
        f"[bold cyan]{APP_NAME}[/bold cyan] "
        f"[green]v{__version__}[/green]"
    )