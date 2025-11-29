# tests/test_git_utils.py
import unittest
from unittest.mock import patch, MagicMock
from app.git_utils import clonar_repo

class TestGitUtils(unittest.TestCase):

    @patch('git.Repo.clone_from')
    def test_clonar_repo_exitoso(self, mock_clone_from: MagicMock):
        """
        Prueba que la función `clonar_repo` llama a `git.Repo.clone_from`
        con los argumentos correctos cuando el clonado es exitoso.
        """
        repo_url = "git@github.com:user/repo.git"
        local_path = "/tmp/test_repo"

        # Simula que la clonación devuelve un objeto Repo
        mock_repo = MagicMock()
        mock_clone_from.return_value = mock_repo

        # Llama a la función a probar
        result = clonar_repo(repo_url, local_path)

        # Verifica que git.Repo.clone_from fue llamado una vez con los argumentos correctos
        mock_clone_from.assert_called_once_with(repo_url, local_path)
        
        # Verifica que la función devuelve el objeto repo simulado
        self.assertEqual(result, mock_repo)

    @patch('git.Repo.clone_from')
    @patch('os.path.exists', return_value=True)
    def test_clonar_repo_directorio_existente(self, mock_exists: MagicMock, mock_clone_from: MagicMock):
        """

        Prueba que no se intenta clonar si el directorio de destino ya existe.
        """
        repo_url = "git@github.com:user/repo.git"
        local_path = "/tmp/existing_repo"

        result = clonar_repo(repo_url, local_path)

        # Verifica que os.path.exists fue llamado
        mock_exists.assert_called_once_with(local_path)
        
        # Verifica que clone_from NO fue llamado
        mock_clone_from.assert_not_called()

        # Verifica que la función devuelve None
        self.assertIsNone(result)
