# Getting Started

This is an open-source FastAPI template to get developers speed up their development process.

## Installation

1. The recommended python version is mentioned in [.python-version](./.python-version).
    - You can use `pyenv` to manage your python versions.
    - If do not have the recommended python version installed, simply run `pyenv install <the-python-version>`.
2. Run `poetry shell` to create a virtual environment.
    - If you prefer having your _virtualenv_ to be created in the same folder, run `poetry config virtualenvs.in-project=true virtualenvs.create=true`.
3. Run `poetry install`.

# Dependencies and Setup

Following dependencies are used to run the project:

| Dependency Name | Description                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `poetry`        | Dependency and package management.                                                                                                                                                       |
| `pytest`        | We are using pytest as our unit testing framework.                                                                                                                                       |
| `Flask`         | This boilerplate provides a Flask production-ready API template, so we use Flask as our main framework.                                                                                  |
| `autopep8`      | This is used for styling and formatting our Python code.                                                                                                                                 |
| `flake8`        | This is used as our linting style.                                                                                                                                                       |
| `pre-commit`    | We use `pre-commit` to manage our `git` hooks. There are few hooks that is installed by default in this repo <br /> for `pre-commit` and they are mentioned in `.pre-commit-config.yaml` |
| `python-dotenv` | This is used to load `.env` files into our environment.                                                                                                                                  |
| `waitress`      | We use this library to create a production-ready server.                                                                                                                                 |
