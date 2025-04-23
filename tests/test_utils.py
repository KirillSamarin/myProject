from unittest.mock import patch
from src.utils import json_read
import json


def test_successful_read_with_patch():
    test_data = {"key": "value"}
    with patch('src.utils.open') as mocked_open:
        mocked_file = mocked_open.return_value
        mocked_file.read.return_value = json.dumps(test_data)
        mocked_file.__enter__.return_value = mocked_file

        result = json_read("path.json")
        assert result == test_data


def test_file_not_found_with_patch():
    with patch('src.utils.open'):
        result = json_read("file.json")
        assert result == []


def test_invalid_json_with_patch():
    invalid_json_string = "invalid json data"

    with patch('src.utils.open') as mocked_open:
        mocked_file = mocked_open.return_value
        mocked_file.read.return_value = invalid_json_string
        mocked_file.__enter__.return_value = mocked_file

        result = json_read("invalid_file.json")
        assert result == []
