from typing import Any


def form(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return str(value)
    return f"'{str(value)}'"


def get_child(item: Any) -> Any:
    if isinstance(item, dict):
        return item["children"]
    return item


def to_plain(data: dict, path: str = "") -> str:
    plain_data = []
    data = get_child(data)
    for item in data:
        new_path = path + str(item["key"])
        status = item["status"]
        if status == "added":
            plain_data.append(f"Property '{new_path}' was added with "
                              f"value: {form(value=item['new'])}")
        elif status == "delete":
            plain_data.append(f"Property '{new_path}' was removed")
        elif status == "changed":
            plain_data.append(f"Property '{new_path}' was updated. "
                              f"From {form(value=item['old'])} "
                              f"to {form(value=item['new'])}")
        elif status == "nested":
            plain_data.append(to_plain(get_child(item), path=f"{new_path}."))

    return "\n".join(plain_data)
