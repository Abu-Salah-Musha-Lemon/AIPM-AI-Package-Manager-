"""
Version comparison utilities.
"""

from __future__ import annotations


def compare_versions(
    current: str,
    latest: str,
) -> int:
    """
    Compare two semantic versions.

    Returns

    -1  current < latest

     0  current == latest

     1  current > latest
    """

    current_parts = [
        int(x)
        for x in current.split(".")
    ]

    latest_parts = [
        int(x)
        for x in latest.split(".")
    ]

    #
    # Equalize lengths
    #

    length = max(
        len(current_parts),
        len(latest_parts),
    )

    current_parts.extend(
        [0]
        * (
            length
            - len(current_parts)
        )
    )

    latest_parts.extend(
        [0]
        * (
            length
            - len(latest_parts)
        )
    )

    #
    # Compare
    #

    for a, b in zip(
        current_parts,
        latest_parts,
    ):

        if a < b:
            return -1

        if a > b:
            return 1

    return 0