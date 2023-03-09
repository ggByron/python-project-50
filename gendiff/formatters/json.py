def build_json(data):

    def walk(data):
        result = ''
        if not isinstance(data, dict):
            return str(data)
        for key, val in data.items():
            if isinstance(val, dict):
                val = walk(val)
            result += f"{key}: {val}"
        result = '[' + result + ']'
        return result
    return walk(data)


def quote_normalizer(data):
    result = ''
    for _ in data:
        if _ != "'":
            result += _
        else:
            result += '"'
    return result


def json(data):
    return quote_normalizer(build_json(data))
