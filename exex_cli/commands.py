import json

import cleo
from exex import parse
from openpyxl import load_workbook

from exex_cli import formats


class ExtractCommand(cleo.Command):
    """
    Extract data from Excel document.

    extract
        {filename : Source file path}
        {--s|sheet=0 : Name of sheet}
        {--r|range=all : Range}
        {--f|format=text : text, table, json, csv}
        {--d|delimiter=, : Delimiter in output}
    """

    def handle(self):
        # file
        arg_filename = self.argument("filename")
        book = load_workbook(arg_filename)

        # sheet
        arg_sheet = self.option("sheet")

        if arg_sheet == "0":
            arg_sheet = book.sheetnames[0]

        sheet = book[arg_sheet]

        # values
        arg_range = self.option("range")

        if arg_range == "all":
            values_raw = sheet.values
        else:
            values_raw = sheet[arg_range]

        values_parsed = parse.values(values_raw)

        # format
        arg_format = self.option("format")

        self.info("\n")
        self.__render(values_parsed, arg_format)
        self.info("\n")

        return

    def __render(self, values, format_=formats.TEXT):
        if format_ == formats.TEXT:
            self.info(values)
        elif format_ == formats.CSV:
            delimiter = self.option("delimiter")
            values_as_csv = "\n".join([delimiter.join(r) for r in values])
            self.info(values_as_csv)
        elif format_ == formats.TABLE:
            self.render_table(headers=values[0], rows=values[1:])
        elif format_ == formats.JSON:
            self.info(json.dumps(values, indent=2))
        else:
            self.info(values)
