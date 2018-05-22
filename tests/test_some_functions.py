#!/usr/bin/env python3

import unittest
import os
import sys
from countfiles.utils.file_handlers import get_file_extension, \
    get_files_without_extension, non_recursive_search, recursive_search, is_hidden_file_or_dir
from countfiles.utils.file_preview import generate_preview


class TestSomeFunctions(unittest.TestCase):

    def get_locations(self, *args):
        print('LOCATION: ', os.path.normpath(os.path.join(os.path.dirname(__file__), *args)))
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    def test_get_file_extension(self):
        """Testing def get_file_extension.

        Expected behavior:
        Extract only the file extension from a given path.
        If the file name does not have an extension, return '[no extension]'.
        :return:
        """
        extensions_dict = {'file.py': ('py', True), '.gitignore': ('', False),
                           'file': ('', False), '.hidden_file.txt': ('txt', True),
                           '.hidden.file.txt': ('txt', True), 'select2.3805311d5fc1.css.gz': ('gz', True)}
        for k, v in extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(get_file_extension(k), v[0])

    # Return len==1 [WindowsPath('C:/../tests/data_for_tests/no_extension')]
    def test_get_files_without_extension(self):
        """Testing def get_files_without_extension, recursive=False.

        Expected behavior:
        Find all files in a given directory that have no extension.
        :return:
        """
        result = get_files_without_extension(path=self.get_locations('data_for_tests'), recursive=False)
        self.assertEqual(len(result), 1)

    # Return len==2 [WindowsPath('C:/.../tests/data_for_tests/no_extension'),
    # WindowsPath('C:/.../tests/data_for_tests/django_staticfiles_for_test/no_ext')]
    def test_get_files_without_extension_recursive(self):
        """Testing def get_files_without_extension, recursive=True.

         Expected behavior:
         Find all files in a given directory that have no extension.
         :return:
         """
        result = get_files_without_extension(path=self.get_locations('data_for_tests'), recursive=True)
        self.assertEqual(len(result), 2)

    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_non_recursive_search_win(self):
        result_false = non_recursive_search(self.get_locations('test_hidden_windows'), include_hidden=False)
        result_true = non_recursive_search(self.get_locations('test_hidden_windows'), include_hidden=True)
        self.assertEqual(len(result_false), 1)
        self.assertEqual(len(result_true), 2)

    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_recursive_search_win(self):
        result_false = recursive_search(self.get_locations('test_hidden_windows'), include_hidden=False)
        result_true = recursive_search(self.get_locations('test_hidden_windows'), include_hidden=True)
        self.assertEqual(len(result_false), 2)
        self.assertEqual(len(result_true), 6)

    @unittest.skipUnless(sys.platform.startswith('linux'), 'for Linux')
    def test_non_recursive_search_linux(self):
        result_false = non_recursive_search(self.get_locations('test_hidden_linux'), include_hidden=False)
        result_true = non_recursive_search(self.get_locations('test_hidden_linux'), include_hidden=True)
        self.assertEqual(len(result_false), 1)
        self.assertEqual(len(result_true), 2)

    @unittest.skipUnless(sys.platform.startswith('linux'), 'for Linux')
    def test_recursive_search_linux(self):
        result_false = recursive_search(self.get_locations('test_hidden_linux'), include_hidden=False)
        result_true = recursive_search(self.get_locations('test_hidden_linux'), include_hidden=True)
        self.assertEqual(len(result_false), 2)
        self.assertEqual(len(result_true), 6)

    @unittest.skipUnless(sys.platform.startswith('darwin'), 'for macOS')
    def test_non_recursive_search_linux(self):
        result_false = non_recursive_search(self.get_locations('test_hidden_linux'), include_hidden=False)
        result_true = non_recursive_search(self.get_locations('test_hidden_linux'), include_hidden=True)
        self.assertEqual(len(result_false), 1)
        self.assertEqual(len(result_true), 2)

    @unittest.skipUnless(sys.platform.startswith('darwin'), 'for macOS')
    def test_recursive_search_linux(self):
        result_false = recursive_search(self.get_locations('test_hidden_linux'), include_hidden=False)
        result_true = recursive_search(self.get_locations('test_hidden_linux'), include_hidden=True)
        self.assertEqual(len(result_false), 2)
        self.assertEqual(len(result_true), 6)

    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_is_hidden_file_or_dir_win(self):
        """Testing def is_hidden_file_or_dir.

        Checking the presence of FILE_ATTRIBUTE_HIDDEN for file or folder.
        Expected behavior: if any part of filepath(parent folders, final file/folder) is hidden return True
        :return:
        """
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'folder_hidden_for_win')), True)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'not_nidden_folder')), False)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'not_nidden_folder', 'hidden_for_win.xlsx')), True)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'folder_hidden_for_win', 'not_hidden.py')), True)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('os_file', '0-NonPersonalRecommendations-https∺∯∯next-services.apps.microsoft.com'
                                          '∯search∯6.3.9600-0∯776∯ru-RU_en-US.en.uk.ru∯c∯UA∯cp∯10005001∯'
                                          'BrowseLists∯lts∯5.3.4∯cid∯0∯pc∯0∯pt∯x64∯af∯0∯lf∯1.dat')), False)

    @unittest.skipUnless(sys.platform.startswith('linux')
                         or sys.platform.startswith('darwin'), 'for Linux, Mac OS')
    def test_is_hidden_file_or_dir_lin_mac(self):
        """Testing def is_hidden_file_or_dir.

        Check for the presence of a '/.' in the path.
        Expected behavior: if any part of filepath(parent folders, final file/folder) is hidden return True
        :return:
        """
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', '.ebookreader')), True)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', 'not_hidden_folder')), False)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', 'not_hidden_folder', '.hidden_for_linux')), True)
        self.assertEqual(is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', '.ebookreader', 'not_hidden.txt')), True)

    # TODO
    def test_generate_preview(self):
        pass

# from root directory:

# run all tests in test_some_functions.py
# python -m unittest tests/test_some_functions.py

# run all tests for class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions

# run test for def test_non_recursive_search in class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions.test_non_recursive_search

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
