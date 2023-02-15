INDENT = 4


def stringify(data, replacer=' ', depth=1):
    step = depth

    def walk(data, replacer, depth):
        result = ''
        if not isinstance(data, dict):
            return str(data)
        for key, val in data.items():
            if isinstance(val, dict):
                val = walk(val, replacer, depth + step)
            result += f"{replacer * (depth + step)}{key}: {val}\n"
        result = '{' + '\n' + result
        result += replacer * depth + '}'
        return result
    return walk(data, replacer, depth)


def build_stylish(data, depth=0):
    result = []
    for item in data:
        if item['action'] == 'nested':
            result.append(
                f"    {item['key']}: {'{'}\n"
                f"{build_stylish(item['children'], INDENT)}\n"
                f"    {'}'}"
            )
        elif item['action'] == 'deleted':
            result.append(
                f"  - {item['key']}: "
                f"{stringify(item['val'], ' ', INDENT)}"
            )
        elif item['action'] == 'added':
            result.append(
                f"  + {item['key']}: "
                f"{stringify(item['val'], ' ', INDENT)}"
            )
        elif item['action'] == 'unchanged':
            result.append(
                f"    {item['key']}: "
                f"{stringify(item['val'], ' ', INDENT)}"
            )
        elif item['action'] == 'changed':
            result.append(
                f"  - {item['key']}: "
                f"{stringify(item['old'], ' ', INDENT)}"
            )
            result.append(
                f"  + {item['key']}: "
                f"{stringify(item['new'], ' ', INDENT)}"
            )

    return '\n'.join(result)


def stylish(data):
    return '{\n' + build_stylish(data) + '\n}'
