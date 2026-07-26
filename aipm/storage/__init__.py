"""
Storage package for AIPM.
"""

from .manager import (
    StorageManager,
    storage_manager,
)

from .models import (
    StorageInfo,
    StorageResult,
    StorageStatus,
)

__all__ = [
    "StorageManager",
    "storage_manager",
    "StorageInfo",
    "StorageResult",
    "StorageStatus",
]