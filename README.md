# Python Package Starter
[![Build Status](https://travis-ci.org/vikpe/python-package-starter.svg?branch=master)](https://travis-ci.org/vikpe/python-package-starter) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Features
* Multi-version support ([pyenv](https://github.com/pyenv/pyenv), [tox](https://github.com/tox-dev/tox/))
* Single config using the new standardized `pyproject.toml` ([PEP518](https://www.python.org/dev/peps/pep-0518/))
* Simple build/publish/dependency management using [poetry](https://github.com/sdispater/poetry)
* Continous integration ([Travis CI](https://travis-ci.org/))
* Code formatting ([black](https://github.com/psf/black))

## Prerequisites
* [pyenv](https://github.com/pyenv/pyenv)
* [poetry](https://github.com/sdispater/poetry)

## Installation
1. Install the Python versions you want to support using pyenv.
2. Clone repo: `git clone git@github.com:vikpe/python-package-starter.git [PACKAGE_NAME]` 
3. `cd [PACKAGE NAME]`
4. Create a virtual env: `pyenv virtualenv [package abbreviation][python version]` (eg. `foo38` for Python 3.8)
5. Activate virtual env: `pyenv activate foo38`
6. Install dependencies: `poetry install`
7. Edit `pyproject.toml`, update project name, description and author and any other settings you like.

## Usage

Command | Description
--- | ---
`poetry add [package]` | Add package to dependencies.
`poetry add -D [package]` | Add package to dev dependencies.
`poetry run pytest` | Run tests in local Python version.
`poetry run tox` | Run tests in all Python versions defined in `tox.ini`.
`poetry run black .` | Run black code formatter.
`poetry build` | Build sdist and wheel to `/dist`.
`poetry publish` | Publish package to PyPi.

## Continous integration

### Travis CI
Login to [Travis CI](https://travis-ci.org/) and connect your repo. Travis will automatically run tests whenever there is a commit.

### Code coverage
[todo]
