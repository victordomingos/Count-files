#!/usr/bin/env python3

import os

from countfiles.utils.file_handlers import human_mem_size
from countfiles.utils.file_handlers import search_files
from countfiles.utils.file_preview import generate_preview


def show_2columns(data):
    if not data:
        print("Oops! We have no data to show...\n")
        return

    max_word_width = 9  # default value, the minimum EXTENSION col. width
    total_occurences = 0
    for word, freq in data:
        total_occurences += freq
        max_word_width = max(len(word), max_word_width)

    total_occurences_width = len(str(total_occurences))
    if total_occurences_width < 5:
        total_occurences_width = 5

    header = f" {'EXTENSION'.ljust(max_word_width)} | {'FREQ.'.ljust(total_occurences_width)} "
    sep_left = (max_word_width + 2) * '-'
    sep_center = "+"
    sep_right = (total_occurences_width + 2) * '-'
    sep = sep_left + sep_center + sep_right
    print(header)
    print(sep)

    for word, freq in data:
        print(f" {word.ljust(max_word_width)} | {str(freq).rjust(total_occurences_width)} ")

    print(sep)
    line = f" {'TOTAL:'.ljust(max_word_width)} | {str(total_occurences).rjust(total_occurences_width)} "
    print(line)
    print(sep + "\n")


def show_total(data) -> int:
    total = sum(data.values())
    print(f"Total number of files in selected directory: {total}.\n")
    return total


def get_files_by_extension(location: str, extension: str, preview=False, preview_size=395,
                           recursion=True, include_hidden=False) -> int:
    """Search for files that have the given extension in their filename and optionally display
    the number of files found, total, minimum and maximum size of files.

    :param location: full/path/to/file
    :param extension: extension name (txt, py) or '' (default all extensions)
    :param preview: file contents
    :param preview_size: number of characters to display the contents of the file
    :param recursion: True or False
    :param include_hidden: True or False
    :return: len(files) for tests,
    For user, depending on the parameters, something like this:
    Search options
    location: C:/Users/.../path/to/folder
    extension: py
    recursion: True
    include hidden: False
    C:/Users/.../path/to/folder\not_hidden.txt (0.0 B)
    C:/Users/.../path/to/folder/sub-folder\not_hidden.xlsx (9.7 KiB)

    Found 2 file(s).
    Total combined size: 9.7 KiB.
    Average file size: 4.8 KiB (max: 9.7 KiB, min: 0.0 B).
    """
    files = search_files(location,
                         extension=extension,
                         recursive=recursion,
                         include_hidden=include_hidden)

    if files:
        sizes = []
        for f_path in files:
            file_size = os.path.getsize(f_path)
            sizes.append(file_size)
            filepath = str(f_path).strip("\r")
            print(f'{filepath} ({human_mem_size(file_size)})')
            if preview:
                print('–––––––––––––––––––––––––––––––––––')
                print(generate_preview(str(f_path), max_size=preview_size))
                print("–––––––––––––––––––––––––––––––––––\n")

        total_size = sum(sizes)
        h_total_size = human_mem_size(total_size)
        avg_size = human_mem_size(int(total_size / len(files)))

        h_max = human_mem_size(max(sizes))
        h_min = human_mem_size(min(sizes))

        print(f"\n   Found {len(files)} file(s).")
        print(f"   Total combined size: {h_total_size}.")
        print(f"   Average file size: {avg_size} (max: {h_max}, min: {h_min}).\n")
        return len(files)

    else:
        print(f"No files were found in the specified directory.\n")
        return 0
