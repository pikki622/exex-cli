import cleo


class ExtractCommand(cleo.Command):
    """
    Extract data from Excel document.

    extract
        {file : Source file path}
        {range? : Range}
        {format? : Format (json, jsonl, xml)}
        {skip_rows? : Number of rows to skip}
        {skip_cols? : Number of cols to skip}
    """

    def handle(self):
        excel_file_path = self.argument("file")

        if not excel_file_path:
            self.info("FAIL")
            return

        if self.argument("format"):
            pass

        ext = extract.Extractor(excel_file_path)
        values = ext.all()

        print(values)
