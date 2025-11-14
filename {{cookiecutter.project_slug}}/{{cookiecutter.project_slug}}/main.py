import os
from typing import Optional
from pyspark.sql import SparkSession, DataFrame
from argparse import ArgumentParser

def create_spark_session() -> SparkSession:
    """
    Create and return a Spark session. Will use Databricks Connect if we're running outside of the Databricks environment.
    
    Returns:
        SparkSession: Configured Spark session
    """
    if os.environ.get("DATABRICKS_RUNTIME_VERSION") is None:
        try:
            # Import and use Databricks Connect
            from databricks.connect import DatabricksSession
            return DatabricksSession.builder.serverless().getOrCreate()
        except ImportError:
            print("Databricks Connect not available. Falling back to standard Spark session.")
            return SparkSession.builder.getOrCreate()
    else:
        return SparkSession.builder.getOrCreate()

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
    # Read the table
    df: DataFrame = spark.table(table_name)
    
    # Limit the number of rows
    result_df: DataFrame = df.limit(limit)
    
    return result_df

def main() -> None:
    """
    Main function to run the PySpark application.
    """
    # Define parser
    parser = ArgumentParser(description="{{ cookiecutter.project_description }}")
    parser.add_argument("--table-name", '-t', type=str, help="Name of the table to scan")
    args = parser.parse_args()

    # Extract Arguments
    table_name = args.table_name

    # Create Spark session
    spark: SparkSession = create_spark_session()
    
    try:
        # Scan the table
        result_df: DataFrame = scan_table(spark, table_name)
        
        # Show the results
        print(f"First 10 rows of table '{table_name}':")
        result_df.show()
        
        # Print schema
        print(f"Schema of table '{table_name}':")
        result_df.printSchema()
        
    except Exception as e:
        print(f"Error scanning table '{table_name}': {str(e)}")
    
    finally:
        # Stop the Spark session
        spark.stop()

if __name__ == "__main__":
    main() 