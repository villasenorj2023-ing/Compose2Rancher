"""
Compose2Rancher Enterprise.

Sistema centralizado de logging.

Este módulo encapsula completamente la configuración de Loguru.
Ningún otro módulo del proyecto debe importar directamente Loguru.

Características:

- Logging en consola.
- Logging en archivo.
- Rotación automática.
- Compresión.
- Retención.
- Colores.
- Backtrace.
- Diagnóstico.

Autor:
    Arturo Villaseñor J.

Licencia:
    Apache License 2.0
"""

from __future__ import annotations

import sys
from pathlib import Path

from loguru import logger as _logger

from compose2rancher.config import settings

###############################################################################
# Directorio de logs
###############################################################################

LOG_DIRECTORY: Path = settings.log_directory
LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "compose2rancher.log"

###############################################################################
# Eliminar configuración por defecto
###############################################################################

_logger.remove()

###############################################################################
# Consola
###############################################################################

_logger.add(
    sys.stderr,
    level=settings.log_level,
    colorize=True,
    backtrace=True,
    diagnose=settings.debug,
    enqueue=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    ),
)

###############################################################################
# Archivo
###############################################################################

_logger.add(
    LOG_FILE,
    level=settings.log_level,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    backtrace=True,
    diagnose=settings.debug,
    encoding="utf-8",
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level: <8} | "
        "{process.name}:{thread.name} | "
        "{name}:{function}:{line} | "
        "{message}"
    ),
)

###############################################################################
# Logger público
###############################################################################

logger = _logger

__all__ = [
    "logger",
]
