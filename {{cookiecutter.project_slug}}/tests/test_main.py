"""
Tests for the main module
"""
import pytest
from unittest.mock import patch, MagicMock

from {{ cookiecutter.project_slug }}.main import scan_table, create_spark_session

@pytest.fixture
def mock_spark():
    """Create a mock Spark session for testing."""
    with patch('{{ cookiecutter.project_slug }}.main.SparkSession') as mock:
        spark = MagicMock()
        mock.builder.getOrCreate.return_value = spark
        yield spark

def test_scan_table(mock_spark):
    """Test the scan_table function."""
    # Mock the table method
    mock_df = MagicMock()
    mock_spark.table.return_value = mock_df
    
    # Mock the limit method
    mock_result_df = MagicMock()
    mock_df.limit.return_value = mock_result_df
    
    # Call the function
    result = scan_table(mock_spark, "test_table", limit=5)
    
    # Verify the function calls
    mock_spark.table.assert_called_once_with("test_table")
    mock_df.limit.assert_called_once_with(5)
    
    # Verify the return value
    assert result == mock_result_df 