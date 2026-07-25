from __future__ import annotations

from pydantic import BaseModel


class RegistryConfig(BaseModel):
    """
    Registry configuration.
    """

    url: str = (
        "https://github.com/Abu-Salah-Musha-Lemon/aipm-registry/blob/main/registry.yaml"
    )

    timeout: int = 30