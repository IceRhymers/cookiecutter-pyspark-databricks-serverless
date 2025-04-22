# Cookiecutter PySpark Databricks

A Cookiecutter template for creating PySpark applications for Databricks deployment.

## Features

- PySpark application structure
- Poetry for dependency management
- Databricks Connect integration
- Type hints for better code quality
- Command-line interface
- Testing setup with pytest
- Documentation structure
- Makefile for common tasks

## Requirements

- Python 3.8+
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 2.0.0+
- [Poetry](https://python-poetry.org/) 1.0.0+

## Usage

```bash
# Install Cookiecutter if you don't have it
pip install cookiecutter

# Generate a new project
cookiecutter git@github.com:IceRhymers/cookiecutter-pyspark-databricks-serverless.git
```

## Options

When generating a new project, you'll be prompted for the following options:

- `project_name`: The name of your project
- `project_description`: A short description of your project
- `author_name`: Your name
- `author_email`: Your email address
- `python_version`: The Python version to use (default: 3.12)
- `databricks_connect_version`: The Databricks Connect version to use (default: 16.1)
- `include_cli`: Whether to include a command-line interface (default: yes)
- `include_tests`: Whether to include a testing setup (default: yes)
- `include_docs`: Whether to include a documentation structure (default: no)

## Project Structure

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.project_slug }}/         # Main package directory
│   ├── __init__.py                          # Package initialization
│   └── main.py                              # Main application code
├── tests/                                   # Test directory
│   ├── __init__.py                          # Test package initialization
│   └── test_main.py                         # Tests for main module
├── docs/                                    # Documentation directory
│   ├── README.md                            # Documentation README
│   ├── api.md                               # API documentation
│   ├── usage.md                             # Usage examples
│   └── deployment.md                        # Deployment instructions
├── .gitignore                               # Git ignore file
├── Makefile                                 # Makefile for common tasks
├── README.md                                # Project README
└── pyproject.toml                           # Poetry configuration
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 