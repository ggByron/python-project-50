import os
import json
import yaml


def parse(file_path):
    file_format = os.path.splitext(file_path)[1]
    with open(file_path, 'r') as file:
        if file_format == '.json':
            dictionary = json.load(file)
        if file_format in ('.yaml', '.yml'):
            dictionary = yaml.load(file, Loader=yaml.FullLoader)
    return dictionary
