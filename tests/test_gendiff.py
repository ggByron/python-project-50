import pytest
import json
import yaml
from gendiff.gendiff import generate_diff
from gendiff.parser import parse
from tests.fixtures.correct_outputs import STYLISH_BASIC, STYLISH_NESTED, PLAIN_NESTED

#inputs for testing
JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
YAML1 = 'tests/fixtures/file1.yml'
YAML2 = 'tests/fixtures/file2.yml'
NESTED_JSON1 = 'tests/fixtures/nested_file1.json'
NESTED_JSON2 = 'tests/fixtures/nested_file2.json'
NESTED_YAML1 = 'tests/fixtures/nested_file1.yml'
NESTED_YAML2 = 'tests/fixtures/nested_file2.yml'


def test_parse_json():
    with open(JSON1, 'r') as file:
        parsed_file = json.load(file)
        assert parse('tests/fixtures/file1.json') == parsed_file
    

def test_parse_yaml():
    with open(YAML1, 'r') as file:
        parsed_file = yaml.load(file, Loader=yaml.FullLoader)
        assert parse('tests/fixtures/file1.yml') == parsed_file


def test_generate_diff():
    assert generate_diff(JSON1, JSON2) == STYLISH_BASIC
    assert generate_diff(YAML1, YAML2) == STYLISH_BASIC


def test_stylish_nested():
    assert generate_diff(NESTED_JSON1, NESTED_JSON2, 'stylish') == STYLISH_NESTED
    assert generate_diff(NESTED_YAML1, NESTED_YAML2, 'stylish') == STYLISH_NESTED


def test_plain_nested():
    assert generate_diff(NESTED_JSON1, NESTED_JSON2, 'plain') == PLAIN_NESTED
    assert generate_diff(NESTED_YAML1, NESTED_YAML2, 'plain') == PLAIN_NESTED
