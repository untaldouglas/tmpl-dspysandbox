# src/app/git_utils.py
import git
import os
import argparse
from typing import Optional

def clonar_repo(repo_url: str, local_path: str) -> Optional[git.Repo]:
    """
    Clona un repositorio de Git desde una URL a una ruta local.

    La autenticación (SSH o HTTPS) se delega a la configuración de Git
    del sistema, que es la forma segura de hacerlo. No se manejan
    credenciales directamente en esta función.

    Args:
        repo_url: La URL del repositorio (ej. 'git@github.com:user/repo.git').
        local_path: La ruta local donde se clonará el repositorio.

    Returns:
        El objeto del repositorio si tiene éxito, None si falla.
    """
    if os.path.exists(local_path):
        print(f"El directorio '{local_path}' ya existe. No se clonará.")
        return None
    
    try:
        print(f"Clonando '{repo_url}' en '{local_path}'...")
        repo = git.Repo.clone_from(repo_url, local_path)
        print("Repositorio clonado con éxito.")
        return repo
    except git.GitCommandError as e:
        print(f"Error al clonar el repositorio: {e}")
        return None

def main():
    """Punto de entrada para la ejecución desde la línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Clona un repositorio de Git desde una URL a una ruta local."
    )
    parser.add_argument("repo_url", help="La URL del repositorio a clonar.")
    parser.add_argument("local_path", help="La ruta local donde se clonará el repositorio.")
    
    args = parser.parse_args()
    
    clonar_repo(args.repo_url, args.local_path)

if __name__ == "__main__":
    main()
