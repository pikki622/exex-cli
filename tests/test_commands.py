import json

from exex_cli.application import application
from exex_cli.commands import ExtractCommand
from cleo import CommandTester

application.add(ExtractCommand())
command = application.find("extract")


# test helpers
def read_file(file_path):
    with open(file_path) as fp:
        return fp.read()


def read_json_file(file_path):
    return json.loads(read_file(file_path))


def get_cmd_output(args):
    tester = CommandTester(command)
    tester.execute(args)
    return tester.io.fetch_output()


# formats
def test_extract():  # default
    expected_output = read_file("tests/expected_output/format_text.txt")
    actual_output = get_cmd_output("tests/files/sample.xlsx")
    assert actual_output == expected_output


def test_extract__format_text():
    expected_output = read_file("tests/expected_output/format_text.txt")
    actual_output = get_cmd_output("tests/files/sample.xlsx --format text")
    assert actual_output == expected_output


def test_extract__format_table():
    expected_output = read_file("tests/expected_output/format_table.txt")
    actual_output = get_cmd_output("tests/files/sample.xlsx --format table")

    assert actual_output == expected_output


def test_extract__format_json():
    expected_output = read_json_file("tests/expected_output/format_json.json")
    actual_output = json.loads(get_cmd_output("tests/files/sample.xlsx --format json"))

    assert actual_output == expected_output


def test_extract__format_csv():
    expected_output = read_file("tests/expected_output/format_csv.csv")
    actual_output = get_cmd_output("tests/files/sample.xlsx --format csv")

    assert actual_output == expected_output


# range
def test_extract__format_json_range():
    expected_output = read_json_file("tests/expected_output/format_json_range.json")
    actual_output = json.loads(
        get_cmd_output("tests/files/sample.xlsx --format json --range A")
    )

    assert actual_output == expected_output
