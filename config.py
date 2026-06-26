"""
Compose2Rancher Enterprise.

Configuración global de la aplicación.

Toda la configuración del proyecto se centraliza en este módulo.

La configuración puede provenir de:

- Valores por defecto
- Variables de entorno
- Archivo .env (Sprint 2)
- Argumentos CLI (Sprint 3)

Autor:
    Arturo Villaseñor J.

Licencia:
    Apache License 2.0
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from compose2rancher import (
    __author__,
    __description__,
    __package_name__,
    __version__,
)


class Settings(BaseSettings):
    """
    Configuración global de Compose2Rancher.
    """

    model_config = SettingsConfigDict(
        env_prefix="C2R_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        validate_assignment=True,
    )

    ###########################################################################
    # Application
    ###########################################################################

    app_name: str = Field(
        default=__package_name__,
        description="Nombre de la aplicación.",
    )

    app_title: str = Field(
        default="Compose2Rancher Enterprise",
        description="Nombre comercial.",
    )

    version: str = Field(
        default=__version__,
        description="Versión instalada.",
    )

    description: str = Field(
        default=__description__,
    )

    author: str = Field(
        default=__author__,
    )

    ###########################################################################
    # General
    ###########################################################################

    debug: bool = Field(
        default=False,
        description="Modo Debug.",
    )

    log_level: str = Field(
        default="INFO",
    )

    output_directory: Path = Field(
        default=Path("output"),
    )

    reports_directory: Path = Field(
        default=Path("reports"),
    )

    log_directory: Path = Field(
        default=Path("logs"),
    )

    ###########################################################################
    # Kubernetes
    ###########################################################################

    default_namespace: str = Field(
        default="default",
    )

    default_storage_class: str = Field(
        default="longhorn",
    )

    image_pull_policy: str = Field(
        default="IfNotPresent",
    )

    ###########################################################################
    # Rancher
    ###########################################################################

    rancher_url: str = Field(
        default="",
    )

    rancher_token: str = Field(
        default="",
    )

    ###########################################################################
    # Registry
    ###########################################################################

    registry_url: str = Field(
        default="",
    )

    registry_username: str = Field(
        default="",
    )

    registry_password: str = Field(
        default="",
    )

    ###########################################################################
    # Kompose
    ###########################################################################

    kompose_binary: str = Field(
        default="kompose",
    )

    ###########################################################################
    # Kubectl
    ###########################################################################

    kubectl_binary: str = Field(
        default="kubectl",
    )

    ###########################################################################
    # Docker
    ###########################################################################

    docker_binary: str = Field(
        default="docker",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """
    Devuelve una instancia singleton de la configuración.

    Returns
    -------
    Settings
        Configuración global.
    """
    return Settings()


settings = get_settings()
