def json(data):

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
