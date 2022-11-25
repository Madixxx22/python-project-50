import json


# Function description the logic of finding difference in flat json files
def generate_diff(first_file: dict, second_file: dict) -> str:
    res_dict = {}
    for key, value in first_file.items():
        if key in second_file and first_file[key] == second_file[key]:
            res_dict.update({f'  {key}': value})
        else:
            res_dict.update({f'- {key}': value})
    for key, value in second_file.items():
        if key in first_file and first_file[key] != second_file[key]:
            res_dict.update({f'+ {key}': value})
        elif key not in first_file:
            res_dict.update({f'+ {key}': value})

    sort_key = sorted(res_dict, key=lambda x: x[2])
    result = {k: res_dict[k] for k in sort_key}
    return json.dumps(result, indent=2).replace('"', '').replace(',', '')
