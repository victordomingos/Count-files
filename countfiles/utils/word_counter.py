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
    """ Search for files that have the given extension in their filename and optionally display
    a preview of the file.

    Special thanks to Natalia Bondarenko (github.com/NataliaBondarenko),
    who suggested this feature and submited an initial implementation.
    """
    if include_hidden:
        hide_text = ", including hidden items,"
    else:
        hide_text = ""
    if recursion:
        if extension == '.':
            print(f'\nRecursively searching for files without extension{hide_text} in {location}.\n')
            files = search_files(location, ".", recursive=True,
                                 include_hidden=include_hidden)
        else:
            print(f'\nRecursively searching for .{extension} files{hide_text} in {location}.\n')
            files = search_files(location, extension, recursive=True,
                                 include_hidden=include_hidden)

    else:
        if extension == '.':
            print(f'\nSearching for files without extension{hide_text} in {location}.\n')
            files = search_files(location, ".", recursive=False,
                                 include_hidden=include_hidden)
        else:
            print(f'\nSearching for .{extension} files{hide_text} in {location}.\n')
            files = search_files(location, extension, recursive=False,
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

        if extension == '.':
            print(f"\n   Found {len(files)} files without extension.")
        else:
            print(f"\n   Found {len(files)} .{extension} files.")
        print(f"   Total combined size: {h_total_size}.")
        print(f"   Average file size: {avg_size} (max: {h_max}, min: {h_min}).\n")
        return len(files)

    else:
        if extension == '.':
            print(f"No files without extension were found in the specified directory.\n")
        else:
            print(
                f"No files with the extension '{extension}' were found in the specified directory.\n")
        return 0
