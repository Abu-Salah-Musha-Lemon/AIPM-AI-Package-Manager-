from dataclasses import dataclass
from pathlib import Path

@dataclass(slots=True)
class StoragePaths:
    root: Path
    logs: Path
    models: Path
    downloads: Path
    cache: Path
    plugins: Path
    workflows: Path
    registry: Path
    providers: Path
    configs: Path
    temp: Path
    backups: Path