"""
Compose2Rancher Enterprise.

Interfaz de Línea de Comandos (CLI).

Este módulo define el punto central de interacción con la herramienta.
La lógica de negocio debe permanecer fuera de este archivo.

Autor:
    Arturo Villaseñor J.

Licencia:
    Apache License 2.0
"""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.panel import Panel

from compose2rancher import (
    __author__,
    __description__,
    __version__,
)

###############################################################################
# Rich Console
###############################################################################

console = Console()

###############################################################################
# Typer
###############################################################################

app = typer.Typer(
    name="compose2rancher",
    help="Enterprise Docker Compose to Rancher Migration Toolkit.",
    no_args_is_help=True,
    rich_markup_mode="rich",
    add_completion=False,
)

###############################################################################
# Version
###############################################################################


@app.command("version")
def version() -> None:
    """
    Muestra la versión instalada.
    """

    console.print()

    console.print(
        Panel.fit(
            f"[bold cyan]Compose2Rancher Enterprise[/bold cyan]\n\n"
            f"Versión : [green]{__version__}[/green]\n"
            f"Autor   : {__author__}\n\n"
            f"{__description__}",
            title="Información",
        )
    )


###############################################################################
# Analyze
###############################################################################


@app.command("analyze")
def analyze(
    compose: Annotated[
        Path,
        typer.Argument(
            exists=True,
            readable=True,
            resolve_path=True,
            help="Ruta del archivo docker-compose.yml",
        ),
    ],
) -> None:
    """
    Analiza un proyecto Docker Compose.

    Esta implementación corresponde al Sprint 1.
    Únicamente valida que el archivo exista.
    """

    console.print()

    console.print(
        Panel.fit(
            f"[green]Archivo encontrado correctamente[/green]\n\n"
            f"{compose}",
            title="Compose Analyzer",
        )
    )

    console.print()

    console.print(
        "[yellow]La implementación completa del analizador "
        "se desarrollará en el Sprint 2.[/yellow]"
    )


###############################################################################
# Callback
###############################################################################


@app.callback()
def main() -> None:
    """
    Punto de entrada principal de la CLI.
    """
    return
