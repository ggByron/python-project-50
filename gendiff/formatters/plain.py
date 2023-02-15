def convert(item):
    result = ''
    if isinstance(item, dict):
        result = "[complex value]"
    elif item is None:
        result = 'null'
    elif isinstance(item, bool):
        result = f"{str(item).lower()}"
    else:
        result = f"'{str(item)}'"
    return result


def build_plain(data, key=''):
    result = []
    for item in data:
        path = f"{key}{item.get('key')}"
        if item['action'] == 'nested':
            result.append(build_plain(item['children'], f"{path}."))
        elif item['action'] == 'deleted':
            result.append(f"Property '{path}' was removed")
        elif item['action'] == 'added':
            result.append(f"Property '{path}' was added with value: "
                          f"{convert(item['val'])}")
        elif item['action'] == 'changed':
            result.append(
                f"Property '{path}' was updated. "
                f"From {convert(item['old'])} to {convert(item['new'])}")

    return '\n'.join(result)


def plain(data):
    return build_plain(data)
