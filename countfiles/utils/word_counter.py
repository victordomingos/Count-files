#!/usr/bin/env python3

import os
from collections import Counter
from pathlib import Path

from countfiles.utils.file_handlers import human_mem_size, is_hidden_file_or_dir
from countfiles.utils.file_handlers import get_files_without_extension
from countfiles.utils.file_handlers import get_files_with_extension
from countfiles.utils.file_preview import generate_preview


class WordCounter:

    def __init__(self):
        self.counters = Counter()


    def count_word(self, word: str):
        """ Add a new word or increment the counter for an existing one. """
        self.counters[word] += 1


    def sort_by_frequency(self):
        return self.counters.most_common()


    def sort_by_word(self):
        return sorted(self.counters.items())


    @staticmethod
    def show_2columns(data):
        if len(data) == 0:
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


    def show_total(self) -> int:
        total = sum(self.counters.values())
        print(f"Total number of files in selected directory: {total}.\n")
        return total


    @staticmethod
    def get_files_by_extension(location: str, extension: str, preview=False, preview_size=395,
                               recursion=True, include_hidden=False) -> int:
        """ Search for files that have the given extension in their filename and optionally display
        a preview of the file.

        Special thanks to Natalia Bondarenko (github.com/NataliaBondarenko),
        who suggested this feature and submited an initial implementation.
        """
        if recursion:
            if extension == '.':
                print(f'\nRecursively searching for files without extension in {location}.\n')
                files = get_files_without_extension(location, recursive=True,
                                                    include_hidden=include_hidden)
            else:
                print(f'\nRecursively searching for .{extension} files in {location}.\n')
                files = get_files_with_extension(location, extension, recursive=True,
                                                 include_hidden=include_hidden)

        else:
            if extension == '.':
                print(f'\nSearching for files without extension in {location}.\n')
                files = get_files_without_extension(location, recursive=False,
                                                    include_hidden=include_hidden)
            else:
                print(f'\nSearching for .{extension} files in {location}.\n')
                if include_hidden:
                    files = sorted([f for f
                                    in Path(os.path.expanduser(location)).glob(f"*.{extension}")
                                    if f.is_file()])
                else:
                    files = sorted([f for f
                                    in Path(os.path.expanduser(location)).glob(f"*.{extension}")
                                    if f.is_file() and not is_hidden_file_or_dir(f)])

        if files:
            sizes = []
            for f_path in files:
                f = Path(f_path)
                file_size = f.stat().st_size
                sizes.append(file_size)
                filepath = str(f).strip("\r")
                print(f'{filepath} ({human_mem_size(file_size)})')
                if preview:
                    print('–––––––––––––––––––––––––––––––––––')
                    print(generate_preview(str(f), max_size=preview_size))
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
