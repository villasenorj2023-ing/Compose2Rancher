"""
Compose2Rancher Enterprise (C2R).

Herramienta empresarial para migrar aplicaciones Docker Compose hacia
Rancher/Kubernetes mediante un proceso automatizado, validado e inteligente.

Características principales
---------------------------
- Análisis de proyectos Docker Compose.
- Conversión hacia manifiestos Kubernetes.
- Integración con Rancher/RKE2/K3s.
- Gestión de ConfigMaps y Secrets.
- Gestión de Persistent Volumes.
- Generación de Ingress.
- Validaciones automáticas.
- Reportes técnicos.
- Migración de datos persistentes.

Autor:
    Arturo Villaseñor J.

Licencia:
    Apache License 2.0
"""

from __future__ import annotations

__title__: str = "Compose2Rancher Enterprise"
__package_name__: str = "compose2rancher"

__version__: str = "0.1.0-alpha"

__author__: str = "Arturo Villaseñor J."

__license__: str = "Apache-2.0"

__description__: str = (
    "Enterprise Docker Compose to Rancher/Kubernetes Migration Toolkit."
)

__url__: str = "https://github.com/arturovillasenor/compose2rancher"

__email__: str = "opensource@compose2rancher.dev"

__copyright__: str = (
    "Copyright (c) 2026 Arturo Villaseñor J. "
    "Todos los derechos reservados."
)

VERSION: tuple[int, int, int, str] = (
    0,
    1,
    0,
    "alpha",
)

__all__: list[str] = [
    "__title__",
    "__package_name__",
    "__version__",
    "__author__",
    "__license__",
    "__description__",
    "__url__",
    "__email__",
    "__copyright__",
    "VERSION",
]
