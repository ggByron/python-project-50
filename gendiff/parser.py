import json
import yaml


def parse(file_path):
    if file_path1[-4].lower() == 'json':
        data = json.load(open(file_path, 'r'))
        return data
    elif file_path1[-3].lower() == 'yml' or file_path1[-4].lower() == 'yaml':
        data = yaml.load(open(file_path, 'r'))
        return data