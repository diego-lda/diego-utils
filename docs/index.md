# Welcome to `diego-utils`

This site contains both the package documentation for `diego-utils` and my "playbook" for Data Science.
`diego-utils` is a Python package with some useful utility functions for data science and econometrics.
The "playbook" part of this site covers several Data Science aspects including:

- Git and sustainability considerations
- Useful Python bits, including my style guide
- Some thoughts on managing a Data Science Project

## 📋 Prerequisites

This package is requires a Python version between 3.11 and 3.13.
It uses `setup.py`, `setup.cfg`, and `pyproject.toml` for dependency management and packaging.

## 🛫 Set Up

### Install with PyPI

The faster and easier way to install `diego-utils` in using PyPI. From your terminal just run:

```bash
pip install diego-utils
```

### Install through Cloning the repository

Alternatively, `diego-utils` can also be installed by first cloning the repository:

```bash
git clone https://github.com/diego-lda/diego-utils.git
```

Then navigating into the home directory and running:

```bash
pip install .
```

## Running Tests

To run tests, ensure you're in the top-level directory of the project and execute:

`pytest`

This will run all the tests using the configurations set in the project.

You can also run `pytest` with coverage information running:

`pytest --cov=diego_utils`

## Pre-Commit Hooks

Pre-commit hooks are used to automate checks and formatting before commits. Follow these steps to set them up:

### Installation Steps

__Install pre-commit__: If you haven't already, install the pre-commit package:

`pip install pre-commit`

__Install pre-commit hooks__: Install the hooks defined in .pre-commit-config.yaml:

`pre-commit install`

This sets up the hooks to run automatically before each commit.

### Usage

The pre-commit hooks will automatically run on your modified files whenever you commit. To manually run all hooks on all files, use:

`pre-commit run --all-files`

This can be useful for checking your codebase.

By following these steps, your development environment for`diego-utils` will be ready, and you can start contributing to the project with ease.
