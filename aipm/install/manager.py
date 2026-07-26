"""
Installation manager for AIPM.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from aipm.download import download_manager
from aipm.logger import get_logger
from aipm.models import model_manager
from aipm.registry import (
    RegistryEntry,
    registry_manager,
)
from aipm.verify import verify_manager

from .models import (
    InstallResult,
    InstallStatus,
)


class InstallManager:
    """
    Install AI models.
    """

    def __init__(
        self,
    ) -> None:

        self.log = get_logger(
            __name__
        )

    def install(
        self,
        name: str,
    ) -> InstallResult:
        """
        Install an AI model.
        """

        self.log.info(
            f"Installing model: {name}"
        )

        #
        # Registry lookup
        #

        registry_model = registry_manager.get(
            name
        )

        if registry_model is None:

            self.log.error(
                "Registry entry not found."
            )

            return InstallResult(
                status=InstallStatus.FAILED,
                message="Registry entry not found.",
            )

        #
        # Already installed
        #

        if model_manager.exists(
            name
        ):

            metadata = model_manager.get_metadata(
                name
            )

            self.log.info(
                "Model already installed."
            )

            return InstallResult(
                status=InstallStatus.SKIPPED,
                name=metadata.name,
                version=metadata.version,
                path=metadata.path,
                message="Model already installed.",
            )

        #
        # Download
        #

        try:

            path = download_manager.download(
                name=registry_model.name,
                url=registry_model.url,
                sha256=registry_model.sha256 or "",
            )

            self._write_metadata(
                registry_model,
                path.parent,
            )

        except Exception as error:

            self.log.exception(
                "Installation failed."
            )

            return InstallResult(
                status=InstallStatus.FAILED,
                message=str(error),
            )

        #
        # Verify
        #

        verify = verify_manager.verify(
            name
        )

        if not verify.exists:

            self.log.error(
                verify.message
            )

            return InstallResult(
                status=InstallStatus.FAILED,
                message=verify.message,
            )

        if not verify.checksum_valid:

            self.log.error(
                verify.message
            )

            return InstallResult(
                status=InstallStatus.FAILED,
                message=verify.message,
            )

        #
        # Read metadata
        #

        metadata = model_manager.get_metadata(
            name
        )

        self.log.info(
            "Installation completed successfully."
        )

        return InstallResult(
            status=InstallStatus.SUCCESS,
            name=metadata.name,
            version=metadata.version,
            path=metadata.path,
            message="Installation completed successfully.",
        )

    def _write_metadata(
        self,
        model: RegistryEntry,
        directory: Path,
    ) -> None:
        """
        Write metadata.yaml.
        """

        metadata = {

            "name": model.name,

            "version": model.version,

            "architecture": model.architecture,

            "framework": model.framework,

            "type": model.type,

            "format": model.format,

            "source": getattr(
                model,
                "source",
                "",
            ),

            "url": model.url,

            "sha256": model.sha256,

            "description": getattr(
                model,
                "description",
                "",
            ),

        }

        metadata_file = (
            directory
            / "metadata.yaml"
        )

        with metadata_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            yaml.safe_dump(
                metadata,
                file,
                sort_keys=False,
                allow_unicode=True,
            )

        self.log.info(
            f"Metadata created: {metadata_file}"
        )


install_manager = InstallManager()