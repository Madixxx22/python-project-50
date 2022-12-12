from gendiff.formatter.stylish import to_stylish
from gendiff.formatter.json import to_json
from gendiff.formatter.plain import to_plain


def formatting(data_diff: list, format: str):
    if format == 'stylish':
        result = to_stylish(data_diff)
    elif format == 'json':
        result = to_json(data_diff)
    elif format == 'plain':
        result = to_plain(data_diff)
    return result
