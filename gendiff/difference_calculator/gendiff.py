from typing import Any
from gendiff.formatter.formatter import formatting


def is_child(data_dict: Any) -> bool:
    if isinstance(data_dict, dict):
        return True
    else:
        return False


# Functon description the logic of finding difference
def gendiff_engine(first_file: dict, second_file: dict) -> dict:
    def diff(first: dict, second: dict) -> list:
        diff_list = []
        merge_list_keys = sorted(list(first | second))
        for key in merge_list_keys:
            if key not in first:
                diff_list.append({'key': key,
                                  'new': second[key],
                                  'status': 'added'})
            elif key not in second:
                diff_list.append({'key': key,
                                  'old': first[key],
                                  'status': 'delete'})
            elif is_child(first[key]) and is_child(second[key]):
                child = diff(first[key], second[key])
                diff_list.append({'key': key,
                                  'status': 'nested',
                                  'children': child})
            elif first[key] == second[key]:
                diff_list.append({'key': key,
                                  'value': first[key],
                                  'status': "unchanged"})
            elif first[key] != second[key]:
                diff_list.append({"key": key,
                                  'old': first[key],
                                  'new': second[key],
                                  'status': "changed"})
        return diff_list
    res = diff(first=first_file, second=second_file)
    return dict(type='root', children=res)


# Function description the logic of finding difference in flat json files
def generate_diff(first_file: dict, second_file: dict,
                  format: str = "stylish") -> str:
    data_diff = gendiff_engine(first_file, second_file)
    result = formatting(data_diff=data_diff, format=format)
    return result
