"""
Model verification manager.
"""

from __future__ import annotations

from pathlib import Path

from aipm.cache import cache_manager
from aipm.download.hash import calculate_sha256
from aipm.verify.models import VerifyResult


class VerifyManager:

    def verify(
        self,
        name: str,
    ) -> VerifyResult:

        cached = cache_manager.get(name)

        if cached is None:

            return VerifyResult(
                name=name,
                exists=False,
                checksum_valid=False,
                metadata_valid=False,
                message="Model not found in cache.",
            )

        path = Path(cached.path)

        if not path.exists():

            return VerifyResult(
                name=name,
                exists=False,
                checksum_valid=False,
                metadata_valid=False,
                message="Model file is missing.",
            )

        checksum = (
            calculate_sha256(path)
            == cached.sha256
        )

        return VerifyResult(
            name=name,
            exists=True,
            checksum_valid=checksum,
            metadata_valid=True,
            message=(
                "Verification successful."
                if checksum
                else "SHA256 mismatch."
            ),
        )


verify_manager = VerifyManager()