import pandas as pd
from unittest.mock import patch, mock_open
from src.reading_tables import dict_csv, dict_excel

TEST_DATA = [
    {"col1": 1, "col2": "test1", "col3": "value1"},
    {"col1": 2, "col2": "test2", "col3": "value2"},
    {"col1": 3, "col2": "test3", "col3": "value3"},
]
CSV_CONTENT = "col1;col2;col3\n1;test1;value1\n2;test2;value2\n3;test3;value3"


def test_csv_reader():
    with patch("builtins.open", mock_open(read_data=CSV_CONTENT)):
        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame(TEST_DATA)
            result = dict_csv("test.csv")
            assert result == TEST_DATA


def test_xlsx_reader():
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame(TEST_DATA)
        result = dict_excel("test.xlsx")
        assert result == TEST_DATA
