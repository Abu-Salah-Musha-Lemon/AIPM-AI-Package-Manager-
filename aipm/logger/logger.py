"""
Central logging utilities for AIPM.
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path


_LOGGERS: dict[str, logging.Logger] = {}



def _log_file(
    log_directory: Path,
) -> Path:
    """
    Return today's log file.
    """

    filename = (
        datetime.now()
        .strftime("%Y-%m-%d")
        + ".log"
    )

    return log_directory / filename



def get_logger(
    name: str = "aipm",
    log_directory: Path | None = None,
) -> logging.Logger:
    """
    Return configured logger.
    """

    if name in _LOGGERS:
        return _LOGGERS[name]


    logger = logging.getLogger(name)

    logger.setLevel(
        logging.INFO
    )

    logger.propagate = False


    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)-8s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )


    #
    # Console Handler
    #

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        console_handler
    )


    #
    # File Handler
    #

    if log_directory:

        log_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        file_handler = logging.FileHandler(
            _log_file(log_directory),
            encoding="utf-8",
        )

        file_handler.setFormatter(
            formatter
        )

        logger.addHandler(
            file_handler
        )


    _LOGGERS[name] = logger

    return logger