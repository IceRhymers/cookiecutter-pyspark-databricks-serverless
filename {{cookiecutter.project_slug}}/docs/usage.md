# Usage Examples

## Command Line Interface

The application provides a command-line interface for easy usage:

```bash
# Activate the virtual environment
poetry shell

# Run the application in Databricks mode (default)
{{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table"

# Run the application in local development mode
{{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table" -l
# or
{{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table" --local
```

Or run directly with Poetry:

```bash
# Run in Databricks mode (default)
poetry run {{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table"

# Run in local development mode
poetry run {{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table" -l
```

## Advanced Usage

### Local Development Mode

The `-l` or `--local` flag allows you to run the application in local development mode, which:
