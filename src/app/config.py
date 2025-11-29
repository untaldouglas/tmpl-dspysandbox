# src/mi_app/config.py
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# --- Configuración de LLM ---
# Lee las variables del entorno, con valores por defecto para Ollama local.
LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")
LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-oss:120b-cloud")
LLM_API_BASE_URL: str | None = os.getenv("LLM_API_BASE_URL") or "http://localhost:11434/v1"
LLM_API_KEY: str = os.getenv("LLM_API_KEY", "ollama")

# Si el proveedor es OpenAI y no hay URL base, se usará la URL por defecto de OpenAI.
if LLM_PROVIDER == "openai" and not os.getenv("LLM_API_BASE_URL"):
    LLM_API_BASE_URL = None

# --- Configuración de Git ---
# Lee la URL del repositorio del entorno.
GIT_REPO_URL: str | None = os.getenv("GIT_REPO_URL")

