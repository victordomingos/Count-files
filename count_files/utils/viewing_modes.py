#!/usr/bin/env python3
# encoding: utf-8
import os
from typing import Iterable, List
from textwrap import wrap

from count_files.utils.file_handlers import human_mem_size
from count_files.utils.file_preview import generate_preview
from count_files.settings import TERM_WIDTH, DEFAULT_PREVIEW_SIZE
from count_files.settings import DEFAULT_EXTENSION_COL_WIDTH
from count_files.settings import DEFAULT_FREQ_COL_WIDTH, MAX_TABLE_WIDTH


def show_2columns(data: List[tuple],
                  max_word_width: int, total_occurrences: int,
                  term_width: int = TERM_WIDTH):
    """Displays a sorted table with file extensions.

    :param data: list with tuples
    default in uppercase: [('TXT', 24), ('PY', 17), ('PYC', 13), ...]
    with --case-sensitive as is: [('txt', 23), ('py', 17), ('pyc', 13), ...]
    :param max_word_width: the longest extension name
    :param total_occurrences: total number of files found
    :param term_width: the size of the terminal window
    :return: the processed data as text to the screen.
    """
    if not data:
        print("Oops! We have no data to show...\n")
        return

    max_word_width = max(DEFAULT_EXTENSION_COL_WIDTH, max_word_width)
    freq_col_width = max(DEFAULT_FREQ_COL_WIDTH, len(str(total_occurrences)))
    ext_col_width = min((term_width - freq_col_width - 5),
                        max_word_width,
                        MAX_TABLE_WIDTH)

    header = f" {'EXTENSION'.ljust(ext_col_width)} | {'FREQ.'.ljust(freq_col_width)} "
    sep_left = (ext_col_width + 2) * '-'
    sep_center = "+"
    sep_right = (freq_col_width + 2) * '-'
    sep = sep_left + sep_center + sep_right
    print(header)
    print(sep)

    for word, freq in data:
        if len(word) <= ext_col_width:
            print(f" {word.ljust(ext_col_width)} | {str(freq).rjust(freq_col_width)} ")
        else:
            head = f" {word[0: ext_col_width]} | {str(freq).rjust(freq_col_width)}"
            word_tail = wrap(word[ext_col_width:],
                             width=ext_col_width,
                             initial_indent=' ' * 2,
                             subsequent_indent=' ' * 2)
            print(head)
            for line in word_tail:
                print(f" {line.ljust(ext_col_width)} | {' '.rjust(freq_col_width)}")

    print(sep)
    line = f" {'TOTAL:'.ljust(ext_col_width)} | {str(total_occurrences).rjust(freq_col_width)} "
    print(line)
    print(sep + "\n")
    return


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
        print(f"\nNo files were found in the specified directory.\n")
        return 0
    if files_amount == 0:
        print(f"\nNo files were found in the specified directory.\n")
        return 0
    print(f"\n   Found {files_amount} file(s).", end="\n")
    if file_sizes:
        total_size = sum(sizes)
        h_total_size = human_mem_size(total_size)
        avg_size = human_mem_size(int(total_size / files_amount))

        h_max = human_mem_size(max(sizes))
        h_min = human_mem_size(min(sizes))

        print(f"   Total combined size: {h_total_size}.")
        print(f"   Average file size: {avg_size} (max: {h_max}, min: {h_min}).",
                 end="\n\n")
    else:
        print("")
    return files_amount


def show_start_message(value: [None, str], case_sensitive: bool, recursive: bool, include_hidden: bool,
                       location: str, group: str = None) -> str:
    """Displays an information message before starting the CLI.

    :param value: str for args.total or args.file_extension, for table - None.
    :param case_sensitive: args.case_sensitive
    :param recursive: args.no_recursion
    :param include_hidden: args.all
    :param location: path argument
    :param group: for now 'total' or None
    :return: prints information message
    """
    wi = 'or without it'
    case = 'case-sensitive' if case_sensitive else 'case-insensitive'
    all_e = ' without any extension'
    h = ' including hidden files and directories'
    nh = ' ignoring hidden files and directories'

    if group == 'total':
        r = f'Recursively counting total number of files'
        nr = 'Counting total number of files'
        e = f' with{" (" + case + ")" if value not in [".", ".."] else ""} ' \
            f'extension {"." + value if value != ".." else wi}'
    # count_group and search_group
    else:
        action = 'searching' if value else 'counting'
        r = f'Recursively {action} all files'
        nr = f'{action.title()} files'
        e = f' with{" (" + case + ")" if value not in [".", ".."] else ""} ' \
            f'extension {"." + value if value != ".." else wi}' if value else ''

    message = f'{r if recursive else nr}{e if value != "." else all_e},' \
              f'{h if include_hidden else nh}, in {location}'

    return message
