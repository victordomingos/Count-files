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
import argparse


def get_file_extension(file_path: str) -> str:
    filename_parts = file_path.split('.')
    if len(filename_parts) == 1:
        extension = '[no extension]'
    else:
        extension = filename_parts[-1]
    return extension


class WordCounter:
    def __init__(self):
        self.counters = dict()

    def count_word(self, word:str):
        if word in self.counters.keys():
            self.counters[word] += 1
        else:
            self.counters[word] = 1           

    def sort_by_frequency(self):
        sorted_counters = [(word, self.counters[word])
                           for word in sorted(self.counters,
                                              key=self.counters.get,
                                              reverse=True)]
        return sorted_counters

    def sort_by_word(self):
        sorted_counters = [(word, self.counters[word])
                           for word in sorted(self.counters,
                                              key=self.counters.get,
                                              reverse=True)]
        return sorted_counters

    def show_2columns(self, data):
        if len(data) == 0:
            print("Oops! We have no data to show...\n")
            return

        max_word_width = 0
        total_occurences = 0
        for word, freq in data:
            total_occurences += freq
            word_w = len(word)
            if word_w > max_word_width:
                max_word_width = word_w

        if max_word_width < 11:
            max_word_width = 11

        total_occurences_width = len(str(total_occurences))
        if total_occurences_width < 5:
            total_occurences_width = 5

        header = f" {'EXTENSION'.ljust(max_word_width)} | {'FREQ.'.ljust(total_occurences_width)} "
        sep_left = (max_word_width+2) * '-'
        sep_center = "+"
        sep_right = (total_occurences_width+2) * '-'
        sep = sep_left + sep_center + sep_right
        print(header)
        print(sep)

        for word, freq in data:
            line = f" {word.ljust(max_word_width)} | {str(freq).rjust(total_occurences_width)} "
            print(line)
        print(sep)
        line = f" {'TOTAL:'.ljust(max_word_width)} | {str(total_occurences).rjust(total_occurences_width)} "
        print(line)
        print(sep + "\n")

    def show_total(self):
        total = 0
        for _, freq in self.counters.items():
            total += freq
        print(f"Total number of files in selected directory: {total}.\n")


if __name__ == "__main__":  
    parser = argparse.ArgumentParser(
        description='\nRecursively count all files in a directory, grouped by file extension.')
    
    parser.add_argument('path',
        nargs='?',
        default=os.getcwd(),
        help='The path to the folder containing the files to be counted.')

    parser.add_argument('-nr',
        action='store_true',
        help="Don't recurse through subdirectories")

    parser.add_argument('-nt',
        action='store_true',
        help="Don't show the table, only the total number of files")

    parser.add_argument('-a',
        action='store_true',
        help="Include hidden files and directories (with filenames starting with '.')")

    args = parser.parse_args()
    recursive = not args.nr
    include_hidden = args.a
    show_table = not args.nt

    
    fc = WordCounter()
        
    if os.path.abspath(args.path) == os.getcwd():
        location = os.getcwd()
        loc_text = ' the current directory'
    else:
        location = os.path.expanduser(args.path)
        loc_text = ':\n' + location

    if include_hidden:
        hidden_msg = "including hidden files and directories,"
    else:
        hidden_msg = "ignoring hidden files and directories,"

    if recursive:  
        print(f'\nRecursively counting all files, {hidden_msg} in{loc_text}.\n')
        for root, dirs, files in os.walk(location):
            for f in files:
                if not include_hidden:
                    if f.startswith('.') or ('/.' in root):
                        continue

                extension = get_file_extension(f)
                fc.count_word(extension)
    else: 
        print(f'\nCounting files, {hidden_msg} in{loc_text}.\n')
        for f in os.listdir(location):
            if not include_hidden:
                if f.startswith('.') or ('/.' in location):
                    continue
            # Skip directories:
            if os.path.isfile(os.path.join(location, f)):
                extension = get_file_extension(f)
                fc.count_word(extension)


    if show_table:
        fc.show_2columns(fc.sort_by_frequency())
    else:
        fc.show_total()
