"""
Doctor result models for AIPM.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel


class DoctorStatus(
    str,
    Enum,
):
    """
    Doctor execution status.
    """

    SUCCESS = "success"

    FAILED = "failed"


class StorageStatus(BaseModel):
    """
    Storage directory status.
    """

    cache: bool = False

    models: bool = False

    loras: bool = False

    workflows: bool = False

    outputs: bool = False

    logs: bool = False


class DoctorResult(BaseModel):
    """
    Doctor command result.
    """

    status: DoctorStatus

    application: str = ""

    version: str = ""

    storage_root: str = ""

    system: object | None = None

    storage: StorageStatus

    message: str = ""