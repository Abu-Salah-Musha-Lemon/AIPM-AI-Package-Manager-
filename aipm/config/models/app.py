from __future__ import annotations

from pydantic import BaseModel


class AppConfig(BaseModel):
    """
    Application metadata configuration.
    """

    name: str = "AIPM"
    version: str = "0.1.0-alpha.1"