import pytest
from gendiff.gendiff import generate_diff


JSON1 = 'tests/fixtures/file1.json'
JSON2 = 'tests/fixtures/file2.json'
JSON_CORRECT = 'tests/fixtures/correct_json.txt'

def test_generate_diff():
    with open(JSON_CORRECT, 'r') as file:
        correct_result = file.read()
    assert generate_diff(JSON1, JSON2) == correct_result