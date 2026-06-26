"""
Compose2Rancher Enterprise.

Modelos de dominio.

Este módulo define todas las entidades utilizadas por el motor de análisis.
No contiene lógica de negocio; únicamente estructuras de datos tipadas.

Autor:
    Arturo Villaseñor J.

Licencia:
    Apache License 2.0
"""

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field


# ============================================================================
# Port
# ============================================================================

class Port(BaseModel):
    """Representa un puerto publicado por un servicio."""

    model_config = ConfigDict(extra="ignore")

    host: Optional[int] = Field(default=None)
    container: int
    protocol: str = Field(default="tcp")


# ============================================================================
# Volume
# ============================================================================

class Volume(BaseModel):
    """Representa un volumen Docker."""

    model_config = ConfigDict(extra="ignore")

    source: str
    target: str

    type: str = "bind"

    read_only: bool = False

    exists: bool = False


# ============================================================================
# Network
# ============================================================================

class Network(BaseModel):
    """Representa una red Docker."""

    model_config = ConfigDict(extra="ignore")

    name: str

    driver: str = "bridge"

    external: bool = False

    attachable: bool = False


# ============================================================================
# Environment Variable
# ============================================================================

class EnvironmentVariable(BaseModel):
    """Variable de entorno."""

    model_config = ConfigDict(extra="ignore")

    key: str

    value: str

    secret: bool = False


# ============================================================================
# Image
# ============================================================================

class Image(BaseModel):
    """Imagen Docker."""

    model_config = ConfigDict(extra="ignore")

    repository: str

    tag: str = "latest"

    registry: Optional[str] = None


# ============================================================================
# Service
# ============================================================================

class Service(BaseModel):
    """Servicio Docker Compose."""

    model_config = ConfigDict(extra="ignore")

    name: str

    image: Optional[Image] = None

    container_name: Optional[str] = None

    hostname: Optional[str] = None

    restart: Optional[str] = None

    command: Optional[str] = None

    entrypoint: Optional[str] = None

    working_dir: Optional[str] = None

    ports: List[Port] = Field(default_factory=list)

    volumes: List[Volume] = Field(default_factory=list)

    environment: List[EnvironmentVariable] = Field(default_factory=list)

    networks: List[str] = Field(default_factory=list)

    depends_on: List[str] = Field(default_factory=list)

    labels: Dict[str, str] = Field(default_factory=dict)


# ============================================================================
# Compose Document
# ============================================================================

class ComposeDocument(BaseModel):
    """Documento docker-compose.yml."""

    model_config = ConfigDict(extra="ignore")

    version: Optional[str] = None

    name: Optional[str] = None

    services: List[Service] = Field(default_factory=list)

    volumes: List[Volume] = Field(default_factory=list)

    networks: List[Network] = Field(default_factory=list)


# ============================================================================
# Inventory
# ============================================================================

class Inventory(BaseModel):
    """
    Inventario completo del proyecto.
    """

    model_config = ConfigDict(extra="ignore")

    compose: ComposeDocument

    services: int = 0

    images: int = 0

    ports: int = 0

    volumes: int = 0

    networks: int = 0

    environment_variables: int = 0

    secrets: int = 0

    warnings: List[str] = Field(default_factory=list)

    errors: List[str] = Field(default_factory=list)
