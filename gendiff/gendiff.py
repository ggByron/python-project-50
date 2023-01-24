import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1, 'r'))
    data2 = json.load(open(file_path2, 'r'))
    keys = data1.keys() | data2.keys()
    result = ''
    for key in sorted(keys):
        if key not in data2:
            result += f'\n- {key}: {data1[key]}'
        elif key not in data1:
            result += f'\n+ {key}: {data2[key]}'
        elif data1[key] == data2[key]:
            result += f'\n{key}: {data2[key]}'
        elif data1[key] != data2[key]:
            result += f'\n- {key}: {data1[key]}'
            result += f'\n+ {key}: {data2[key]}'
    return result