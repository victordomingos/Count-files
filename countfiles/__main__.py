#!/usr/bin/env python3
# encoding: utf-8
"""
A little CLI utility written in Python to help you count files, grouped by
extension, in a directory. You can either pass it the path to the directory to
scan, or leave that argument empty and it will scan the current working
directory.
© 2018 Victor Domingos, Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
"""
import os
import sys

from argparse import ArgumentParser, Namespace
from typing import Type, TypeVar

from countfiles.utils.file_handlers import get_file_extension, is_hidden
from countfiles.utils.word_counter import WordCounter
from countfiles.utils.file_handlers import recursive_search, non_recursive_search, is_hidden_file_or_dir


parser = ArgumentParser(
    description="Count files, grouped by extension, in a directory. By "
                "default, it will count files recursively in current "
                "working directory and all of its subdirectories, and "
                "will display a table showing the frequency for each file "
                "extension (e.g.: .txt, .py, .html, .css) and the total "
                "number of files found. Any hidden files or folders "
                "(those with names starting with '.') are ignored by "
                "default.")

parser.add_argument('path', nargs="?", default=os.getcwd(),
                    help='The path to the folder containing the files to be counted.')

parser.add_argument('-a', '--all', action='store_true',
                    help="Include hidden files and directories (names starting with '.')")

parser.add_argument('-alpha', '--sort-alpha', action='store_true',
                    help="Sort the table alphabetically, by file extension.")

parser.add_argument('-nr', "--no-recursion", action='store_true',
                    help="Don't recurse through subdirectories")

parser.add_argument('-nt', '--no-table', action='store_true',
                    help="Don't show the table, only the total number of files")

parser.add_argument('-fe', '--file-extension', required=False, type=str,
                    help="Search files by file extension (use a single dot '.' to search for "
                         "files without any extension)")

parser.add_argument('-p', '--preview', action='store_true',
                    help="Display a short preview (only available for text files when "
                         "using '-fe' or '--file_extension')")

parser.add_argument('-ps', '--preview-size', required=False, type=int, default=390,
                    help="Specify the number of characters to be displayed from each "
                         "found file when using '-p' or '--preview')")
args = parser.parse_args()

argparse_namespace_object = TypeVar('argparse_namespace_object', bound=Namespace)


# @exceptions_decorator
def main_flow(args: Type[argparse_namespace_object]):
    """Main application function.

    :param args: object <class 'argparse.Namespace'>
    :return:
    """
    recursive = not args.no_recursion
    include_hidden = args.all
    show_table = not args.no_table
    sort_alpha = args.sort_alpha
    search_by_extension = True if args.file_extension else False
    platform_name = sys.platform
    fc = WordCounter()

    if os.path.abspath(args.path) == os.getcwd():
        location = os.getcwd()
        loc_text = ' the current directory'
    else:
        location = os.path.expanduser(args.path)
        loc_text = ':\n' + location

    if not os.path.exists(location):
        print(f'The path {location} does not exist, or there may be a typo in it.')
        return

    if not include_hidden and is_hidden_file_or_dir(platform_name, location):
        print(f'\nNot counting any files, because {loc_text[2:]} is hidden.')
        return

    # Either search and list files by extension...
    if search_by_extension:
        len_files = fc.get_files_by_extension(location, args.file_extension,
                                              preview=args.preview,
                                              preview_size=args.preview_size,
                                              recursion=recursive,
                                              include_hidden=include_hidden)
        return len_files

    # ...or do other stuff.
    if include_hidden:
        hidden_msg = "including hidden files and directories,"
    else:
        hidden_msg = "ignoring hidden files and directories,"

    if recursive:
        print(f'\nRecursively counting all files, {hidden_msg} in {loc_text}.\n')
        files = recursive_search(location, platform_name, hidden=include_hidden)
        #for root, dirs, files in os.walk(location):
            #if not include_hidden:
                #dirs[:] = [d for d in dirs if not is_hidden(d)]
                #files = [f for f in files if not is_hidden(f)]
        #for f in files:
            #fc.count_word(get_file_extension(f))
    else:
        #if not include_hidden and '/.' in location:
            #print(f'\nNot counting any files, because {loc_text[2:]} is hidden.')
            #return
        #else:
        print(f'\nCounting files, {hidden_msg} in {loc_text}.\n')
            #with os.scandir(location) as directory:
                #for f in directory:
                    #if not include_hidden and is_hidden(f):
                        #continue
                    #if f.is_file():  # Skip directories
                        #fc.count_word(get_file_extension(f.name))
        files = non_recursive_search(location, platform_name, hidden=include_hidden)

    for f in files:
        fc.count_word(get_file_extension(f))

    if show_table:
        if sort_alpha:
            fc.show_2columns(fc.sort_by_word())
        else:
            fc.show_2columns(fc.sort_by_frequency())
    else:
        return fc.show_total()


if __name__ == "__main__":
    main_flow(args)
