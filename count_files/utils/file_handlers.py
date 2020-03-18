#!/usr/bin/env python3
# encoding: utf-8
import os
from itertools import chain
from typing import List, Tuple, Dict

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


def group_ext_by_type(data: List[Tuple[str, int]],
                      ext_and_group: Dict[str, str]) -> Dict[str, List[Tuple[str, int]]]:
    """Group file extensions by type.

    Default ext_and_group:
    archives, audio, audio/video, data, documents, executables, fonts, images,
    Python related extensions, videos, and other files.
    User-defined ext_and_group:
    may be created from configuration file.
    Initial storage: dict with items like {'documents': [], 'images': [], ...}
    key - group name, value - empty list.
    'other': reserved key.
    :param data: list with items like [('png', 8), ('txt', 25), ...]
    :param ext_and_group: dict with items like {'png': 'image', 'txt': documents, ...}
    :return: sorted dict with items like {'documents': [('txt', 25), ...], 'images': [('png', 8), ...], ...}
    """
    # storage: Dict[str, list]
    # local scope important
    storage = dict.fromkeys(sorted(set(ext_and_group.values())), [])
    other = []
    for (ext, freq) in data:
        item_type = ext_and_group.get(ext.lower(), 'other')
        if item_type == 'other':
            other.append((ext, freq))
        else:
            if storage.get(item_type):
                storage[item_type].append((ext, freq))
            else:
                storage[item_type] = [(ext, freq)]
    if other:
        storage.update({'other': other})
    return storage
