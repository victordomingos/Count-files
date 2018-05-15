#!/usr/bin/env python3

import os
import stat
from pathlib import Path
from typing import List

try:
    import ctypes
except:
    pass

def get_file_extension(filepath: str) -> str:
    """Extract only the file extension from a given path.

    If the file name does not have an extension, return '[no extension]'.
    Behavior:
    select2.3805311d5fc1.css.gz -> gz, .gitignore -> [no extension]
    Pipfile -> [no extension], .hidden_file.txt -> txt
    """
    extension = os.path.splitext(filepath)[1][1:]
    if extension:
        return extension
    else:
        return '[no extension]'


def has_extension(filepath) -> bool:
    """Check if a filename has an extension.

    Behavior:
    select2.3805311d5fc1.css.gz -> True, .gitignore -> False
    Pipfile -> False, .hidden_file.txt -> True
    """
    if not os.path.splitext(filepath)[1]:
        return False
    else:
        return True


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


def _has_hidden_attribute(filepath):
    """
    Adapted from Jason R. Coombs (https://stackoverflow.com/a/6365265/6167478)
    """
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(filepath)
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result


def is_hidden(filepath: str) -> bool:
    """ Check if the given path (file or directory) is hidden """
    # TODO: adapt this for both windows and Unix.
    # TODO: adapt for Pythonista/iOS and test.
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or _has_hidden_attribute(filepath)


def get_files_without_extension(path: str, recursive=False, include_hidden=True):
    """Find all files in a given directory that have no extension.

    By default, this function does not recurse through subdirectories.
    :param recursive:
    :param path:
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
                    if f.is_file() and not has_extension(f)]
        else:
            return [f for f in Path(os.path.expanduser(path)).rglob("*")
                    if f.is_file() and not is_hidden(f) and not has_extension(f)]
    else:
        if include_hidden:
            return [f for f in Path(path).iterdir()
                    if f.is_file() and not has_extension(f)]
        else:
            return [f for f in Path(path).iterdir()
                    if f.is_file() and not is_hidden(f) and not has_extension(f)]


def is_hidden_file_or_dir(platform_name: str, filepath: str) -> bool:
    """The function determines whether the file or folder is hidden.

    Windows: testing the FILE_ATTRIBUTE_HIDDEN for file or folder
    (source: https://stackoverflow.com/questions/284115/cross-platform-hidden-file-detection)
    Linux: testing at least for the dot character in path on Unix-like systems
    Note: for Linux def is_hidden_file_or_dir('~/path/.to/file.txt') checking for the dot character in path,
    so if '/.' in path the entire folder is ignored, even if it has visible files.
    For Windows def is_hidden_file_or_dir('~/path/to/file.txt')
    checking only file. For checking folder - def is_hidden_file_or_dir('~/path/to_folder')
    :param platform_name: result of a 'sys.platform' parameter call
    :param filepath: ~/path/to/file.txt or ~/path/to_folder
    :return: True if hidden or False if not
    """
    filepath = os.path.normpath(filepath)
    if platform_name.startswith('win'):
        return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
    elif platform_name.startswith('linux'):
        return bool('/.' in filepath)
    elif platform_name.startswith('darwin'):
        return bool('/.' in filepath)

# TODO: add checking for hidden folder in Windows to skip it.
def non_recursive_search(location: str, platform_name: str, hidden: bool) -> List[str]:
    """Non recursive search for files in folder.

    :param location: ~/path/to_folder
    :param platform_name: result of a 'sys.platform' parameter call
    :param hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: list with filenames
    """
    with os.scandir(location) as directory:
        # if True return all files
        if hidden:
            result = [f for f in directory if f.is_file()]
        else:
            result = [f for f in directory if f.is_file()
                      and not is_hidden_file_or_dir(platform_name, os.path.join(location, f))]
    return result


def recursive_search(location: str, platform_name: str, hidden: bool) -> List[str]:
    """Recursive search for files in folder and subfolders.

    :param location: ~/path/to_folder
    :param platform_name: result of a 'sys.platform' parameter call
    :param hidden: False -> exclude hidden, True -> include hidden, counting all files
    :return: list with filenames
    """
    if hidden:
        result = []
        for root, dirs, files in os.walk(location):
            result.extend(files)
    else:
        result = []
        for root, dirs, files in os.walk(location):
            result.extend([f for f in files
                           if not is_hidden_file_or_dir(platform_name, os.path.join(root, f))])
    return result


