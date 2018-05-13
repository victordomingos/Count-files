import os
from pathlib import Path


def get_file_extension(file_path: str) -> str:
    """Extract only the file extension from a given path.

    If the file name does not have an extension, return '[no extension]'.
    Behavior:
    select2.3805311d5fc1.css.gz -> gz, .gitignore -> [no extension]
    Pipfile -> [no extension], .hidden_file.txt -> txt
    """
    extension = os.path.splitext(file_path)[1][1:]
    if extension:
        return extension
    else:
        return '[no extension]'


def has_extension(path) -> bool:
    """Check if a filename has an extension.

    Behavior:
    select2.3805311d5fc1.css.gz -> True, .gitignore -> False
    Pipfile -> False, .hidden_file.txt -> True
    """
    if not os.path.splitext(path)[1]:
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


def is_hidden(path):
    """ Check if the given path is hidden """
    #TODO
    pass


def get_files_without_extension(path: str, recursive=False):
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
        return [f for f in Path(os.path.expanduser(path)).rglob("*")
                if f.is_file() and not has_extension(f)]
    else:
        return [f for f in Path(path).iterdir()
                if f.is_file() and not has_extension(f)]
