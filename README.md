# exex-cli [![Build Status](https://travis-ci.org/vikpe/exex-cli.svg?branch=master)](https://travis-ci.org/vikpe/exex-cli) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
> Command-line interface for extracting data from Excel documents.

## Installation
```sh
pip install exex-cli
```

## Usage
### Synopsis
```bash
exex FILENAME [SHEET] [SELECTION] [--format json|xml|csv] 
```

Parameter | Type | Default | Description
--- | --- | --- | ---
`FILENAME` | string | | Path to .xlsx file. 
`[SHEET]` | string or int | `0` (first sheet) | Name or index of sheet
`[SELECTION]` | selection | `all` (all values) | Selection
`[format]` | string | `text` | `text`, `json`, `xml`, `csv`

**Types of selections**

Type | Syntax | Example
--- | --- | ---
All values | `all` | `all`
Cell by name | `[COLUMN_NAME][ROW_NUMBER]` | `A1`
Cell by index | `[COLUMN_INDEX],[ROW_INDEX]` | `1,1`
Cell range | `[FROM]:[TO]` |  `A1:A3`
Column | `[COLUMN_NAME]` | `A`
Column range | `[FROM]:[TO]` | `A:C`
Row | `[ROW_NUMBER]` | `1`
Row range | `[FROM]:[TO]` | `1:3`

### Examples

**Get all values**
```bash
exex sample.xlsx 
```

**Get all values as JSON**
```bash
exex sample.xlsx --format json 
```

## Development

**Tests** (local Python version)
```sh
poetry run pytest
```

**Tests** (all Python versions defined in `tox.ini`)
```sh
poetry run tox
```

**Code formatting** (black)
```sh
poetry run black .
```
