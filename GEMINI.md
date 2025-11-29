# Gemini Project: Python LLM Application Template

## Project Overview

This project is a modern and robust template for Python applications. It demonstrates how to interact with a Large Language Model (LLM) using a configurable client and includes utility functions for Git. The project is structured with a clear separation of concerns, with source code in the `src` directory and tests in the `tests` directory.

A comprehensive `README.md` has been generated to serve as a guide for new developers using this template.

The main application (`src/app/main.py`) initializes an `LLMClient` and uses it to ask a question to the configured LLM. The `LLMClient` (`src/app/llm_client.py`) is designed to be compatible with OpenAI's API. The project also includes a Git utility function (`src/app/git_utils.py`) for cloning repositories, which can be executed from the command line via the `Makefile`.

The project has been updated to use modern Python packaging standards, generating `wheel` (`.whl`) and `sdist` packages, and removing legacy `.egg` formats from the final build.

## Building and Running

This project uses a `Makefile` to automate common development tasks.

### Installation

To set up the development environment and install dependencies, run:

```bash
make install
```

This will create a Python virtual environment in `.venv`, install the required dependencies from `pyproject.toml`, and install the project in editable mode.

### Running the Application

To run the main application, execute:

```bash
.venv/bin/python src/app/main.py
```

### Running Tests and Quality Checks

The project includes a suite of quality checks that can be run with a single command:

```bash
make check
```

This command will:
1.  Run the `ruff` linter to check for code quality issues.
2.  Run `mypy` to perform static type checking.
3.  Run `pytest` to execute unit tests and generate a code coverage report.

You can also run these checks and other commands individually. See the `Makefile` or the newly created `README.md` for a full list of commands, which includes:
- `make activate`
- `make lint`
- `make type-check`
- `make test`
- `make format`
- `make build`
- `make clone REPO_URL=<url> LOCAL_PATH=<path>`
- `make clean`

## Development Conventions

*   **Structure:** Source code is located in `src/app`, and tests are in `tests`.
*   **Dependencies:** Project dependencies are managed in `pyproject.toml`.
*   **Formatting:** Code is formatted with `black` and `ruff`. You can format the code by running `make format`.
*   **Testing:** Unit tests are written with `pytest` and `unittest.mock`.
*   **Configuration:** The application is configured through environment variables, as detailed in `.env.example`.
*   **Documentation:** A detailed `README.md` file is available in the project root, providing a comprehensive guide for developers.