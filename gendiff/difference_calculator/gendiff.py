import json
import yaml


# Functon description the logic of finding difference in flat dicts
def generate_diff(first_file: dict, second_file: dict) -> dict:
    res_dict = {}
    for key, value in first_file.items():
        if key in second_file and first_file[key] == second_file[key]:
            res_dict.update({f'    {key}': value})
        else:
            res_dict.update({f'  - {key}': value})
    for key, value in second_file.items():
        if key in first_file and first_file[key] != second_file[key]:
            res_dict.update({f'  + {key}': value})
        elif key not in first_file:
            res_dict.update({f'  + {key}': value})

    sort_key = sorted(res_dict, key=lambda x: x[4])
    return {k: res_dict[k] for k in sort_key}


# Function description the logic of finding difference in flat json files
def generate_diff_json(first_file: dict, second_file: dict) -> str:
    result = generate_diff(first_file, second_file)
    return json.dumps(result, indent=0).replace('"', '').replace(',', '')


# Functon description the logic of finding difference in flat yaml files
def generate_diff_yml(first_file: dict, second_file: dict) -> str:
    result = generate_diff(first_file, second_file)
    if result != {}:
        res = yaml.safe_dump(result, sort_keys=False).replace('"', '')
        return '{\n' + res.replace(',', '').replace('\'', '') + '}'
    else:
        return f'{result}'
