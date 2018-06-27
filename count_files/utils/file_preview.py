#!/usr/bin/env python3
# encoding: utf-8
import os
import puremagic
import itertools

from pathlib import Path

from count_files.utils.file_handlers import get_file_extension
from count_files.settings import SUPPORTED_TYPES


#TODO
def generic_text_preview(filepath: str, max_size: int) -> str:
    """ Read the first characters of the file and return a string

    :param filepath: a string containing the path to the file
    :param max_size: max number of characters to be read from file
    :return: a string with the text preview
    """
    p = Path(filepath)
    try:
        with p.open(mode='r') as f:
            return str(f.read(max_size)).replace('\n', ' ')
    except Exception as e:
        print("TEXT_PREVIEW_ERROR", e) # DEBUG
        return ""


# TODO: build a better preview system for binaries
def generic_binary_preview(filepath: str, max_size: int) -> str:
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


def generate_preview(filepath: str, max_size=390) -> str:
    """ Detect filetype and generate a human readable text preview

    Detects filetype and returns a string if there is a compatible text
    preview method available. For text files, the preview will be the first
    `max_size` characters. For other file types, a selection of their
    metadata could be shown.
    """
    filetype = ""
    excerpt = ""
    extension = get_file_extension(filepath, case_sensitive=False).lower()


    try:
        my_file = puremagic.magic_file(filepath)
        if my_file:
            filetype = " ".join(str(i) for i in next(itertools.chain(my_file)))
    except Exception as e:
        print("FILETYPE_DETECTION_ERROR:", e) # DEBUG
        pass

    # TODO: Check if there is a specific file preview method
    #print('EXT:', extension) # DEBUG
    #print('TYPE:', filetype) # DEBUG


    if extension in SUPPORTED_TYPES['text']:
        excerpt = generic_text_preview(filepath, max_size)

    elif extension in SUPPORTED_TYPES['image']:
        excerpt = "[Text preview for image files not implemented yet.]"

    elif extension in SUPPORTED_TYPES['pdf']:
        excerpt = "[Text preview for PDF files not implemented yet.]"

    else:
        excerpt = generic_binary_preview(filepath, max_size)


    if excerpt:
        return f"Format: {filetype}\n{excerpt}"
    else:
        return f"Format: {filetype}\n[No preview available for this file.]"
