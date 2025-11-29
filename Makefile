# Makefile para un proyecto Python moderno
#
# Este Makefile sigue las mejores prácticas de DevOps para automatizar el ciclo de
# vida de una aplicación Python.
#
# Requisitos previos:
#   - Python 3.8+ instalado en el sistema.
#   - Un archivo `pyproject.toml` para definir las dependencias y metadatos del proyecto.
#
# Uso:
#   1. `make install` - Para crear el entorno virtual e instalar dependencias.
#   2. `make check`   - Para ejecutar todas las verificaciones de calidad.
#   3. `make all`     - Para instalar dependencias y ejecutar todas las verificaciones.
#   4. `make help`    - Para ver todos los comandos disponibles.

# --- Variables de Configuración ---

# Usar python3 como intérprete por defecto.
PYTHON := python3

# Directorio del entorno virtual. La convención es `.venv`.
VENV_DIR := .venv

# Ruta al ejecutable de Python dentro del entorno virtual.
VENV_PYTHON := $(VENV_DIR)/bin/python

# Directorios de código fuente. Se asume una estructura con `src` y `tests`.
SRC_DIR := src
TEST_DIR := tests

# --- Metas Phony ---
# Declara metas que no son archivos para evitar conflictos.
.PHONY: help install format lint type-check test check all build clean activate

# Meta por defecto: se ejecuta cuando se llama a `make` sin argumentos.
.DEFAULT_GOAL := help

# --- Comandos Disponibles ---

activate: ## Activa el entorno virtual.
	@echo "Para activar el entorno virtual, ejecuta:"
	@echo "source $(VENV_DIR)/bin/activate"

help: ## Muestra esta ayuda.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: $(VENV_DIR)/bin/activate ## Crea el entorno virtual e instala las dependencias.
	@echo "Instalando dependencias desde pyproject.toml..."
	$(VENV_PYTHON) -m pip install --upgrade pip
	# Instala el proyecto en modo editable y las dependencias de desarrollo.
	# Asegúrate de tener una sección [project.optional-dependencies] con "dev" en tu pyproject.toml
	# que incluya: black, ruff, mypy, pytest, pytest-cov, build.
	$(VENV_PYTHON) -m pip install -e .[dev]
	@echo "\nEntorno listo. Para activarlo, ejecuta: make activate"

# El entorno virtual depende de `pyproject.toml`. Si este cambia, las dependencias deben reinstalarse.
$(VENV_DIR)/bin/activate: pyproject.toml
	@echo "Creando entorno virtual en $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)

format: ## Formatea el código fuente usando 'black' y 'ruff'.
	@echo "Formateando el código..."
	$(VENV_PYTHON) -m black $(SRC_DIR) $(TEST_DIR)
	$(VENV_PYTHON) -m ruff --fix $(SRC_DIR) $(TEST_DIR)

lint: ## Ejecuta el linter 'ruff' para verificar la calidad del código.
	@echo "Ejecutando linter..."
	$(VENV_PYTHON) -m ruff check $(SRC_DIR) $(TEST_DIR)

type-check: ## Verifica los tipos estáticos con 'mypy'.
	@echo "Verificando tipos estáticos..."
	$(VENV_PYTHON) -m mypy $(SRC_DIR)

test: ## Ejecuta las pruebas unitarias con 'pytest' y genera un reporte de cobertura.
	@echo "Ejecutando pruebas..."
	PYTHONPATH=$(SRC_DIR) $(VENV_PYTHON) -m pytest --cov=$(SRC_DIR) --cov-report term-missing

check: lint type-check test ## Ejecuta todas las verificaciones de calidad (sin formatear).
	@echo "\nTodas las verificaciones de calidad han pasado."

all: install check ## Instala dependencias y ejecuta todas las verificaciones.
	@echo "\nProyecto configurado y verificado con éxito."

build: ## Construye los paquetes de distribución (wheel y sdist).
	@echo "Construyendo paquetes..."
	$(VENV_PYTHON) -m build

clean: ## Elimina los artefactos de compilación, cachés y el entorno virtual.
	@echo "Limpiando el proyecto..."
	rm -rf $(VENV_DIR)
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Limpieza completada."

clone: ## Clona un repositorio de Git. Uso: make clone REPO_URL=<url> LOCAL_PATH=<path>
	@if [ -z "$(REPO_URL)" ] || [ -z "$(LOCAL_PATH)" ]; then \
		echo "Error: REPO_URL y LOCAL_PATH son obligatorios."; \
		echo "Uso: make clone REPO_URL=<url> LOCAL_PATH=<path>"; \
		exit 1; \
	fi
	$(VENV_PYTHON) $(SRC_DIR)/app/git_utils.py $(REPO_URL) $(LOCAL_PATH)
