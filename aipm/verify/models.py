"""
Verification models.
"""

from __future__ import annotations

from pydantic import BaseModel


class VerifyResult(BaseModel):
    name: str
    exists: bool
    checksum_valid: bool
    metadata_valid: bool
    message: str