#!/usr/bin/env python3
# encoding: utf-8
import ctypes
import os
import sys

from pathlib import Path
from typing import Iterable
from collections import Counter
from itertools import chain

from countfiles.settings import SUPPORTED_TYPES, TERM_WIDTH


def get_file_extension(filepath: str) -> str:
    """Extract only the file extension from a given path.

    Behavior:
    select2.3805311d5fc1.css.gz -> gz, .gitignore -> '.'
    Pipfile -> '.', .hidden_file.txt -> txt
    :param filepath: full/path/to/file
    :return: extension name (txt, py) or '.' (for files without extension)
    """
    extension = os.path.splitext(filepath)[1][1:]
    if extension:
        return extension
    else:
        return '.'


def is_supported_filetype(extension: str) -> bool:
    """
    Return a True if the given file extension has a supported file preview

    :param extension:
    :return: True if we have a preview procedure for the given file type, False otherwise.
    """
    return extension in list(chain.from_iterable(SUPPORTED_TYPES.values()))


def human_mem_size(num: int, suffix='B') -> str:
    """Return a human readable memory size in a string.

    Initially written by Fred Cirera, modified and shared by Sridhar Ratnakumar
    (https://stackoverflow.com/a/1094933/6167478), edited by Victor Domingos.
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num = num / 1024.0

    return "%.1f%s%s" % (num, 'Yi', suffix)


def search_files(dirpath: str, extension: str, recursive: bool, include_hidden: bool) -> Iterable[str]:
    """Find all files in a given directory with and without the extension.

    :param dirpath: full/path/to/folder
    :param extension: extension name (txt, py) or '' (default all extensions)
    :param recursive: True or False
    :param include_hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: object <class 'generator'>
    """

    # this part used in def get_files_by_extension
    if extension:
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                f_path = os.path.join(root, f)
                f_extension = get_file_extension(f_path)
                if f_extension != extension or not os.path.isfile(f_path):
                    continue
                if include_hidden or not is_hidden_file_or_dir(f_path):
                    yield f_path
            if not recursive:
                break
    # in fact this part do the same as def count_files_by_extension(except counters) if it called
    # directly -> search_files('full/path/to/folder', '', recursive=True, include_hidden=True)
    # in the current structure of the parser is not used
    # (two functions: one for searching (-fe) and one for counting)
    else:
        if not recursive:
            with os.scandir(dirpath) as directory:
                for f in directory:
                    f_path = os.path.join(dirpath, f)
                    if not f.is_file():
                        continue
                    if include_hidden or not is_hidden_file_or_dir(f_path):
                        yield f_path

        else:
            for root, dirs, files in os.walk(dirpath):
                for f in files:
                    f_path = os.path.join(root, f)
                    if not os.path.isfile(f_path):
                        continue
                    if include_hidden or not is_hidden_file_or_dir(f_path):
                        yield f_path


def count_files_by_extension(dirpath: str, recursive=False, include_hidden=True):
    """ Count all files in a given directory by their extensions.

    :param recursive: True or False
    :param dirpath: full/path/to/folder
    :param include_hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: Counter() with extensions (keys: str)and their frequencies (values: int)
    """
    counters = Counter()
    dirpath = os.path.expanduser(dirpath)

    def count_file_extensions(files):
        for f in files:
            extension = get_file_extension(f)
            if extension == '.':
                extension = '[no extension]'
            counters[extension] += 1
            print("\r"+os.path.basename(f)[:TERM_WIDTH-1].ljust(TERM_WIDTH-1), end="")

    if recursive:
        if include_hidden:
            for root, dirs, files in os.walk(dirpath):
                count_file_extensions(files)
        else:
            for root, dirs, files in os.walk(dirpath):
                only_these = [f for f in files
                              if not is_hidden_file_or_dir(os.path.join(root, f))]
                count_file_extensions(only_these)
    else:
        with os.scandir(dirpath) as directory:
            # if True return all files
            if include_hidden:
                only_these = [f for f in directory if f.is_file()]
            else:
                only_these = [f for f in directory if f.is_file()
                              and not is_hidden_file_or_dir(os.path.join(dirpath, f))]
            count_file_extensions(only_these)
    
    print("\r".ljust(TERM_WIDTH-1)) # Clean the feedback text before proceeding.
    return counters


def is_hidden_file_or_dir(filepath: str) -> bool:
    """The function determines whether the file or folder in filepath is hidden.

    Windows: testing the FILE_ATTRIBUTE_HIDDEN for file or folder.
    Note: if any parent folders of filepath is hidden
    def is_hidden_file_or_dir return True, even if it has visible final file/folder.
    If parent folders not hidden, but final file/folder is hidden also return True.
    (discussion: https://stackoverflow.com/questions/284115/cross-platform-hidden-file-detection)

    Linux: testing at least for the dot character in path on Unix-like systems.
    Note: for Linux def is_hidden_file_or_dir('~/path/.to/file.txt') checking for the dot character in path,
    so if '/.' in path the entire folder is ignored, even if it has visible files.

    :param filepath: full/path/to/file.txt or full/path/to_folder
    :return: True if hidden or False if not
    """
    platform_name = sys.platform
    filepath = os.path.normpath(filepath)
    if platform_name.startswith('win'):
        # list with full paths of all parents in filepath except drive
        list_for_check = list(Path(filepath).parents)[:-1]
        list_for_check.append(Path(filepath))
        response = []
        for some_path in list_for_check:
            try:
                attrs = ctypes.windll.kernel32.GetFileAttributesW(str(some_path))
                assert attrs != -1
                result = bool(attrs & 2)
            except (AttributeError, AssertionError):
                result = False
            response.append(result)
        if any(response):
            return True
        return False
    elif platform_name.startswith('linux'):
        return bool('/.' in filepath)
    elif platform_name.startswith('darwin'):
        return bool('/.' in filepath)
