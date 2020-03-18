#!/usr/bin/env python3
# encoding: utf-8
"""Functions designed to display the results of the program or CLI messages.

CLI viewing modes:
count - def show_2columns
    table with file extensions sorted by frequency or alphabetically
count - def show_ext_grouped_by_type
    displays a two column list with file extensions and its frequency
    sorted by type and by frequency (inside each type group)
count - def show_group_ext_and_freq
    displays one type group with header and file extensions and its frequency
search - def show_result_for_search_files
    list of all found file paths(with sizes),
    preview, total number of files and size info(summary)
total - def show_result_for_total
    total number of all found file paths
help extension - def show_help_columns
    table with the specified number of columns to display available help topics
    (argument or group name, sort words)

CLI messages:
def show_start_message
    message with information about selected counting or searching CLI arguments

Other utilities:
def human_mem_size
    return a human readable memory size in a string for os.path.getsize(file_path)
"""
import os
from typing import Iterable, List, Tuple, Dict
from textwrap import wrap

from count_files.utils.file_preview import generate_preview
from count_files.utils.file_handlers import group_ext_by_type
from count_files.settings import TERM_WIDTH, DEFAULT_PREVIEW_SIZE
from count_files.settings import DEFAULT_EXTENSION_COL_WIDTH
from count_files.settings import DEFAULT_FREQ_COL_WIDTH, MAX_TABLE_WIDTH


def show_group_ext_and_freq(data: List[Tuple[str, int]], header: str,
                            term_width: int = TERM_WIDTH, end_message: str = None):
    """Displays one type group with header and file extensions and its frequency.
     A list of two columns that adjusts to the width of the terminal.
    :param data: : [('png', 8), ('jpg', 5),...]
    :param header: group name, for example, 'images'
    :param term_width: terminal width
    :param end_message: total_occurrences
    :return: the processed data as text to the screen
    """
    # with def show_ext_grouped_by_type:
    # "+", 1 indentation spaces before header, header, "(", number, ")"
    # 3 indentation spaces before ext, ext, 1 separator ":", 1 space before freq, freq
    # with def show_2columns:
    # header '+ EXTENSION: FREQ.'
    # 3 indentation spaces before ext, ext, 1 separator ":", 1 space before freq, freq
    if len(header) <= term_width:
        print(header)
    else:
        # if greater than terminal width
        header = wrap(header,
                      width=term_width, initial_indent='', subsequent_indent=' ' * 2)
        for line in header:
            print(line)
    for (ext, freq) in data:
        ext_and_freq = f'   {ext}: {freq}'
        if len(ext_and_freq) <= term_width:
            print(ext_and_freq)
        else:
            # if greater than terminal width
            w = wrap(f'   {ext}: {freq}',
                     width=term_width, initial_indent='', subsequent_indent=' ' * 3)
            for line in w:
                print(line)
    if end_message:
        print(end_message)
    return


def show_ext_grouped_by_type(data: List[tuple], ext_and_group: Dict[str, str],
                             term_width: int = TERM_WIDTH) -> Dict[str, List[Tuple[str, int]]]:
    """Displays a two column list with file extensions and its frequency.
     Extensions sorted by type (e.g.: images, videos, documents)
     and by frequency (inside each type group).
    :param data: Counter.most_common(), list with tuples sorted by frequency
    default in uppercase: [('TXT', 24), ('PY', 17), ('PYC', 13), ...]
    with --case-sensitive as is: [('txt', 23), ('py', 17), ('pyc', 13), ('JPG', 9), ...]
    :param ext_and_group: dict with items like {'png': 'image', 'txt': documents, ...}
    :param term_width: the size of the terminal window
    :return: the processed data as text to the screen
    sorted_data - dict with items like {'images': [('png', 8), ...], 'documents': [('txt', 25), ...], ...}
    """
    sorted_data: dict = group_ext_by_type(data=data, ext_and_group=ext_and_group)
    for k, v in sorted_data.items():
        # if value list is not empty
        if v:
            total_v_occurrences = sum([x[1] for x in v])
            header = f"+ {k.upper()}({total_v_occurrences})"
            show_group_ext_and_freq(v, header, term_width)
    return sorted_data


def human_mem_size(num: int, suffix: str = 'B') -> str:
    """Return a human readable memory size in a string.

    Initially written by Fred Cirera, modified and shared by Sridhar Ratnakumar
    (https://stackoverflow.com/a/1094933/6167478), edited by Victor Domingos.
    """
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num = num / 1024.0

    return "%.1f%s%s" % (num, 'Yi', suffix)


