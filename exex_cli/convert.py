from exex_cli.util import array_dimensions

import json


def to_csv(values, delimiter=",", line_separator="\n"):
    width, height = array_dimensions(values)

    if width == 0 and height == 0:
        return values
    elif height == 0:
        return line_separator.join(values)
    else:
        return line_separator.join(delimiter.join(r) for r in values)


def to_json(values):
    return json.dumps(values, indent=2)
