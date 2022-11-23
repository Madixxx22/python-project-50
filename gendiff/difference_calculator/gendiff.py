import json


def generate_diff(first_file:str, second_file:str) -> str:
    res_dict = {}
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))

    for k, v in file1.items():
        if k in file2 and file1[k] == file2[k]:
            res_dict.update({f'  {k}': v})
        else:
            res_dict.update({f'- {k}': v})


    for k, v in file2.items():
        if k in file1 and file1[k] != file2[k]:
            res_dict.update({f'+ {k}': v})


        elif k not in file1:
            res_dict.update({f'+ {k}': v})

    sort_key = sorted(res_dict, key = lambda x: x[2])
    result = {k: res_dict[k] for k in sort_key}
    return json.dumps(result, indent=4)