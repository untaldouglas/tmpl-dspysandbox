# Plantilla de Proyecto Python Moderna
## Author : @untaldouglas

Este proyecto es una plantilla para iniciar aplicaciones de Python. Incluye herramientas y prácticas recomendadas para un desarrollo limpio y automatizado.

## Características

-   **Gestión de Dependencias:** Usa `pyproject.toml`.
-   **Automatización:** `Makefile` preconfigurado para instalación, pruebas, linting, etc.
-   **Calidad de Código:** Formateo con `black` y `ruff`, linting con `ruff` y tipado estático con `mypy`.
-   **Pruebas:** `pytest` y `pytest-cov` para pruebas unitarias y cobertura.
-   **Entorno Virtual:** Aislamiento de dependencias en `.venv`.
-   **Configuración:** Carga de variables de entorno desde `.env`.
-   **Estructura Clara:** Directorios `src/` y `tests/`.

## Cómo Empezar

### Prerrequisitos

-   Python 3.8+
-   `make`
-   `git`

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_PLANTILLA> mi_nuevo_proyecto
    cd mi_nuevo_proyecto
    ```

2.  **Instala las dependencias:**
    ```bash
    make install
    ```

3.  **Activa el entorno virtual:**
    ```bash
    make activate
    # Copia y pega la salida en tu terminal, que será:
    # source .venv/bin/activate
    ```

4.  **Configura las variables de entorno:**
    Copia el archivo de ejemplo y edítalo.
    ```bash
    cp .env.example .env
    # Edita .env con tus valores
    ```

## Uso

El `Makefile` contiene los comandos para el flujo de trabajo:

| Comando | Descripción |
| :--- | :--- |
| `make install` | Instala dependencias. |
| `make activate`| Muestra el comando para activar el entorno. |
| `make run` | Ejecuta la aplicación principal. |
| `make check` | Ejecuta `lint`, `type-check` y `test`. |
| `make format` | Formatea el código. |
| `make lint` | Ejecuta el linter `ruff`. |
| `make type-check` | Ejecuta `mypy`. |
| `make test` | Ejecuta las pruebas con `pytest`. |
| `make build` | Construye los paquetes de distribución. |
| `make clone` | Clona un repositorio de Git. |
| `make clean` | Elimina artefactos de compilación y cachés. |
| `make help` | Muestra todos los comandos. |

## Cómo Adaptar esta Plantilla

1.  **Cambia el Nombre del Proyecto:**
    En `pyproject.toml`, cambia el campo `name`.

2.  **Añade Dependencias:**
    -   Producción: a `dependencies` en `pyproject.toml`.
    -   Desarrollo: a `dev` en `[project.optional-dependencies]`.
    Luego, ejecuta `make install`.

3.  **Escribe tu Código:**
    -   Modifica o elimina los archivos de ejemplo en `src/app/`.
    -   Añade tus módulos en `src/`.

4.  **Añade Pruebas:**
    -   Añade tus pruebas en `tests/`, siguiendo la estructura de `src/`.

## Estructura del Proyecto

```
.
├── .env.example
├── .gitignore
├── GEMINI.md
├── Makefile
├── pyproject.toml
├── src/
│   └── app/
│       ├── __init__.py
│       ├── config.py
│       ├── git_utils.py
│       ├── llm_client.py
│       └── main.py
└── tests/
    ├── test_git_utils.py
    └── test_llm_client.py
```
