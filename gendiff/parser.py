import os
import json
import yaml


def get_format(file_path):
    return os.path.splitext(file_path)[1]


def read(file_path):
    file_format = get_format(file_path)
    with open(file_path) as file:
        content = file.read()
    return content, file_format


def parse(content, data_format):
    if data_format == '.json':
        dictionary = json.loads(content)
    if data_format in ('.yaml', '.yml'):
        dictionary = yaml.load(content, Loader=yaml.FullLoader)
    return dictionary
