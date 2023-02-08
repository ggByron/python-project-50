import pytest
import json
import yaml
from gendiff.gendiff import generate_diff
from gendiff.parser import parse


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
YAML1 = 'tests/fixtures/file1.yml'
YAML2 = 'tests/fixtures/file2.yml'

NESTED_JSON1 = 'tests/fixtures/nested_file1.json'
NESTED_JSON2 = 'tests/fixtures/nested_file2.json'
NESTED_YAML1 = 'tests/fixtures/nested_file1.yml'
NESTED_YAML2 = 'tests/fixtures/nested_file2.yml'

OUTPUT_FOR_SIMPLE ='''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''
OUTPUT_FOR_NESTED = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

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

def test_generate_diff_nested():
    assert generate_diff(NESTED_JSON1, NESTED_JSON2) == OUTPUT_FOR_NESTED
    assert generate_diff(NESTED_YAML1, NESTED_YAML2) == OUTPUT_FOR_NESTED