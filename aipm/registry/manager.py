"""
Registry manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from aipm.registry.models import (
    Registry,
    RegistryEntry,
)


class RegistryManager:
    """
    Manage model registry.
    """

    def __init__(self) -> None:

        self.path = (
            Path(__file__).parent
            / "registry.yaml"
        )

        self.registry = Registry(
            models=[]
        )

    def load(self) -> Registry:
        """
        Load registry file.
        """

        if not self.path.exists():
            return self.registry

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = yaml.safe_load(file) or {}

        self.registry = Registry(
            **data
        )

        return self.registry

    def all_models(
        self,
    ) -> list[RegistryEntry]:
        """
        Return all models.
        """

        return self.load().models

    def get(
        self,
        name: str,
    ) -> RegistryEntry | None:
        """
        Get model by name.
        """

        for model in self.load().models:

            if (
                model.name.lower()
                == name.lower()
            ):
                return model

        return None


registry_manager = RegistryManager()