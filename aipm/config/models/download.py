from __future__ import annotations

from pydantic import BaseModel


class DownloadConfig(BaseModel):
    """
    Download configuration.
    """

    workers: int = 4
    timeout: int = 60
    retries: int = 3
    verify_sha256: bool = True