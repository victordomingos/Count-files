#!/usr/bin/env python3
# encoding: utf-8
"""Count Files.
A command-line interface (CLI) utility.
Supported operating systems: Linux, Mac OS, Windows.
It may also be used on iOS (iPhone/iPad) using the StaSh command-line in the Pythonista 3 app.
Main functions:
total counting of files (the total number of files it the directory);
file counting by extension (a table with file extensions sorted by frequency or alphabetically);
file searching by extension(a list with file paths, optional: file sizes, preview for text files).
Features:
counting or searching files with a specific extension, files without an extension,
all files regardless of the extension;
recursive and non-recursive counting or searching;
enable or disable the search or counting in hidden files and folders;
process the file extensions with case-sensitive or case-insensitive mode;
enable or disable the program's operating indicator (feedback).

© 2018 Victor Domingos & Nataliia Bondarenko
MIT License
"""
import os
from sys import platform
from argparse import ArgumentParser, Namespace
from typing import TypeVar, Union
from pathlib import Path
from textwrap import fill

from count_files.utils.file_handlers import count_files_by_extension, search_files, \
    get_total, get_total_by_extension
from count_files.utils.file_handlers import is_hidden_file_or_dir, is_supported_filetype
from count_files.utils.viewing_modes import show_2columns, show_start_message
from count_files.utils.viewing_modes import show_result_for_search_files
from count_files.settings import not_supported_type_message, supported_type_info_message, \
    DEFAULT_PREVIEW_SIZE, START_TEXT_WIDTH

# from count_files.utils.decorators import exceptions_decorator


parser = ArgumentParser(
    prog='count-files',
    description='Count files, grouped by extension, in a directory. By '
                'default, it will count files recursively in current '
                'working directory and all of its subdirectories, and '
                'will display a table showing the frequency for each file '
                'extension (e.g.: .txt, .py, .html, .css) and the total '
                'number of files found. Also by default, '
                'any hidden files or folders are ignored, '
                'and file extensions are treated with no case sensitiveness.')

parser.add_argument('-v', '--version', action='version', version=__import__('count_files').__version__)

parser.add_argument('-st', '--supported-types', action='store_true',
                    help='The list of currently supported file types for preview.')

parser.add_argument('path', nargs='?', default=os.getcwd(), type=str,
                    help='The path to the folder containing the files to be counted. '
                         'If you leave this argument empty, it will scan the current working directory. '
                         "To process files in the user's home directory, you can use ~ (tilde). "
                         'For example: count-files ~/Documents')

parser.add_argument('-a', '--all', action='store_true', default=False,
                    help='Include hidden files and directories. ')

parser.add_argument('-nr', '--no-recursion', action='store_true', default=False,
                    help="Don't recurse through subdirectories.")

parser.add_argument('-c', '--case-sensitive', action='store_true', default=False,
                    help='Treat file extensions with case sensitiveness.')

parser.add_argument('-nf', '--no-feedback', action='store_true', default=False,
                    help="Don't show the program's operating indicator "
                         '(printing processed file names in one line). '
                         'Feedback is available by default for counting files by extension '
                         '(table) and for counting the total number of files ("-t" or "--total"). '
                         'This option disables it.')

total_group = parser.add_argument_group('Total number of files'.upper(),
                                        description='Displaying the number of files that either have a '
                                                    'certain extension or no extension at all. '
                                                    'Usage: count-files [-a] [-c] [-nr] [-nf] [-t EXTENSION] [path]')

total_group.add_argument('-t', '--total', dest="extension", type=str,
                         help='Get the total number of files in the directory. '
                              'Specify the file extension or '
                              'use a single dot "." to get the total number of files that do not have any extension. '
                              'Use two dots without spaces ".." to get the total number of all files '
                              'with or without extension.')


count_group = parser.add_argument_group('File counting by extension'.upper(),
                                        description='Counting all files in the specified '
                                                    'directory, by file extension. '
                                                    'By default, it displays some feedback '
                                                    'while scanning and it presents a table with file '
                                                    'extensions sorted by frequency. '
                                                    'Usage: count-files [-a] [-alpha] [-c] [-nr] [-nf] [path]')

count_group.add_argument('-alpha', '--sort-alpha', action='store_true', default=False,
                         help='Sort the table alphabetically, by file extension.')

search_group = parser.add_argument_group('File searching by extension'.upper(),
                                         description='Searching for files that have a given extension. '
                                                     'By default, it presents a simple list with full '
                                                     'file paths. Optionally, it may also display a short '
                                                     'text preview for each found file. '
                                                     'Usage: count-files [-a] [-c] [-nr] [-fe FILE_EXTENSION] '
                                                     '[-fs] [-p] [-ps PREVIEW_SIZE] [path]')

search_group.add_argument('-fe', '--file-extension', type=str,
                          help='Search files by file extension. '
                               'You may use, instead, a single dot "." to search for files that don\'t have any extension, '
                               'or two dots ".." to search for all files with or without extension.')

search_group.add_argument('-p', '--preview', action='store_true', default=False,
                          help='Display a short preview (only available for text files when '
                               'using "-fe" or "--file_extension"). Default preview size: '
                               f'{DEFAULT_PREVIEW_SIZE} characters (5 lines).')

