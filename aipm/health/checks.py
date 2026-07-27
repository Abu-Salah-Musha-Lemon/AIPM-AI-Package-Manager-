"""
Health check functions for AIPM.
"""

from __future__ import annotations

import platform
import socket

from aipm.config import load_config
from aipm.registry import registry_manager
from aipm.cache import cache_manager
from aipm.history import history_manager
from aipm.storage import storage_manager

from .models import (
    HealthCheck,
    HealthStatus,
)


def check_python() -> HealthCheck:
    """
    Verify Python runtime.
    """

    version = platform.python_version()

    return HealthCheck(
        name="Python",
        status=HealthStatus.SUCCESS,
        message="Python runtime detected.",
        details={
            "version": version,
        },
    )


def check_storage() -> HealthCheck:
    """
    Verify storage directories.
    """

    missing: list[str] = []

    for directory in (
        "cache",
        "models",
        "logs",
        "outputs",
        "workflows",
        "loras",
    ):

        if not storage_manager.exists(directory):

            missing.append(directory)

    if missing:

        return HealthCheck(
            name="Storage",
            status=HealthStatus.FAILED,
            message="Missing storage directories.",
            details={
                "missing": ", ".join(missing),
            },
        )

    return HealthCheck(
        name="Storage",
        status=HealthStatus.SUCCESS,
        message="Storage is healthy.",
    )


def check_registry() -> HealthCheck:
    """
    Verify registry.
    """

    models = registry_manager.all_models()

    if not models:

        return HealthCheck(
            name="Registry",
            status=HealthStatus.WARNING,
            message="Registry is empty.",
        )

    return HealthCheck(
        name="Registry",
        status=HealthStatus.SUCCESS,
        message="Registry loaded.",
        details={
            "models": str(len(models)),
        },
    )


def check_cache() -> HealthCheck:
    """
    Verify cache.
    """

    entries = cache_manager.list()

    return HealthCheck(
        name="Cache",
        status=HealthStatus.SUCCESS,
        message="Cache loaded.",
        details={
            "entries": str(len(entries)),
        },
    )


def check_history() -> HealthCheck:
    """
    Verify history.
    """

    entries = history_manager.list()

    return HealthCheck(
        name="History",
        status=HealthStatus.SUCCESS,
        message="History loaded.",
        details={
            "entries": str(len(entries)),
        },
    )


def check_config() -> HealthCheck:
    """
    Verify configuration.
    """

    cfg = load_config()

    return HealthCheck(
        name="Configuration",
        status=HealthStatus.SUCCESS,
        message="Configuration loaded.",
        details={
            "storage": str(cfg.storage.root),
        },
    )


def check_network() -> HealthCheck:
    """
    Verify internet connectivity.
    """

    try:

        socket.create_connection(
            ("8.8.8.8", 53),
            timeout=3,
        ).close()

        return HealthCheck(
            name="Network",
            status=HealthStatus.SUCCESS,
            message="Internet connection available.",
        )

    except OSError:

        return HealthCheck(
            name="Network",
            status=HealthStatus.WARNING,
            message="No internet connection.",
        )