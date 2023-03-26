import pytest
import json
from gendiff.generate import generate_diff
from gendiff.parser import parse


PATH = 'tests/fixtures/'


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


@pytest.mark.parametrize(
    "content, file_format, expected", [
        (read_file(f'{PATH}file1.json'), '.json', json.loads(read_file(f'{PATH}file1_content.json'))),
        (read_file(f'{PATH}file1.yml'), '.yml', json.loads(read_file(f'{PATH}file1_content.json')))
    ]
)
def test_parse(content, file_format, expected):
    assert parse(content, file_format) == expected


@pytest.mark.parametrize(
    "file_path1, file_path2, format, expected", [
        (f'{PATH}file1.json', f'{PATH}file2.json', 'stylish', read_file(f'{PATH}correct_stylish_basic.txt')),
        (f'{PATH}file1.yml', f'{PATH}file2.yml', 'stylish', read_file(f'{PATH}correct_stylish_basic.txt')),
        (f'{PATH}nested_file1.json', f'{PATH}nested_file2.json', 'stylish', read_file(f'{PATH}correct_stylish_nested.txt')),
        (f'{PATH}nested_file1.yml', f'{PATH}nested_file2.yml', 'stylish', read_file(f'{PATH}correct_stylish_nested.txt')),
        (f'{PATH}nested_file1.json', f'{PATH}nested_file2.json', 'plain', read_file(f'{PATH}correct_plain.txt')),
        (f'{PATH}nested_file1.yml', f'{PATH}nested_file2.yml', 'plain', read_file(f'{PATH}correct_plain.txt')),
        (f'{PATH}nested_file1.json', f'{PATH}nested_file2.json', 'json', read_file(f'{PATH}correct_json.txt')),
        (f'{PATH}nested_file1.yml', f'{PATH}nested_file2.yml', 'json', read_file(f'{PATH}correct_json.txt'))
    ]
)
def test_generate_diff(file_path1, file_path2, format, expected):
    assert generate_diff(file_path1, file_path2, format) == expected
