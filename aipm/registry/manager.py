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
    Manage AI model registry.
    """

    def __init__(
        self,
    ) -> None:

        self.path = (
            Path(__file__).parent
            / "registry.yaml"
        )

        self.registry: Registry | None = None

    #
    # Core
    #

    def load(
        self,
    ) -> Registry:
        """
        Load registry from disk.
        Uses in-memory cache when available.
        """

        if self.registry is not None:

            return self.registry

        if not self.path.exists():

            self.registry = Registry()

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

    def reload(
        self,
    ) -> Registry:
        """
        Force reload registry.
        """

        self.registry = None

        return self.load()

    #
    # Query
    #

    def all_models(
        self,
    ) -> list[RegistryEntry]:
        """
        Return every registry model.
        """

        return self.load().models

    def list(
        self,
    ) -> list[RegistryEntry]:
        """
        Alias of all_models().
        """

        return self.all_models()

    def count(
        self,
    ) -> int:
        """
        Number of registry models.
        """

        return len(
            self.load().models
        )

    def names(
        self,
    ) -> list[str]:
        """
        Return model names.
        """

        return sorted(

            model.name

            for model in self.load().models

        )

    #
    # Lookup
    #

    def get(
        self,
        name: str,
    ) -> RegistryEntry | None:
        """
        Get registry model.
        """

        name = name.lower()

        for model in self.load().models:

            if model.name.lower() == name:

                return model

        return None

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check registry existence.
        """

        return self.get(name) is not None

    def require(
        self,
        name: str,
    ) -> RegistryEntry:
        """
        Return model or raise error.
        """

        model = self.get(name)

        if model is None:

            raise ValueError(
                f"Model '{name}' not found in registry."
            )

        return model

    #
    # Search
    #

    def search(
        self,
        keyword: str,
    ) -> list[RegistryEntry]:
        """
        Search registry.
        """

        keyword = keyword.lower().strip()

        if not keyword:

            return []

        results: list[
            RegistryEntry
        ] = []

        for model in self.load().models:

            searchable = " ".join(

                [

                    model.name,

                    model.description,

                    model.architecture,

                    model.type,

                    model.framework,

                ]

            ).lower()

            if keyword in searchable:

                results.append(
                    model
                )

        return results


registry_manager = RegistryManager()