def show_start_message(value: [None, str], case_sensitive: bool, recursive: bool, include_hidden: bool,
                       location: str, group: str = None) -> str:
    """Displays a message with information about selected counting or searching CLI arguments.

    :param value: for args.pattern, args.total or args.file_extension - string, for table - None.
    :param case_sensitive: args.case_sensitive
    :param recursive: args.no_recursion
    :param include_hidden: args.all
    :param location: path argument
    :param group: 'pattern'(search_group -fm), 'total' or None(count_group and search_group -fe)
    :return: prints information message
    """
    wi = 'or without it'
    case = 'case-sensitive' if case_sensitive else 'case-insensitive'
    all_e = ' without any extension'
    h = ' including hidden files and directories'
    nh = ' ignoring hidden files and directories'

    if group == 'pattern':  # search_group --filename-match [pattern]
        r = f'Recursively searching for files'
        nr = f'Searching for files'
        message = f'{r if recursive else nr} with{" (" + case + ") pattern"} {value},' \
                  f'{h if include_hidden else nh}, in {location}'

    else:
        if group == 'total':
            r = f'Recursively counting total number of files'
            nr = 'Counting total number of files'
            e = f' with{" (" + case + ")" if value not in [".", ".."] else ""} ' \
                f'extension {"." + value if value != ".." else wi}'
        else:
            # count_group and search_group -fe
            action = 'searching' if value else 'counting'
            r = f'Recursively {action} all files'
            nr = f'{action.title()} files'
            e = f' with{" (" + case + ")" if value not in [".", ".."] else ""} ' \
                f'extension {"." + value if value != ".." else wi}' if value else ''

        message = f'{r if recursive else nr}{e if value != "." else all_e},' \
                  f'{h if include_hidden else nh}, in {location}'
    return message


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

    if term_width < (max_word_width + freq_col_width + 5):
        print("Oops! There isn't enough horizontal space to display the frequency table. \n")
        return

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
    :return: len(files), print list with paths(default),
    get preview and file_sizes if specified.

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


def show_result_for_total(files: Iterable[str], show_folders: bool = False,
                          total_size: bool = False, no_feedback: bool = False,
                          recursive: bool = True) -> int:
    """Prints feedback and the total number of all files found for Parser total_group.

    Prints a list of folders in which the found files are located,
    the number of found files in each folder
    and the total combined size of the found files (if specified).
    When recursively counting all files(--total ..) and using the --show-folders argument,
    all folders containing files are displayed.

    :param files: object <class 'generator'> with full paths to all found files
    :param show_folders: optional, args.show_folders
    True - show the list of folders in which the found files are located,
    and the number of found files in each folder,
    False(default) - don't show
    :param total_size: optional, args.total_size
    True - show the total combined size of files found, average, minimum and maximum file size
    False(default) - don't show
    :param no_feedback: optional, args.no_feedback
    True - disable feedback
    False(default) - prints processed file paths in one line
    :param recursive: default recursive search or count if args.no_recursion is not selected
    :return: files amount - Found ... file(s).
    print list with folder paths if show_folders, and total combined size of files found if specified.

    File(s) found in the following folder(s):
    –––––––––––––––––––––––––––––––––––-----
    full/path/to/folder1 (2 files)
    full/path/to/folder2 (1 file)
    ...
    –––––––––––––––––––––––––––––––––––-----

    Found ... file(s).
    Total combined size of files found: ... KiB.
    Average file size: ... KiB (max: ... KiB, min: ... B).
    """
    files_amount = 0
    sizes = []
    folders = {}
    try:
        for f_path in files:
            if not no_feedback:
                print("\r" + f_path[:TERM_WIDTH - 1].ljust(TERM_WIDTH - 1), end="")
            files_amount += 1
            if total_size:
                file_size = os.path.getsize(f_path)
                sizes.append(file_size)
            if show_folders and recursive:
                root, filename = str(f_path).strip("\r").rsplit(os.sep, maxsplit=1)
                if root not in folders.keys():
                    folders.update({root: 1})
                else:
                    folders[root] += 1
            else:
                pass
        if not no_feedback:
            print("\r".ljust(TERM_WIDTH))  # Clean the feedback text before proceeding.
    except StopIteration:
        print(f"\nNo files were found in the specified directory.\n")
        return 0
    if files_amount == 0:
        print(f"\nNo files were found in the specified directory.\n")
        return 0
    if show_folders:
        if recursive:
            print('File(s) found in the following folder(s):')
            print('–––––––––––––––––––––––––––––––––––-----')
            for folder, f in folders.items():
                print(f'{folder} ({f} {"file" if f == 1 else "files"})')
            print('–––––––––––––––––––––––––––––––––––-----')
        else:
            pass  # count/search in one folder
    print(f"\n   Found {files_amount} file(s).", end="\n")
    if total_size:
        total_fsize = sum(sizes)
        h_total_size = human_mem_size(total_fsize)
        avg_size = human_mem_size(int(total_fsize / files_amount))

        h_max = human_mem_size(max(sizes))
        h_min = human_mem_size(min(sizes))

        print(f"   Total combined size of files found: {h_total_size}.")
        print(f"   Average file size: {avg_size} (max: {h_max}, min: {h_min}).",
              end="\n\n")
    else:
        print("")
    return files_amount


def show_help_columns(column_version: List[str], list_version: List[str],
                      num_columns: int = 2, term_width: int = TERM_WIDTH) -> str:
    """Displays a table with the specified number of columns.

    Suitable for a list with short words.
    If the words are very long and/or there are many columns
    (the width of the table is greater than the width of the terminal),
    then the data is displayed in a list.
    When used in the help extension, the list is displayed using the textwrap fill().
    For a table, the width of each column is equal
    to the width of the longest word in the list.

    :param column_version: list with words
    The first in the list may be the names of the columns.
    Example: column_version = ['LONG', 'SHORT',
                               'path', 'path',
                               'all', 'a',
                               'args-help', 'ah']
    :param list_version: list with words
    :param num_columns: number of columns
    :param term_width: width of the terminal; also required for testing
    :return:
    """
    max_word_width = max(map(len, column_version))
    if (max_word_width * num_columns + 3 * num_columns) > term_width:
        return ', '.join(list_version)
    text_table = " "
    for count, item in enumerate(column_version, 1):
        text_table += item.ljust(max_word_width + 3)
        if count % num_columns == 0 or count == len(column_version):
            text_table += "\n "
    return text_table
