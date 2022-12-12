from typing import Any


def get_child(item: Any) -> Any:
    if isinstance(item, dict):
        return item["children"]
    return item


def build_item(status_item: str) -> str:
    status = {'added': '  + ',
              'delete': '  - ',
              'unchanged': '    ',
              'nested': '    ',
              'changed': '  + '
              }
    return status[status_item]


STARTING_INDENT = 4


def nested(value, depth):
    if isinstance(value, dict):
        lines = ["{"]
        for key, nest_val in value.items():
            if isinstance(nest_val, dict):
                new_value = nested(nest_val, depth + STARTING_INDENT)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {nest_val}")
        lines.append(f'{" " * depth}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return value


def form(dict, key, depth, sign):
    return f"{' ' * depth}{sign}{dict['key']}:" \
           f" {nested(dict[key], depth + STARTING_INDENT)}"


def to_stylish(diff, depth=0):
    lines = ['{']
    diff = get_child(diff)
    for item in diff:
        status = item['status']
        if status == "unchanged":
            lines.append(form(
                item, 'value',
                depth, build_item('unchanged')
            ))

        if status == "added":
            lines.append(form(
                item, "new",
                depth, build_item('added')
            ))

        if status == "delete" or status == "changed":
            lines.append(form(
                item, "old",
                depth, build_item('delete')
            ))

        if status == "changed":
            lines.append(form(
                item, "new",
                depth, build_item('added')
            ))

        if status == "nested":
            children = item["children"]
            lines.append(f"{' ' * depth}    {item['key']}:"
                         f" {to_stylish(children, depth + STARTING_INDENT)}")

    lines.append(f'{" " * depth}}}')
    return "\n".join(lines)
