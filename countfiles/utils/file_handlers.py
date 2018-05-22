#!/usr/bin/env python3

import os
import sys
import ctypes
from pathlib import Path
from typing import List


def get_file_extension(filepath: str) -> str:
    """Extract only the file extension from a given path.

    If the file name does not have an extension, return '' (empty string).
    Behavior:
    select2.3805311d5fc1.css.gz -> gz, .gitignore -> ''
    Pipfile -> '', .hidden_file.txt -> txt
    """
    extension = os.path.splitext(filepath)[1][1:]
    if extension:
        return extension
    else:
        return ''


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


def get_files_without_extension(path: str, recursive=False, include_hidden=True):
    """Find all files in a given directory that have no extension.

    By default, this function does not recurse through subdirectories.
    :param recursive:
    :param path:
    :param include_hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: list with objects
    list example for win: return list with objects <class 'pathlib.WindowsPath'>
    [WindowsPath('C:/.../.gitignore'),
    WindowsPath('C:/.../Pipfile')]
    Special thanks to Natalia Bondarenko (github.com/NataliaBondarenko),
    who submited the initial implementation.
    """
    if recursive:
        if include_hidden:
            return [f for f in Path(os.path.expanduser(path)).rglob("*")
                    if f.is_file() and not get_file_extension(f)]
        else:
            return [f for f in Path(os.path.expanduser(path)).rglob("*")
                    if f.is_file() and not is_hidden_file_or_dir(f) and not get_file_extension(f)]
    else:
        if include_hidden:
            return [f for f in Path(path).iterdir()
                    if f.is_file() and not get_file_extension(f)]
        else:
            return [f for f in Path(path).iterdir()
                    if f.is_file() and not is_hidden_file_or_dir(f) and not get_file_extension(f)]


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


def non_recursive_search(location: str, include_hidden: bool) -> List[str]:
    """Non recursive search for files in folder.

    :param location: ~/path/to_folder
    :param include_hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: list with filenames
    """
    with os.scandir(location) as directory:
        # if True return all files
        if include_hidden:
            result = [f for f in directory if f.is_file()]
        else:
            result = [f for f in directory if f.is_file()
                      and not is_hidden_file_or_dir(os.path.join(location, f))]
    return result


def recursive_search(location: str, include_hidden: bool) -> List[str]:
    """Recursive search for files in folder and subfolders.

    :param location: ~/path/to_folder
    :param include_hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: list with filenames
    """
    if include_hidden:
        result = []
        for root, dirs, files in os.walk(location):
            result.extend(files)
    else:
        result = []
        for root, dirs, files in os.walk(location):
            result.extend([f for f in files
                           if not is_hidden_file_or_dir(os.path.join(root, f))])
    return result


