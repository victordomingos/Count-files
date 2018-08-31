#!/usr/bin/env python3
import unittest
import os
import sys
from contextlib import redirect_stdout
import filecmp

from count_files.utils.viewing_modes import show_2columns, show_result_for_search_files, show_start_message
from count_files.utils.file_handlers import count_files_by_extension, search_files


class TestViewingModes(unittest.TestCase):
    """Testing viewing_modes.py functions"""

    def setUp(self):
        self.test_file = self.get_locations('compare_tables', 'test_show_result_list.txt')
        if sys.platform.startswith('win'):
            self.standard_file = self.get_locations('compare_tables', 'win_show_result_list.txt')
        elif sys.platform.startswith('linux'):
            self.standard_file = self.get_locations('compare_tables', 'linux_show_result_list.txt')
        elif sys.platform.startswith('darwin'):
            self.standard_file = self.get_locations('compare_tables', 'darwin_show_result_list.txt')

    def get_locations(self, *args):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    def generate_standard_file(self):
        with open(self.standard_file, 'w') as f:
            f.write(f"{self.get_locations('data_for_tests', 'no_extension')} (49.0 B)\n")
            f.write(f"{self.get_locations('data_for_tests', 'django_staticfiles_for_test', 'no_ext')} (0.0 B)\n")
            f.write('\n')
            f.write('   Found 2 file(s).\n')
            f.write('   Total combined size: 49.0 B.\n')
            f.write('   Average file size: 24.0 B (max: 49.0 B, min: 0.0 B).\n\n')
        return

    def test_show_2columns(self):
        """Testing def show_2columns(compare files with tables).

        Comparison of the file with the results of the function with the specified file.
        standard: 2columns_sorted.txt and 2columns_most_common.txt
        results of the function: test_2columns_sorted.txt and test_2columns_most_common.txt
        :return:
        """
        test1 = self.get_locations('compare_tables', 'test_2columns_sorted.txt')
        test2 = self.get_locations('compare_tables', 'test_2columns_most_common.txt')
        data = count_files_by_extension(dirpath=self.get_locations('data_for_tests'), no_feedback=True,
                                        include_hidden=False, recursive=True)

        with open(test1, 'w') as f:
            with redirect_stdout(f):
                show_2columns(sorted(data.items()), max_word_width=14, total_occurrences=16)
        with open(test2, 'w') as f:
            with redirect_stdout(f):
                show_2columns(data.most_common(), max_word_width=14, total_occurrences=16)
        self.assertEqual(filecmp.cmp(test1, self.get_locations('compare_tables', '2columns_sorted.txt'),
                                     shallow=False), True)
        self.assertEqual(filecmp.cmp(test2, self.get_locations('compare_tables', '2columns_most_common.txt'),
                                     shallow=False), True)

    # TODO:  test show_result_for_search_files() for different OS
    # compare lists with paths and file sizes
    def test_show_result_for_search_files(self):
        """Testing def show_result_for_search_files. Search by extension.

        Comparison of the file with the results of the function with the specified file.
        Note: for different OS and PC lists will be different!
        Preconditions: create standard file for a particular PC
        Expected behavior: List with paths and file sizes.

        full/path/to/file1.extension (... KiB)
        full/path/to/file2.extension (... KiB)
        ...
        Found ... file(s).
        Total combined size: ... KiB.
        Average file size: ... KiB (max: ... KiB, min: ... B).
        :return:
        """
        if not os.path.exists(self.standard_file):
            print('A standard file is generated.')
            self.generate_standard_file()
        data = search_files(dirpath=self.get_locations('data_for_tests'), extension='.',
                            include_hidden=False, recursive=True, case_sensitive=False)
        with open(self.test_file, 'w') as f:
            with redirect_stdout(f):
                show_result_for_search_files(files=data, file_sizes=True)
        self.assertEqual(filecmp.cmp(self.test_file, self.standard_file,
                                     shallow=False), True)

    def test_show_start_message(self):
        """Testing def show_start_message. Count, search, total group.

        :return:
        """
        count = show_start_message(value=None, case_sensitive=False, recursive=True, include_hidden=False,
                                   location='/some/path', group=None)
        search = show_start_message(value='.', case_sensitive=False, recursive=False, include_hidden=False,
                                    location='/some/path', group=None)
        total = show_start_message(value='TXT', case_sensitive=True, recursive=True, include_hidden=True,
                                   location='/some/path', group='total')
        self.assertEqual(count, '\nRecursively counting all files, '
                                'ignoring hidden files and directories, in /some/path\n')
        self.assertEqual(search, '\nSearching files without any extension, '
                                 'ignoring hidden files and directories, in /some/path\n')
        self.assertEqual(total, '\nRecursively counting total number of files with (case-sensitive) extension .TXT, '
                                'including hidden files and directories, in /some/path\n')

# from root directory:
# run all tests in test_viewing_modes.py
# python -m unittest tests/test_viewing_modes.py
# run all tests for class TestViewingModes
# python -m unittest tests.test_viewing_modes.TestViewingModes
# run test for def test_show_2columns in class TestViewingModes
# python -m unittest tests.test_word_counter.TestViewingModes.test_show_2columns

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
