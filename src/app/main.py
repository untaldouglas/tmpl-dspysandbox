# src/mi_app/main.py
import asyncio
from app.llm_client import LLMClient

async def main() -> None:
    """Punto de entrada principal de la aplicación."""
    print("--- Demostración de Cliente LLM Configurable ---")

    # 1. Inicializa el cliente. La configuración se carga automáticamente.
    llm_client = LLMClient()

    # 2. Prepara una pregunta para el modelo.
    pregunta = "Explica brevemente qué es un Makefile en el contexto de DevOps."

    # 3. Envía la pregunta y espera la respuesta.
    respuesta = await llm_client.ask(pregunta)

    # 4. Muestra la respuesta.
    print("\nRespuesta del modelo:")
    print(respuesta)


if __name__ == "__main__":
    # Ejecuta la función asíncrona principal.
    asyncio.run(main())
