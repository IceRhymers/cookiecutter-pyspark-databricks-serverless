from typing import Optional
from pyspark.sql import SparkSession, DataFrame
from argparse import ArgumentParser

def create_spark_session(use_databricks_connect: bool = False) -> SparkSession:
    """
    Create and return a Spark session.
    
    Args:
        use_databricks_connect: If True, use Databricks Connect for local development.
                               If False, use standard Spark session (default).
    
    Returns:
        SparkSession: Configured Spark session
    """
    if use_databricks_connect:
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
    parser.add_argument("--local", '-l', action='store_true', help="Use Databricks Connect for local development")
    args = parser.parse_args()

    # Extract Arguments
    table_name = args.table_name
    use_local = args.local

    # Create Spark session
    spark: SparkSession = create_spark_session(use_local)
    
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