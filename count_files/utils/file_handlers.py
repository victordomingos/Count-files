#!/usr/bin/env python3
# encoding: utf-8
import os
from itertools import chain

from count_files.settings import SUPPORTED_TYPES


def get_file_extension(filepath: str, case_sensitive: bool = False) -> str:
    """Extract only the file extension from a given path.

    Behavior:
    select2.3805311d5fc1.css.gz -> gz, .gitignore -> '.'
    Pipfile -> '.', .hidden_file.txt -> txt
    Used in platforms.py and file_preview.py
    :param filepath: full/path/to/file or filename
    :param case_sensitive: False -> ignore case in extensions,
    True -> distinguish case variations in extensions
    :return: extension name (txt, py) or '.' (for files without extension).
    If case_sensitive==False, return in uppercase.
    """
    extension = os.path.splitext(filepath)[1][1:]
    if extension:
        if case_sensitive:
            return extension
        else:
            return extension.upper()
    else:
        return '.'


def is_supported_filetype(extension: str) -> bool:
    """Return a True if the given file extension has a supported file preview.

    :param extension: extension name (txt, py), '.'(without extension) or '..' (all extensions)
    :return: True if we have a preview procedure for the given file type, False otherwise.
    """
    return extension in list(chain.from_iterable(SUPPORTED_TYPES.values()))
