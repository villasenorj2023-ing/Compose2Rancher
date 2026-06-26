"""
Compose2Rancher Enterprise.

Punto de entrada principal del paquete.

Este módulo permite ejecutar la aplicación utilizando:

    python -m compose2rancher

No contiene lógica de negocio; únicamente delega la ejecución
a la interfaz de línea de comandos (CLI).

Autor:
    Arturo Villaseñor J.

Licencia:
    Apache License 2.0
"""

from __future__ import annotations

import sys

from compose2rancher.cli import app


def main() -> int:
    """
    Ejecuta la interfaz de línea de comandos.

    Returns:
        int: Código de salida del proceso.

            0 -> Ejecución exitosa.
            !=0 -> Error durante la ejecución.
    """
    try:
        app()

    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
        return 130

    except Exception as exc:  # pragma: no cover
        print(f"\nError inesperado: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
