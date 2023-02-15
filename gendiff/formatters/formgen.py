from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def generate_formatters():
    return {'stylish': stylish, 'plain': plain, 'json': json}
