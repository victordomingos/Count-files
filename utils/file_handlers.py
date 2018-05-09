import os

def get_file_extension(file_path: str) -> str:
    """ Extract only the file extension from a given path.
        If the file name does not have an extension, return '[no extension]'.
    """
    extension = os.path.splitext(file_path)[1]
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
