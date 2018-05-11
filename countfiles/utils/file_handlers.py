import os
from pathlib import Path

def get_file_extension(file_path: str) -> str:
    """ Extract only the file extension from a given path.
        If the file name does not have an extension, return '[no extension]'.
    """
    extension = os.path.splitext(file_path)[1][1:]
    if extension:
        return extension
    else:
        return '[no extension]'


def human_mem_size(num: int, suffix='B') -> str:
    """ Return a human readable memory size in a string.
    Initially written by Fred Cirera, modified and shared by Sridhar Ratnakumar
    (https://stackoverflow.com/a/1094933/6167478), edited by Victor Domingos.
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num = num / 1024.0

    return "%.1f%s%s" % (num, 'Yi', suffix)


def get_files_without_extension_path(path):
    """
    Don't recurse through subdirectories.
    Files without extension are those that do not have a suffix or start from a dot.
    PurePath.suffix return the file extension of the final component, if any.
    Path inherits this method.
    Behavior:
    PurePosixPath('my/library/setup.py').suffix -> '.py'
    PurePosixPath('my/library.tar.gz').suffix -> '.gz'
    PurePosixPath('my/library').suffix -> '' (empty string)
    :param path:
    :return: list with objects
    list example for win: return list with objects <class 'pathlib.WindowsPath'>
    [WindowsPath('C:/.../.gitignore'),
    WindowsPath('C:/.../Pipfile')]
    """
    result = []
    for p in Path(path).iterdir():
        if p.is_file():
            if '.' not in p.suffix:
                result.append(p)
    print(result)
    return result


def get_files_without_extension_scandir(path):
    """
    Don't recurse through subdirectories.
    Files without extension are those that do not have a suffix or start from a dot.
    :param path:
    :return: list with objects <class 'os.DirEntry'>
    list example: [<DirEntry '.gitignore'>, <DirEntry 'Pipfile'>]
    """
    result = []
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                if '.' not in entry.name or entry.name.startswith('.'):
                    result.append(entry)
    return result
