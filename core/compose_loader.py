"""
Compose2Rancher Enterprise.

Compose Loader.

Responsabilidad:

    Leer docker-compose.yml

No interpreta el contenido.
"""

from pathlib import Path
from typing import Any

import yaml

from core.compose_parser import ComposeParser
from core.logger import logger
from core.models import ComposeDocument


class ComposeLoaderError(Exception):
    """Error durante la lectura del archivo."""


class ComposeLoader:

    def __init__(self, compose_file: Path):

        self.compose_file = compose_file

    def load(self) -> ComposeDocument:

        logger.info(
            f"Leyendo {self.compose_file}"
        )

        if not self.compose_file.exists():

            raise ComposeLoaderError(
                f"No existe {self.compose_file}"
            )

        with self.compose_file.open(
            encoding="utf-8"
        ) as fp:

            data: dict[str, Any] = yaml.safe_load(fp) or {}

        parser = ComposeParser()

        compose = parser.parse(data)

        logger.success(
            "Compose cargado correctamente."
        )

        return compose
