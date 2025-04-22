# Deployment Instructions

## Deploying to Databricks

### Using Databricks Asset Bundle

1. Build the wheel package:

```bash
poetry build
```

2. Deploy the bundle to Databricks:

```bash
databricks bundle deploy
```

The project includes a `databricks.yml` file that configures the Databricks Asset Bundle. This file defines a job that runs the main function of your application. You can customize the parameters in the `databricks.yml` file to suit your needs.

### Manual Deployment

1. Build the wheel package:

```bash
poetry build
```

2. Upload the wheel file to Databricks:

```bash
databricks libraries install --cluster-id <cluster-id> --whl dist/{{ cookiecutter.project_slug }}-0.1.0-py3-none-any.whl
```

3. Create a job in Databricks:

```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import JobSettings, PythonWheelTask

client = WorkspaceClient()

job_settings = JobSettings(
    name="Scan Table Job",
    tasks=[
        PythonWheelTask(
            package_name="{{ cookiecutter.project_slug }}",
            entry_point="main",
            parameters=["--table-name", "your_catalog.your_schema.your_table"]
        )
    ]
)

job = client.jobs.create(job_settings)
```

## Local Development

The application supports local development with Databricks Connect, by including a `-l` or `--local` flag

```bash
poetry run {{ cookiecutter.project_slug }} --table-name "your_catalog.your_schema.your_table" -l
```