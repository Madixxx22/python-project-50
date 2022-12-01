import json
import yaml
from gendiff.difference_calculator.gendiff import generate_diff_json
from gendiff.difference_calculator.gendiff import generate_diff_yml


def file_format_selection(first_path_file: str, second_path_file: str) -> str:
    with open(first_path_file, encoding='utf8') as ff:
        with open(second_path_file, encoding='utf8') as sf:
            if ".json" in first_path_file and ".json" in second_path_file:
                first_file = json.load(ff)
                second_file = json.load(sf)
                return generate_diff_json(first_file=first_file,
                                          second_file=second_file)
            elif ".yaml" in first_path_file and ".yaml" in second_path_file:
                first_file = yaml.safe_load(ff)
                second_file = yaml.safe_load(sf)
                return generate_diff_yml(first_file=first_file,
                                         second_file=second_file)
            elif ".yml" in first_path_file and ".yml" in second_path_file:
                first_file = yaml.safe_load(ff)
                second_file = yaml.safe_load(sf)
                return generate_diff_yml(first_file=first_file,
                                         second_file=second_file)
