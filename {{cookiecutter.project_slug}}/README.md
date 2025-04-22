# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

- PySpark application for Databricks deployment
- Databricks Connect integration for local development
- Poetry for dependency management
- Type hints for better code quality
- Command-line interface for easy usage

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```bash
# Install Poetry if you don't have it
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install
```

## Usage

{% if cookiecutter.include_cli == "yes" %}
### Command Line Interface

```bash
# Activate the virtual environment
poetry shell

# Run the application
{{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table"
```

Or run directly with Poetry:

```bash
poetry run {{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table"
```
{% endif %}

### As a Python Module

```python
from {{ cookiecutter.project_slug }}.main import scan_table, create_spark_session

# Create a Spark session
spark = create_spark_session(use_databricks_connect=True)

# Scan a table
result_df = scan_table(spark, "your_catalog.your_schema.your_table")

# Show the results
result_df.show()
```

## Development

{% if cookiecutter.include_tests == "yes" %}
### Running Tests

```bash
poetry run pytest
```
{% endif %}

{% if cookiecutter.include_docs == "yes" %}
### Documentation

Documentation is available in the `docs` directory.
{% endif %}

## License

This project is licensed under the MIT License - see the LICENSE file for details. 