# API Documentation

## `create_spark_session`

```python
def create_spark_session(use_databricks_connect: bool = False) -> SparkSession:
    """
    Create and return a Spark session.
    
    Args:
        use_databricks_connect: If True, use Databricks Connect for local development.
                               If False, use standard Spark session (default).
    
    Returns:
        SparkSession: Configured Spark session
    """
```

Creates and returns a Spark session. If `use_databricks_connect` is True, it will attempt to use Databricks Connect for local development. If Databricks Connect is not available, it will fall back to a standard Spark session.

## `scan_table`

```python
def scan_table(spark: SparkSession, table_name: str, limit: int = 10) -> DataFrame:
    """
    Perform a simple table scan and return the first N rows.
    
    Args:
        spark: SparkSession object
        table_name: Name of the table to scan
        limit: Maximum number of rows to return (default: 10)
    
    Returns:
        DataFrame: DataFrame containing the first N rows of the table
    """
```

Performs a simple table scan and returns the first N rows of the specified table. The `limit` parameter controls the maximum number of rows to return.

## `main`

```python
def main() -> None:
    """
    Main function to run the PySpark application.
    """
```

The main entry point for the application. It parses command-line arguments, creates a Spark session, scans the specified table, and displays the results. 