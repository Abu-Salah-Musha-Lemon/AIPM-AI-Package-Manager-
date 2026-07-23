"""
Central logging utilities for AIPM.
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path


_LOGGERS: dict[str, logging.Logger] = {}


def _log_directory() -> Path:
    """
    Return the AIPM log directory.

    Example (Windows):
        C:\\Users\\<user>\\.aipm\\logs
    """

    directory = Path.home() / ".aipm" / "logs"
    directory.mkdir(parents=True, exist_ok=True)

    return directory


def _log_file() -> Path:
    """
    Return today's log file.
    """

    filename = datetime.now().strftime("%Y-%m-%d") + ".log"

    return _log_directory() / filename


def get_logger(name: str = "aipm") -> logging.Logger:
    """
    Return a configured logger instance.
    """

    if name in _LOGGERS:
        return _LOGGERS[name]

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    #
    # Console
    #

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    #
    # File
    #

    file_handler = logging.FileHandler(
        _log_file(),
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    _LOGGERS[name] = logger

    return logger