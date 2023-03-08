import pytest
import json
import yaml
from gendiff.generate import generate_diff
from gendiff.parser import parse
from tests.fixtures.correct_outputs import STYLISH_BASIC, STYLISH_NESTED, PLAIN_NESTED, JSON_NESTED


#inputs for testing
JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
YAML1 = 'tests/fixtures/file1.yml'
YAML2 = 'tests/fixtures/file2.yml'
NESTED_JSON1 = 'tests/fixtures/nested_file1.json'
NESTED_JSON2 = 'tests/fixtures/nested_file2.json'
NESTED_YAML1 = 'tests/fixtures/nested_file1.yml'
NESTED_YAML2 = 'tests/fixtures/nested_file2.yml'

CORRECT_BASIC_DICT = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
}


@pytest.mark.parametrize("file_path,format,expected", [(JSON1, '.json', CORRECT_BASIC_DICT), (YAML1,'.yaml' or '.yml', CORRECT_BASIC_DICT)])
def test_parse(file_path, format, expected):
    assert parse(file_path, format) == expected


@pytest.mark.parametrize("file_path1,file_path2,format,expected", [
                        (JSON1, JSON2, 'stylish', STYLISH_BASIC),
                        (YAML1, YAML2, 'stylish', STYLISH_BASIC),
                        (NESTED_JSON1, NESTED_JSON2,'stylish', STYLISH_NESTED),
                        (NESTED_YAML1, NESTED_YAML2,'stylish', STYLISH_NESTED),
                        (NESTED_JSON1, NESTED_JSON2,'plain', PLAIN_NESTED),
                        (NESTED_YAML1, NESTED_YAML2,'plain', PLAIN_NESTED),
                        (NESTED_JSON1, NESTED_JSON2,'json', JSON_NESTED),
                        (NESTED_YAML1, NESTED_YAML2,'json', JSON_NESTED)
                        ])
def test_generate_diff(file_path1, file_path2, format, expected):
    assert generate_diff(file_path1, file_path2, format) == expected
