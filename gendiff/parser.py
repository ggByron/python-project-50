import os
import json
import yaml


def get_format(file_path):
    return os.path.splitext(file_path)[1]


def parse(content, file_format):
    with open(content, 'r') as file:
        if file_format == '.json':
            dictionary = json.load(file)
        if file_format in ('.yaml', '.yml'):
            dictionary = yaml.load(file, Loader=yaml.FullLoader)
    return dictionary
