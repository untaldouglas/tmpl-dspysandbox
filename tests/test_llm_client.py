# tests/test_llm_client.py
import unittest
import asyncio
import os
import importlib
from unittest.mock import patch, MagicMock, AsyncMock

class TestLLMClient(unittest.TestCase):

    @patch('openai.AsyncOpenAI')
    @patch.dict(os.environ, {
        'LLM_PROVIDER': 'test_provider',
        'LLM_MODEL': 'test_model',
        'LLM_API_BASE_URL': 'http://test.url/v1',
        'LLM_API_KEY': 'test_key'
    })
    def test_init_cliente(self, mock_async_openai: MagicMock):
        """Prueba que el cliente se inicializa con la configuración correcta."""
        from app import config
        importlib.reload(config)
        import app.llm_client
        importlib.reload(app.llm_client)
        from app.llm_client import LLMClient

        # Instanciamos el cliente
        client = LLMClient()
        
        # Verifica que AsyncOpenAI fue llamado con los datos de config
        mock_async_openai.assert_called_once_with(
            base_url='http://test.url/v1',
            api_key='test_key'
        )
        self.assertEqual(client.model, 'test_model')

    @patch('openai.AsyncOpenAI')
    @patch.dict(os.environ, {
        'LLM_PROVIDER': 'test_provider',
        'LLM_MODEL': 'test_model',
        'LLM_API_BASE_URL': 'http://test.url/v1',
        'LLM_API_KEY': 'test_key'
    })
    def test_ask_exitoso(self, mock_async_openai: MagicMock):
        """Prueba que el método 'ask' construye y envía la petición correctamente."""
        # Recargamos los módulos
        from app import config
        importlib.reload(config)
        import app.llm_client
        importlib.reload(app.llm_client)
        from app.llm_client import LLMClient

        # Configura el mock para la llamada asíncrona
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Respuesta de prueba"
        
        mock_client_instance = mock_async_openai.return_value
        mock_client_instance.chat.completions.create = AsyncMock(return_value=mock_response)

        # Ejecuta la prueba
        client = LLMClient()
        prompt = "¿Funciona la prueba?"
        
        respuesta = asyncio.run(client.ask(prompt))

        # Verifica que el método de la API fue llamado con los argumentos correctos
        mock_client_instance.chat.completions.create.assert_called_once_with(
            model='test_model',
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )
        
        self.assertEqual(respuesta, "Respuesta de prueba")

if __name__ == '__main__':
    unittest.main()
