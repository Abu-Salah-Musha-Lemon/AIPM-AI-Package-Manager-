"""
AI Model storage manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

from aipm.config import load_config
from aipm.logger import get_logger
from aipm.models.metadata import ModelMetadata


class ModelManager:
    """
    Manage AI model files.
    """

    def __init__(
        self,
        model_path: Path | None = None,
    ) -> None:

        cfg = load_config()

        self.log = get_logger(
            __name__,
            cfg.storage.logs,
        )

        self.path = (
            model_path
            if model_path
            else cfg.storage.models
        )


    def initialize(self) -> None:
        """
        Create model directory.
        """

        self.path.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.log.info(
            "Model storage initialized"
        )


    def list_models(self) -> list[str]:
        """
        Return installed models.
        """

        if not self.path.exists():
            return []


        models = []

        for item in self.path.iterdir():

            if item.is_dir():

                models.append(
                    item.name
                )

            elif item.is_file():

                models.append(
                    item.stem
                )


        return sorted(models)



    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check model exists.
        """

        return (
            self.path / name
        ).exists()



    def get_path(
        self,
        name: str,
    ) -> Path:
        """
        Return model path.
        """

        return self.path / name



    def get_metadata(
        self,
        name: str,
    ) -> ModelMetadata:
        """
        Generate model metadata.
        """

        path = self.get_path(name)

        size = "Unknown"


        if path.exists():

            if path.is_file():

                size = (
                    f"{path.stat().st_size / (1024**3):.2f} GB"
                )


        return ModelMetadata(
            name=name,
            path=path,
            size=size,
        )



model_manager = ModelManager()