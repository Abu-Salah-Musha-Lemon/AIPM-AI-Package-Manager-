"""
Download system for AIPM.
"""
from .manager import DownloadManager, download_manager
from .manager import DownloadManager
from .manager import download_manager
from .hash import calculate_sha256

download_manager = DownloadManager()

__all__ = [
    "download_manager",
    "DownloadManager",
    "calculate_sha256",
]