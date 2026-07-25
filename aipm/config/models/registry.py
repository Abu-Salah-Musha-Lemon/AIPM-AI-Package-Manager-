from __future__ import annotations

from pydantic import BaseModel


class RegistryConfig(BaseModel):
    """
    Registry configuration.
    """

    url: str = (
        "https://raw.githubusercontent.com/Abu-Salah-Musha-Lemon/aipm-registry/main/registry.yaml"
    )

    timeout: int = 30