#!/usr/bin/env python3
# encoding: utf-8
"""
A little CLI utility written in Python to help you count files, grouped by
extension, in a directory. You can either pass it the path to the directory to
scan, or leave that argument empty and it will scan the current working
directory.

© 2018 Victor Domingos & Nataliia Bondarenko
MIT License
"""
import os

from argparse import ArgumentParser, Namespace
from typing import Type, TypeVar, Union
from count_files.utils.file_handlers import count_files_by_extension, search_files
from count_files.utils.file_handlers import is_hidden_file_or_dir, is_supported_filetype
from count_files.utils.word_counter import show_2columns, show_total
from count_files.utils.word_counter import show_result_for_search_files
from count_files.settings import not_supported_type_message, supported_type_info_message,\
    DEFAULT_PREVIEW_SIZE
# from count_files.utils.decorators import exceptions_decorator


parser = ArgumentParser(
    prog='count_files',
    description="Count files, grouped by extension, in a directory. By "
                "default, it will count files recursively in current "
                "working directory and all of its subdirectories, and "
                "will display a table showing the frequency for each file "
                "extension (e.g.: .txt, .py, .html, .css) and the total "
                "number of files found. Any hidden files or folders "
                "are ignored by default. File extensions are treated with no"
                "case sensitiveness, by default."
                "(Windows: files and directories for which FILE_ATTRIBUTE_HIDDEN is true; "
                "Linux, Mac OS: those with names starting with '.')")

parser.add_argument('-v', '--version', action='version', version=__import__('count_files').__version__)

parser.add_argument('-st', '--supported-types', action='store_true',
                    help="The list of currently supported file types for preview.")

parser.add_argument('path', nargs="?", default=os.getcwd(), type=str,
                    help='The path to the folder containing the files to be counted.')

parser.add_argument('-a', '--all', action='store_true',
                    help="Include hidden files and directories. "
                         "Windows: files and directories for which FILE_ATTRIBUTE_HIDDEN is true; "
                         "Linux, Mac OS: those with names starting with '.'(dot)")

parser.add_argument('-nr', "--no-recursion", action='store_true',
                    help="Don't recurse through subdirectories.")

parser.add_argument('-c', "--case-sensitive", action='store_true',
                    help="Treat file extensions with case sensitiveness.")

parser.add_argument('-nf', "--no-feedback", action='store_true', default=False,
                    help="Don't show the program's operating indicator"
                         "(printing processed file names in one line). "
                         "Feedback is available by default for counting files by extension"
                         "(table and no-table), searching for files by extension"
                         "(viewing mode no-list). This option disables it.")

count_group = parser.add_argument_group('File counting by extension',
                                        description='Counting all files in the specified '
                                                    'directory with or without extensions. '
                                                    'Default settings: recursively count all files, '
                                                    'ignoring hidden files and directories; '
                                                    'path - the current working directory; '
                                                    'view mode - a table with file '
                                                    'extensions sorted by frequency; '
                                                    "feedback - printing processed file names in one line, "
                                                    "use '-nf' to disable it). "
                                                    'Usage: count_files [-a] [-nr] [-nf] [-alpha] [-nt] [path]')

count_group.add_argument('-alpha', '--sort-alpha', action='store_true',
                         help="Sort the table alphabetically, by file extension.")

count_group.add_argument('-nt', '--no-table', action='store_true',
                         help="Don't show the table, only the total number of files.")

search_group = parser.add_argument_group("File searching by extension",
                                         description="Search for files with a given extension. "
                                                     "Default settings: recursively search all files, "
                                                     "ignoring hidden files and directories; "
                                                     "path - the current working directory; "
                                                     "view mode - a list with full file paths; "
                                                     f"preview size - {DEFAULT_PREVIEW_SIZE} chars; "
                                                     "feedback - printing processed file names in one line"
                                                     "(available by default only for '-nl' or '--no-list', "
                                                     "use '-nf' to disable it). "
                                                     "Usage: count_files [-a] [-nr] [-nf] [-fe FILE_EXTENSION] [-p] "
                                                     "[-ps PREVIEW_SIZE] [-nl] [path]")

