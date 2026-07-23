"""
Download system for AIPM.
"""

from .manager import DownloadManager

download_manager = DownloadManager()

__all__ = [
    "download_manager",
    "DownloadManager",
]