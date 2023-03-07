def convert(data):
    if data is None:
        return 'null'
    elif isinstance(data, bool):
        return f"{str(data).lower()}"
    elif isinstance(data, dict):
        return '[complex value]'
    return f"'{str(data)}'"


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
