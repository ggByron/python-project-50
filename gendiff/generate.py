from gendiff.parser import parse, read
from gendiff.formatters.formatters import FORMATS


def build_diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = []
    for key in sorted(keys):
        if key not in dict2:
            result.append(
                {
                    'key': key,
                    'action': 'deleted',
                    'val': dict1[key],
                }
            )
        elif key not in dict1:
            result.append(
                {
                    'key': key,
                    'action': 'added',
                    'val': dict2[key],
                }
            )
        elif dict1[key] == dict2[key]:
            result.append(
                {
                    'key': key,
                    'action': 'unchanged',
                    'val': dict1[key],
                }
            )
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result.append(
                {
                    'key': key,
                    'action': 'nested',
                    'children': build_diff(dict1[key], dict2[key]),
                }
            )
        else:
            result.append(
                {
                    'key': key,
                    'action': 'changed',
                    'old': dict1[key],
                    'new': dict2[key],
                }
            )
    return result


def generate_diff(file_path1, file_path2, format='stylish'):
    file_content1, file_format1 = read(file_path1)
    file_content2, file_format2 = read(file_path2)
    dict1 = parse(file_content1, file_format1)
    dict2 = parse(file_content2, file_format2)
    return FORMATS[format](build_diff(dict1, dict2))
