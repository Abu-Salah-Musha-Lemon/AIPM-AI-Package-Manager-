"""
Logger Factory

Provides a singleton logger instance for the application.
"""

from __future__ import annotations

import logging

_LOGGER: logging.Logger | None = None


def get_logger(name: str = "aipm") -> logging.Logger:
    """
    Return the application logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
    """

    global _LOGGER

    if _LOGGER is None:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                "%Y-%m-%d %H:%M:%S",
            )

            handler.setFormatter(formatter)

            logger.addHandler(handler)

        logger.propagate = False

        _LOGGER = logger

    return _LOGGER