#!/usr/bin/env python3
# encoding: utf-8
from pathlib import Path

from count_files.utils.file_handlers import get_file_extension
from count_files.settings import SUPPORTED_TYPES


def generic_text_preview(filepath: str, max_size: int) -> str:
    """Read the first characters of the file and return a string.

    :param filepath: a string containing the path to the file
    :param max_size: max number of characters to be read from file
    :return: a string with the text preview or error message
    """
    try:
        p = Path(filepath)
        with p.open(mode='r') as f:
            return str(f.read(max_size)).replace('\n', ' ')
    except Exception as e:
        # DEBUG OSError
        return f"TEXT_PREVIEW_ERROR: {e}"


# TODO: build a better preview system for binaries
def generic_binary_preview(filepath: str, max_size: int) -> bytes or str:
    """ Read the first characters of the file and return a string

    :param filepath: a string containing the path to the file
    :param max_size: max number of characters to be read from file
    :return: a string with the text preview (without newline characters)
    """
    p = Path(filepath)
    try:
        with p.open(mode='rb') as f:
            return f.read(max_size)
    except Exception as e:
        print("BINARY_PREVIEW_ERROR", e) # DEBUG
        return ""


def generate_preview(filepath: str, max_size: int = 390) -> str:
    """Generate a human readable text preview.

    For text files, the preview will be the first `max_size` characters.
    For other file types the preview is not implemented.
    :param filepath: full/path/to/file (with extension or without it)
    :param max_size:
    For CLI.
    The number of characters for viewing by default depends on the terminal width settings
    and can be changed with the -ps or -preview-size argument.
    :return: a string with the text preview (without newline characters).
    If the preview is not available for the file, it returns an information message.
    """
    extension = get_file_extension(filepath, case_sensitive=False).lower()

    if extension in SUPPORTED_TYPES['text']:
        excerpt = generic_text_preview(filepath, max_size)
        if excerpt:
            # return excerpt or error string
            return f"{excerpt}"
        else:
            return "[This file can be empty.]"
    else:
        # skip the extension if it is not supported
        return "[A preview of this file type is not yet implemented.]"


