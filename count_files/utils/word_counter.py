#!/usr/bin/env python3
# encoding: utf-8
import os
from typing import Iterable

from count_files.utils.file_handlers import human_mem_size
from count_files.utils.file_preview import generate_preview
from count_files.settings import DEFAULT_PREVIEW_SIZE, TERM_WIDTH


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


def old_show_result_for_search_files(files: Iterable[str], no_list: bool, no_feedback: bool, preview: bool = False,
                                     preview_size: int = DEFAULT_PREVIEW_SIZE) -> int:
    """Print list of all found file paths, preview and size info
    or only the total number and size info(summary).

    :param files: list with paths
    :param no_list: view mode, False -> for now list(show list with paths, preview and size info),
    True -> no-list(show only the total number and size info)
    :param no_feedback: True or False(default, prints processed file names in one line)
    :param preview: optional, args.preview, True or False
    :param preview_size: optional, args.preview_size, number
    :return: len(files), print view mode
    no_list=True
    Found ... file(s).
    Total combined size: ... KiB.
    Average file size: ... KiB (max: ... KiB, min: ... B).
    no_list=False default
    full/path/to/file1.extension (... KiB)
    –––––––––––––––––––––––––––––––––––
    preview, if preview=True and supported type
    –––––––––––––––––––––––––––––––––––
    full/path/to/file2.extension (... KiB)
    ...
    Found ... file(s).
    Total combined size: ... KiB.
    Average file size: ... KiB (max: ... KiB, min: ... B).
    """
    files_amount = 0
    sizes = []
    if not no_list:
        try:
            for f_path in files:
                files_amount += 1
                file_size = os.path.getsize(f_path)
                sizes.append(file_size)
                filepath = str(f_path).strip("\r")
                print(f'{os.path.normpath(filepath)} ({human_mem_size(file_size)})')
                if preview:
                    print('–––––––––––––––––––––––––––––––––––')
                    print(generate_preview(str(f_path), max_size=preview_size))
                    print("–––––––––––––––––––––––––––––––––––\n")
        except StopIteration:
            print(f"No files were found in the specified directory.\n")
            return 0
    else:
        try:
            for f_path in files:
                files_amount += 1
                file_size = os.path.getsize(f_path)
                sizes.append(file_size)
                if not no_feedback:
                    print("\r" + os.path.basename(f_path)[:TERM_WIDTH - 1].ljust(TERM_WIDTH - 1), end="")
            print("\r".ljust(TERM_WIDTH - 1))  # Clean the feedback text before proceeding.
        except StopIteration:
            print(f"No files were found in the specified directory.\n")
            return 0
    if files_amount == 0:
        print(f"No files were found in the specified directory.\n")
        return 0

    total_size = sum(sizes)
    h_total_size = human_mem_size(total_size)
    avg_size = human_mem_size(int(total_size / files_amount))

    h_max = human_mem_size(max(sizes))
    h_min = human_mem_size(min(sizes))

    print(f"\n   Found {files_amount} file(s).")
    print(f"   Total combined size: {h_total_size}.")
    print(f"   Average file size: {avg_size} (max: {h_max}, min: {h_min}).\n")
    return files_amount


def show_result_for_search_files(files: Iterable[str],
                                 file_sizes: bool = False,
                                 preview: bool = False,
                                 preview_size: int = DEFAULT_PREVIEW_SIZE) -> int:
    """Print list of all found file paths(with sizes),
    preview, total number of files and size info(summary).

    :param files: list with paths
    :param file_sizes: True -> show size info, False -> don't show size info
    :param preview: optional, args.preview, True or False
    :param preview_size: optional, args.preview_size, number
    :return: len(files), print list with paths(default)
                                  if file_sizes:
    full/path/to/file1.extension (... KiB)
    –––––––––––––––––––––––––––––––––––
    preview, if preview=True and supported type
    –––––––––––––––––––––––––––––––––––
    full/path/to/file2.extension (... KiB)
    ...
    Found ... file(s).
    Total combined size: ... KiB.
    Average file size: ... KiB (max: ... KiB, min: ... B).
    """
    files_amount = 0
    sizes = []
    try:
        for f_path in files:
            files_amount += 1
            if file_sizes:
                file_size = os.path.getsize(f_path)
                sizes.append(file_size)
                s = f'({human_mem_size(file_size)})'
            filepath = str(f_path).strip("\r")
            print(f'{os.path.normpath(filepath)} {s if file_sizes else ""}')
            if preview:
                print('–––––––––––––––––––––––––––––––––––')
                print(generate_preview(str(f_path), max_size=preview_size))
                print("–––––––––––––––––––––––––––––––––––\n")
    except StopIteration:
        print(f"No files were found in the specified directory.\n")
        return 0
    if files_amount == 0:
        print(f"No files were found in the specified directory.\n")
        return 0
    print(f"\n   Found {files_amount} file(s).")
    if file_sizes:
        total_size = sum(sizes)
        h_total_size = human_mem_size(total_size)
        avg_size = human_mem_size(int(total_size / files_amount))

        h_max = human_mem_size(max(sizes))
        h_min = human_mem_size(min(sizes))

        print(f"   Total combined size: {h_total_size}.")
        print(f"   Average file size: {avg_size} (max: {h_max}, min: {h_min}).\n")
    return files_amount
