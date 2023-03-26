import json as build_json


INDENT = 4


def json(data):
    return build_json.dumps(data, indent=INDENT)
