from pathlib import Path

import yaml

from aipm.config.models import Config
from aipm.config.settings import expand

CONFIG_FILE = Path("configs/config.yaml")


def load_config() -> Config:

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    for key, value in data["storage"].items():
        data["storage"][key] = str(expand(value))

    return Config.model_validate(data)