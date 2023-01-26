import pytest
import json
import yaml
from gendiff.gendiff import generate_diff
from gendiff.parser import parse


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
YAML1 = 'tests/fixtures/file1.yml'
YAML2 = 'tests/fixtures/file2.yml'
OUTPUT_FOR_SIMPLE ='''- follow: False
host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True'''


def test_parse_json():
    with open(JSON1, 'r') as file:
        parsed_file = json.load(file)
        assert parse('tests/fixtures/file1.json') == parsed_file
    

def test_parse_yaml():
    with open(YAML1, 'r') as file:
        parsed_file = yaml.load(file, Loader=yaml.FullLoader)
        assert parse('tests/fixtures/file1.yml') == parsed_file


def test_generate_diff_json():
    assert generate_diff(JSON1, JSON2) == OUTPUT_FOR_SIMPLE


def test_generate_diff_yaml():
    assert generate_diff(YAML1, YAML2) == OUTPUT_FOR_SIMPLE
