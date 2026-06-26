###############################################################################
#
# Compose2Rancher Enterprise
#
# Makefile
#
###############################################################################

.DEFAULT_GOAL := help

###############################################################################
# Variables
###############################################################################

PYTHON      := python3

PIP         := pip

PACKAGE     := compose2rancher

SRC         := src

TESTS       := tests

VERSION     := 0.1.0-alpha

###############################################################################
# Colors
###############################################################################

GREEN=\033[0;32m
BLUE=\033[0;34m
YELLOW=\033[1;33m
RED=\033[0;31m
NC=\033[0m

###############################################################################
# Help
###############################################################################

help:
	@echo ""
	@echo "==========================================================="
	@echo " Compose2Rancher Enterprise"
	@echo "==========================================================="
	@echo ""
	@echo " Comandos disponibles"
	@echo ""
	@echo "  make install        Instalar dependencias"
	@echo "  make upgrade        Actualizar dependencias"
	@echo "  make clean          Limpiar archivos temporales"
	@echo "  make lint           Ejecutar Ruff"
	@echo "  make format         Ejecutar Black"
	@echo "  make typecheck      Ejecutar MyPy"
	@echo "  make test           Ejecutar pruebas"
	@echo "  make coverage       Generar cobertura"
	@echo "  make check          Ejecutar todas las validaciones"
	@echo "  make run            Ejecutar la aplicación"
	@echo "  make version        Mostrar versión"
	@echo ""

###############################################################################
# Installation
###############################################################################

install:
	@echo "$(GREEN)Instalando dependencias...$(NC)"
	$(PIP) install -U pip
	$(PIP) install -e ".[dev]"

upgrade:
	@echo "$(GREEN)Actualizando dependencias...$(NC)"
	$(PIP) install -U pip setuptools wheel

###############################################################################
# Formatting
###############################################################################

format:
	@echo "$(GREEN)Formateando código...$(NC)"
	black $(SRC) $(TESTS)

###############################################################################
# Ruff
###############################################################################

lint:
	@echo "$(GREEN)Ejecutando Ruff...$(NC)"
	ruff check $(SRC) $(TESTS)

lint-fix:
	@echo "$(GREEN)Corrigiendo errores automáticamente...$(NC)"
	ruff check $(SRC) $(TESTS) --fix

###############################################################################
# MyPy
###############################################################################

typecheck:
	@echo "$(GREEN)Ejecutando MyPy...$(NC)"
	mypy $(SRC)

###############################################################################
# Tests
###############################################################################

test:
	@echo "$(GREEN)Ejecutando pruebas...$(NC)"
	pytest

coverage:
	@echo "$(GREEN)Generando reporte de cobertura...$(NC)"
	pytest --cov=$(PACKAGE) --cov-report=html

###############################################################################
# Validation
###############################################################################

check:
	@echo ""
	@echo "============================================"
	@echo " Validación completa"
	@echo "============================================"
	@echo ""
	make lint
	make typecheck
	make test

###############################################################################
# Run
###############################################################################

run:
	python -m compose2rancher

###############################################################################
# Version
###############################################################################

version:
	@echo ""
	@echo "Compose2Rancher Enterprise"
	@echo "Versión: $(VERSION)"
	@echo ""

###############################################################################
# Cleaning
###############################################################################

clean:
	@echo "$(YELLOW)Limpiando proyecto...$(NC)"

	find . -type d -name "__pycache__" -exec rm -rf {} +

	find . -type d -name ".pytest_cache" -exec rm -rf {} +

	find . -type d -name ".ruff_cache" -exec rm -rf {} +

	find . -type d -name ".mypy_cache" -exec rm -rf {} +

	find . -type d -name "*.egg-info" -exec rm -rf {} +

	rm -rf build

	rm -rf dist

	rm -rf htmlcov

	rm -f .coverage

###############################################################################
# Package
###############################################################################

build:
	@echo "$(GREEN)Construyendo paquete...$(NC)"
	$(PYTHON) -m build

###############################################################################
# Documentation
###############################################################################

docs:
	mkdocs serve

docs-build:
	mkdocs build

###############################################################################
# Security
###############################################################################

security:
	@echo "$(GREEN)Ejecutando auditoría de dependencias...$(NC)"
	pip list --outdated

###############################################################################
# Development
###############################################################################

dev:
	make format
	make lint
	make typecheck
	make test

###############################################################################
# Git
###############################################################################

status:
	git status

###############################################################################
# End
###############################################################################
