import pytest
import json
from gendiff.generate import generate_diff
from gendiff.parser import parse


def path(file_path):
    return f'tests/fixtures/{file_path}'


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


@pytest.mark.parametrize(
    "content, file_format, expected", [
        (read_file(path('file1.json')), '.json', json.loads(read_file(path('file1_content.json')))),
        (read_file(path('file1.yml')), '.yml', json.loads(read_file(path('file1_content.json'))))
    ]
)
def test_parse(content, file_format, expected):
    assert parse(content, file_format) == expected


@pytest.mark.parametrize(
    "file_path1, file_path2, format, expected", [
        (path('file1.json'), path('file2.json'), 'stylish', read_file(path('correct_stylish_basic.txt'))),
        (path('file1.yml'), path('file2.yml'), 'stylish', read_file(path('correct_stylish_basic.txt'))),
        (path('nested_file1.json'), path('nested_file2.json'), 'stylish', read_file(path('correct_stylish_nested.txt'))),
        (path('nested_file1.yml'), path('nested_file2.yml'), 'stylish', read_file(path('correct_stylish_nested.txt'))),
        (path('nested_file1.json'), path('nested_file2.json'), 'plain', read_file(path('correct_plain.txt'))),
        (path('nested_file1.yml'), path('nested_file2.yml'), 'plain', read_file(path('correct_plain.txt'))),
        (path('nested_file1.json'), path('nested_file2.json'), 'json', read_file(path('correct_json.txt'))),
        (path('nested_file1.yml'), path('nested_file2.yml'), 'json', read_file(path('correct_json.txt')))
    ]
)
def test_generate_diff(file_path1, file_path2, format, expected):
    assert generate_diff(file_path1, file_path2, format) == expected