search_group.add_argument('-fe', '--file-extension', type=str,
                          help="Search files by file extension. "
                               "Specify the name of the extension or "
                               "use a single dot '.' to search for files without any extension. "
                               "Use a two dots '..' to search for all files with extension or without it.")

search_group.add_argument('-p', '--preview', action='store_true',
                          help="Display a short preview (only available for text files when "
                          "using '-fe' or '--file_extension').")

search_group.add_argument('-ps', '--preview-size', type=int, default=DEFAULT_PREVIEW_SIZE,
                          help="Specify the number of characters to be displayed from each "
                          "found file when using '-p' or '--preview'.")

search_group.add_argument('-nl', '--no-list', action='store_true',
                          help="Don't show the list, "
                               "only the total number of files and information about file sizes.")


argparse_namespace_object = TypeVar('argparse_namespace_object', bound=Namespace)


# @exceptions_decorator
def main_flow(*args: [argparse_namespace_object, Union[bytes, str]]):
    """Main application function.

    :param args: object <class 'argparse.Namespace'>,
    for tests param args - tuple with objects of <class 'str'>
    :return:
    """
    args = parser.parse_args(*args)
    recursive = not args.no_recursion
    include_hidden = args.all
    show_table = not args.no_table
    sort_alpha = args.sort_alpha
    extension = args.file_extension

    if args.supported_types:
        parser.exit(status=0, message=supported_type_info_message)

    if os.path.abspath(args.path) == os.getcwd():
        location = os.getcwd()
        loc_text = ' the current directory'
    else:
        location = os.path.expanduser(args.path)
        loc_text = ':\n' + location

    if not os.path.exists(location):
        parser.exit(status=1, message=f'The path {location} does not exist, or there may be a typo in it.')

    if not include_hidden and is_hidden_file_or_dir(location):
        parser.exit(status=1, message=f'\nNot counting any files, because {loc_text[2:]} has hidden folders.\n'
                                      f'Use: python -m count_files {args.path} --all')

    action = 'searching' if extension else "counting"
    r = f'Recursively {action} all files'
    nr = f'{action.title()} files'
    wi = 'or without it'
    case = 'case-sensitive' if args.case_sensitive else 'case-insensitive'
    e = f' with ({case}) extension {"." + args.file_extension if args.file_extension != ".." else wi}' if extension else ''
    all_e = ' without any extension' if extension else ''
    h = ' including hidden files and directories'
    nh = ' ignoring hidden files and directories'

    print(f'\n{r if recursive else nr}{e if args.file_extension != "." else all_e},'
          f'{h if include_hidden else nh}, in {location}\n')
    # Either search and list files by extension...
    if extension:
        # no-list=True, only the total number of files and information about file sizes
        # no-list=False, list of all found file paths - enabled by default,
        # optional file preview, size specification for file preview
        #if args.preview and not args.no_list:
        #    if not is_supported_filetype(extension):
        #        parser.exit(status=0, message=not_supported_type_message)

        # getting data list for -fe .. (all extensions), -fe . and -fe extension_name
        data = (f for f in search_files(dirpath=location, extension=extension,
                                        include_hidden=include_hidden,
                                        recursive=recursive,
                                        case_sensitive=args.case_sensitive))

        # display result in chosen view mode
        len_files = show_result_for_search_files(files=data,
                                                 no_list=args.no_list,
                                                 no_feedback=args.no_feedback,
                                                 preview=args.preview,
                                                 preview_size=args.preview_size)

        return len_files

    # ...or do other stuff, i.e., counting files.
    # all extensions
    data = count_files_by_extension(dirpath=location,
                                    no_feedback=args.no_feedback,
                                    include_hidden=include_hidden,
                                    recursive=recursive,
                                    case_sensitive=args.case_sensitive)

    if show_table:
        if sort_alpha:
            # sort extensions alphabeticaly, with uppercase versions on top
            sort_key = lambda data: (data[0].casefold(), data[0])
            show_2columns(sorted(data.items(), key=sort_key))
        else:
            show_2columns(data.most_common())
        # it returns None
    else:
        return show_total(data) # this return value is used for tests in test_argument_parser.py


if __name__ == "__main__":
    main_flow()
