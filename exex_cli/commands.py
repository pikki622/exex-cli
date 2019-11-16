import cleo
from exex import parse
from exex_cli import formats
from openpyxl import load_workbook


class ExtractCommand(cleo.Command):
    """
    Extract data from Excel document.

    extract
        {filename : Source file path}
        {--s|sheet=0 : Name of sheet}
        {--r|range=all : Range}
        {--f|format=text : text, table, json, csv}
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

        if arg_format == formats.TEXT:
            self.info('you want it as text')
        elif arg_format == formats.CSV:
            self.info('you want it as csv')
        elif arg_format == formats.JSON:
            self.info('you want it as json')
        elif arg_format == formats.JSONL:
            self.info('you want it as json lines')

        print(values_parsed)

        return
