from parser import parse


def generate_diff(file_path1, file_path2):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    keys = data1.keys() | data2.keys()
    result = ''
    new_line = '\n'
    for key in sorted(keys):
        if key not in data2:
            result += f'- {key}: {data1[key]}{new_line}'
        elif key not in data1:
            result += f'+ {key}: {data2[key]}{new_line}'
        elif data1[key] == data2[key]:
            result += f'{key}: {data2[key]}{new_line}'
        elif data1[key] != data2[key]:
            result += f'- {key}: {data1[key]}{new_line}'
            result += f'+ {key}: {data2[key]}{new_line}'
    return result[:-1]
