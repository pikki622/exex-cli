from exex_cli.util import array_dimensions

import json


def to_string(value):
    if value:
        return str(value)
    else:
        return ""


def to_strings(values):
    outer_dim, inner_dim = array_dimensions(values)

    if outer_dim == 0 and inner_dim == 0:
        return to_string(values)
    elif inner_dim == 0:
        return list(map(to_string, values))
    else:
        return [list(map(to_string, row)) for row in values]


def to_csv(values, delimiter=",", line_separator="\n"):
    if not values:
        return ""
    elif not isinstance(values, list):
        return to_strings(values)

    outer_dim, inner_dim = array_dimensions(values)

    if outer_dim == 0 and inner_dim == 0:
        return values
    elif inner_dim == 0:
        return line_separator.join(to_strings(values))
    else:
        return line_separator.join(delimiter.join(to_strings(row)) for row in values)


def to_json(values):
    return json.dumps(values, indent=2)
