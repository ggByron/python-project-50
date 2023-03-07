INDENT = 4
ACTION = {'added': ' + ', 'deleted': ' - ', 'unchanged': '   '}


def convert_to_str(data):
    if data is None:
        return 'null'
    elif isinstance(data, bool):
        return f"{str(data).lower()}"
    return str(data)


def stringify(data, replacer=' ', depth=1):
    step = depth

    def walk(data, replacer, depth):
        result = ''
        if not isinstance(data, dict):
            return convert_to_str(data)
        for key, val in data.items():
            if isinstance(val, dict):
                val = walk(val, replacer, depth + step)
            result += f"{INDENT * ' '}{replacer * depth}{key}: {val}\n"
        result = '{' + '\n' + result
        result += replacer * depth + '}'
        return result
    return walk(data, replacer, depth)


def build_key_str(depth, action, key):
    indent = (depth + INDENT - len(action)) * ' '
    return f"{indent}{action}{key}: "


def build_stylish(data, depth=0):
    result = []
    for item in data:
        if item['action'] == 'nested':
            result.append(
                f"{build_key_str(depth, ACTION['unchanged'], item['key'])}"
                f"{'{'}\n"
                f"{build_stylish(item['children'], depth + INDENT)}\n"
                f"{(depth + INDENT) * ' ' + '}'}"
            )
        elif item['action'] in ACTION:
            action = item['action']
            result.append(
                f"{build_key_str(depth, ACTION[action], item['key'])}"
                f"{stringify(item['val'], ' ', depth + INDENT)}"
            )
        elif item['action'] == 'changed':
            result.append(
                f"{build_key_str(depth, ACTION['deleted'], item['key'])}"
                f"{stringify(item['old'], ' ', depth + INDENT)}"
            )
            result.append(
                f"{build_key_str(depth, ACTION['added'], item['key'])}"
                f"{stringify(item['new'], ' ', depth + INDENT)}"
            )

    return '\n'.join(result)


def stylish(data):
    return '{\n' + build_stylish(data) + '\n}'
