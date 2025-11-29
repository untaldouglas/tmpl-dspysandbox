# Gemini Project: Plantilla de Aplicación Python

## Resumen del Proyecto

Este proyecto es una plantilla para aplicaciones de Python, estructurada con una clara separación de responsabilidades. El código fuente se encuentra en el directorio `src` y las pruebas en `tests`.

Se ha generado un `README.md` completo como guía para los nuevos desarrolladores que utilicen esta plantilla.

La aplicación principal (`src/app/main.py`) sirve como punto de entrada de ejemplo. El proyecto está diseñado para ser fácilmente adaptable, permitiendo a los desarrolladores sustituir la lógica de ejemplo por su propia funcionalidad.

## Comandos y Flujo de Trabajo

Este proyecto utiliza un `Makefile` para automatizar las tareas de desarrollo.

### Instalación

Para configurar el entorno de desarrollo e instalar las dependencias, ejecuta:

```bash
make install
```

### Ejecución de la Aplicación

Para ejecutar la aplicación principal, utiliza:

```bash
make run
```

### Pruebas y Calidad de Código

Para ejecutar el linter, el verificador de tipos y las pruebas unitarias, ejecuta:

```bash
make check
```

Consulta el `Makefile` o el `README.md` para ver una lista completa de los comandos disponibles.

## Convenciones de Desarrollo

*   **Estructura:** Código fuente en `src/app`, pruebas in `tests`.
*   **Dependencias:** Gestionadas en `pyproject.toml`.
*   **Formateo:** `black` y `ruff`.
*   **Pruebas:** `pytest`.
*   **Configuración:** Variables de entorno desde `.env`.
*   **Documentación:** `README.md` en la raíz del proyecto.