# src/mi_app/llm_client.py
import asyncio
from openai import AsyncOpenAI
from app import config

class LLMClient:
    """
    Un cliente para interactuar con un LLM a través de una API compatible con OpenAI.
    La configuración se toma automáticamente del módulo `config`.
    """
    def __init__(self):
        print(f"Inicializando cliente LLM para proveedor: '{config.LLM_PROVIDER}'...")
        self.client = AsyncOpenAI(
            base_url=config.LLM_API_BASE_URL,
            api_key=config.LLM_API_KEY,
        )
        self.model = config.LLM_MODEL

    async def ask(self, prompt: str, system_prompt: str = "Eres un asistente útil.") -> str:
        """
        Envía un prompt al LLM y devuelve la respuesta.

        Args:
            prompt: La pregunta o instrucción para el LLM.
            system_prompt: El comportamiento que debe adoptar el LLM.

        Returns:
            La respuesta del modelo como una cadena de texto.
        """
        print(f"Enviando prompt al modelo '{self.model}': '{prompt[:50]}...'" ) # Removed unnecessary escaping for quotes
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
            )
            content = response.choices[0].message.content
            if content is None:
                return "El modelo no devolvió contenido."
            return content.strip()
        except Exception as e:
            print(f"Error al contactar al LLM: {e}")
            return f"Error: No se pudo conectar con el proveedor '{config.LLM_PROVIDER}'. Asegúrate de que esté en ejecución y accesible."

# Ejemplo de uso (para pruebas rápidas)
async def main():
    client = LLMClient()
    respuesta = await client.ask("¿Cuál es la capital de Francia?")
    print("\nRespuesta del modelo:") # Removed unnecessary escaping for newline
    print(respuesta)

if __name__ == "__main__":
    asyncio.run(main())
