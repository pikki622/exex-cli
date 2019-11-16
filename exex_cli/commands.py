import cleo


class ExtractCommand(cleo.Command):
    """
    Extract data from Excel document.

    extract
        {filename : Source file path}
        {sheet? : Name or index of sheet}
        {selection? : Selection}
        {format? : text, json, xml, csv}
    """

    def handle(self):
        filename = self.argument("filename")

        if not filename:
            self.info("FAIL")
            return

        self.info(filename)

        return