search_group.add_argument('-ps', '--preview-size', type=int, default=DEFAULT_PREVIEW_SIZE,
                          help='Specify the number of characters to be displayed from each '
                               'found file when using "-p" or "--preview".')

search_group.add_argument('-fs', '--file-sizes', action='store_true', default=False,
                          help='Show size info for each '
                               'found file when using "-fe" or "--file_extension". '
                               'Additional information: total combined size and average file size.')

parser._positionals.title = parser._positionals.title.upper()
parser._optionals.title = parser._optionals.title.upper()

argparse_namespace_object = TypeVar('argparse_namespace_object', bound=Namespace)


# @exceptions_decorator
def main_flow(*args: [argparse_namespace_object, Union[bytes, str]]):
    """Main application function.

    :param args: object <class 'argparse.Namespace'>,
    for tests param args - list with objects of <class 'str'>
    :return:
    Returns the processed data as text to the screen.
    Total number of files, table or list with file paths.
    Returns parser.exit(status=1):
    if path does not exist or there may be a typo in it,
    if the path has hidden folders and the argument --all is not specified,
    if the preview is not available for the specified file type.
    """
    args = parser.parse_args(*args)
    recursive = not args.no_recursion
    include_hidden = args.all
    sort_alpha = args.sort_alpha
    extension = args.file_extension

    if args.supported_types:
        parser.exit(status=0, message=supported_type_info_message)

    if os.path.abspath(args.path) == os.getcwd():
        location = os.getcwd()
        loc_text = ' the current directory'
    else:
        location = os.path.expanduser(args.path)
        loc_text = ':\n' + os.path.normpath(location)

    if not os.path.exists(location):
        parser.exit(status=1, message=f'The path {location} '
                                      f'does not exist, or there may be a typo in it.')

    if not include_hidden and is_hidden_file_or_dir(location):
        # skip check if path is a local drive
        if platform.startswith('win') and len(Path(location).parents) == 0:
            pass
        else:
            parser.exit(status=1, message=f'\nNot counting any files, because {loc_text[2:]}'
                                          f' has hidden folders.\n'
                                          f'Use the --all argument to include hidden files and folders.')

    # Parser total_group
    # getting the total number of files for -fe .. (all extensions), -fe . and -fe extension_name
    print("")
    if args.extension:
        print(fill(show_start_message(args.extension, args.case_sensitive, recursive, include_hidden, location, 'total'),
                   width=START_TEXT_WIDTH),
              end="\n\n"
              )

        if args.extension == '..':
            result = get_total(dirpath=location,
                               include_hidden=include_hidden,
                               no_feedback=args.no_feedback,
                               recursive=recursive)
        else:
            result = get_total_by_extension(dirpath=location,
                                            extension=args.extension,
                                            case_sensitive=args.case_sensitive,
                                            include_hidden=include_hidden,
                                            no_feedback=args.no_feedback,
                                            recursive=recursive)
        # var for tests
        total_result = len(list(result))
        print(f'   Found {total_result} file(s).',
              end="\n\n")
        return total_result

    # Parser search_group
    # search and list files by extension
    if extension:
        print(
            fill(show_start_message(extension, args.case_sensitive, recursive, include_hidden, location),
                 width=START_TEXT_WIDTH),
                 end="\n\n"
        )
        # list of all found file paths - enabled by default,
        # optional: information about file sizes, file preview, size specification for file preview
        if args.preview:
            if extension == '.' or not is_supported_filetype(extension.lower()):
                parser.exit(status=1, message=not_supported_type_message)

        # getting data list for -fe .. (all extensions), -fe . and -fe extension_name
        data = (f for f in search_files(dirpath=location,
                                        extension=extension,
                                        include_hidden=include_hidden,
                                        recursive=recursive,
                                        case_sensitive=args.case_sensitive))

        # display the result as a list
        len_files = show_result_for_search_files(files=data,
                                                 file_sizes=args.file_sizes,
                                                 preview=args.preview,
                                                 preview_size=args.preview_size)

        return len_files

    # Parser count_group
    # counting all files by extension
    print(fill(show_start_message(None, args.case_sensitive, recursive, include_hidden, location),
               width=START_TEXT_WIDTH),
          end="\n\n"
          )
    data = count_files_by_extension(dirpath=location,
                                    no_feedback=args.no_feedback,
                                    include_hidden=include_hidden,
                                    recursive=recursive,
                                    case_sensitive=args.case_sensitive)

    # display the result as a table
    
    # if empty sequence
    if not data:
        print("Oops! We have no data to show...\n")
        parser.exit(status=0)
        
    total_occurrences = sum(data.values())
    max_word_width = max(map(len, data.keys()))

    if sort_alpha:
        # sort extensions alphabetically, with uppercase versions on top
        sort_key = lambda data: (data[0].casefold(), data[0])
        data = sorted(data.items(), key=sort_key)
    else:
        # sort extensions by frequency for each file extension
        data = data.most_common()
    show_2columns(data, max_word_width, total_occurrences)
    parser.exit(status=0)


if __name__ == "__main__":
    main_flow()
