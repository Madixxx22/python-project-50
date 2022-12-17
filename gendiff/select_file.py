import json
import yaml
from gendiff import generate_diff


def file_format_selection(first_path_file: str,
                          second_path_file: str,
                          format: str) -> str:
    format_f = first_path_file.split('.')[1]
    format_s = second_path_file.split('.')[1]
    with open(first_path_file, encoding='utf8') as ff:
        with open(second_path_file, encoding='utf8') as sf:
            if format_f in ("json") and format_s in ("json"):
                first_file = json.load(ff)
                second_file = json.load(sf)
                return generate_diff(first_file=first_file,
                                     second_file=second_file,
                                     format=format)
            elif format_f in ("yaml", "yml") and format_s in ("yaml", "yml"):
                first_file = yaml.safe_load(ff)
                second_file = yaml.safe_load(sf)
                return generate_diff(first_file=first_file,
                                     second_file=second_file,
                                     format=format)
            elif format_f not in ("json", "yaml", "yml") or \
                    format_s not in ("json", "yaml", "yml"):
                raise ValueError(f"{format_f} - format not supported")
            return ""
