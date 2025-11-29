# Modern Python Project Template

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Code Coverage](https://img.shields.io/badge/coverage-80%25-yellow)
![License](https://img.shields.io/badge/license-MIT-blue)

Este proyecto sirve como una plantilla moderna y robusta para iniciar nuevas aplicaciones en Python. Incluye un conjunto de herramientas y prácticas recomendadas para asegurar un desarrollo limpio, automatizado y de alta calidad.

## Características

-   **Gestión de Dependencias:** Usa `pyproject.toml` para una gestión de dependencias moderna y estándar.
-   **Automatización con `make`:** Un `Makefile` preconfigurado para automatizar tareas comunes como instalación, pruebas, linting y formateo.
-   **Calidad de Código:**
    -   **Formateo:** `black` y `ruff` para un estilo de código consistente.
    -   **Linting:** `ruff` para detectar problemas y errores comunes.
    -   **Tipado Estático:** `mypy` para verificar los tipos y prevenir bugs.
-   **Pruebas Unitarias:** Entorno de pruebas con `pytest` y `pytest-cov` para medir la cobertura de código.
-   **Entorno Virtual:** Creación automática de un entorno virtual en `.venv` para aislar las dependencias.
-   **Configuración Centralizada:** Carga de variables de entorno desde un archivo `.env` para una configuración flexible.
-   **Estructura de Proyecto Clara:** Disposición de directorios `src/` para el código fuente y `tests/` para las pruebas.

## Cómo Empezar

### Prerrequisitos

-   Python 3.8 o superior.
-   `make` para ejecutar los comandos automatizados.
-   `git` para el control de versiones.

### Instalación

1.  **Clona este repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO_PLANTILLA> mi_nuevo_proyecto
    cd mi_nuevo_proyecto
    ```

2.  **Crea el entorno virtual e instala las dependencias:**
    El siguiente comando creará un directorio `.venv` con el intérprete de Python y todas las dependencias listadas en `pyproject.toml`.
    ```bash
    make install
    ```

3.  **Activa el entorno virtual:**
    Para usar las herramientas y ejecutar la aplicación, activa el entorno. El `Makefile` proporciona un comando para mostrar el comando de activación.
    ```bash
    make activate
    # Copia y pega la salida en tu terminal, que será:
    # source .venv/bin/activate
    ```

4.  **Configura tus variables de entorno:**
    Copia el archivo de ejemplo y edítalo con tu configuración.
    ```bash
    cp .env.example .env
    # Ahora, edita el archivo .env con tus valores
    # Por ejemplo, para usar un LLM de OpenAI:
    # LLM_PROVIDER=openai
    # LLM_MODEL=gpt-4
    # LLM_API_KEY=sk-xxxxxxxxxxxx
    ```

## Uso

### Ejecutar la Aplicación de Ejemplo

Este template incluye una pequeña aplicación asíncrona en `src/app/main.py` que demuestra cómo usar el cliente LLM. Para ejecutarla:

```bash
python src/app/main.py
```

### Flujo de Trabajo de Desarrollo

El `Makefile` es el corazón del flujo de trabajo. Aquí están los comandos más importantes:

| Comando | Descripción |
| :--- | :--- |
| `make install` | Crea el entorno virtual e instala todas las dependencias. |
| `make activate` | Muestra el comando para activar el entorno virtual. |
| `make check` | Ejecuta todas las verificaciones de calidad: `lint`, `type-check` y `test`. |
| `make format` | Formatea todo el código con `black` y `ruff`. |
| `make lint` | Ejecuta el linter `ruff` para buscar errores y problemas de estilo. |
| `make type-check` | Ejecuta `mypy` para verificar la consistencia de los tipos. |
| `make test` | Ejecuta las pruebas unitarias con `pytest` y muestra un reporte de cobertura. |
| `make build` | Construye los paquetes de distribución (wheel y sdist) en el directorio `dist/`. |
| `make clone` | Clona un repositorio de Git. **Uso:** `make clone REPO_URL=<url> LOCAL_PATH=<path>` |
| `make clean` | Elimina todos los artefactos de compilación, cachés y el entorno virtual. |
| `make help` | Muestra una lista de todos los comandos disponibles. |


## Cómo Adaptar esta Plantilla

1.  **Cambia el Nombre del Proyecto:**
    Abre `pyproject.toml` y cambia el campo `name` de `"python-project-template"` al nombre de tu nuevo proyecto.

    ```toml
    [project]
    name = "mi-super-app"
    version = "0.1.0"
    ...
    ```

2.  **Añade Dependencias:**
    -   Para dependencias de producción, añádelas a la lista `dependencies` en `pyproject.toml`.
    -   Para dependencias de desarrollo (herramientas, librerías de prueba), añádelas a la lista `dev` en `[project.optional-dependencies]`.

    Después de modificar `pyproject.toml`, ejecuta `make install` de nuevo para actualizar tu entorno.

3.  **Escribe tu Código:**
    -   Elimina o modifica los archivos de ejemplo en `src/app/`.
    -   Añade tus propios módulos y paquetes dentro de `src/`.

4.  **Añade Pruebas:**
    -   Añade tus archivos de prueba en el directorio `tests/`. Es una buena práctica que la estructura de `tests/` refleje la de `src/`.
    -   Asegúrate de que tus nuevos archivos de prueba sigan el patrón `test_*.py`.

## Estructura del Proyecto

```
.
├── .env.example          # Archivo de ejemplo para variables de entorno
├── .gitignore            # Archivos y directorios a ignorar por Git
├── GEMINI.md             # Archivo de contexto para Gemini
├── Makefile              # Automatización de tareas de desarrollo
├── pyproject.toml        # Configuración del proyecto y dependencias
├── src/
│   └── app/              # Paquete principal de la aplicación
│       ├── __init__.py
│       ├── config.py     # Carga de configuración
│       ├── git_utils.py  # Utilidades de Git
│       ├── llm_client.py # Cliente para el Large Language Model
│       └── main.py       # Punto de entrada de la aplicación
└── tests/
    ├── test_git_utils.py
    └── test_llm_client.py
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* para discutir cambios importantes antes de enviar un *pull request*.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
