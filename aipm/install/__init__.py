"""
Install package for AIPM.
"""

from .manager import (
    InstallManager,
    install_manager,
)

from .models import (
    InstallResult,
    InstallStatus,
)

__all__ = [
    "InstallManager",
    "install_manager",
    "InstallResult",
    "InstallStatus",
]