#!/usr/bin/env python3

import unittest
import os
import sys
from count_files.utils.file_handlers import get_file_extension,\
    is_hidden_file_or_dir, search_files, count_files_by_extension
from count_files.utils.file_preview import generate_preview


class TestSomeFunctions(unittest.TestCase):

    def get_locations(self, *args):
        print('LOCATION: ', os.path.normpath(os.path.join(os.path.dirname(__file__), *args)))
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    def test_get_file_extension(self):
        """Testing def get_file_extension.

        Extract only the file extension from a given path.
        Expected behavior: return extension name (txt, py) or '.' (for files without extension)
        :return:
        """
        extensions_dict = {'file.py': ('py', True), '.gitignore': ('.', False),
                           'file': ('.', False), '.hidden_file.txt': ('txt', True),
                           '.hidden.file.txt': ('txt', True), 'select2.3805311d5fc1.css.gz': ('gz', True)}
        for k, v in extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(get_file_extension(k), v[0])

    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_search_files_win(self):
        """Testing def search_files, def search_files returns generator.

        Expected behavior: return list with strings(full paths to files)
        """
        a = list(f for f in search_files(self.get_locations('hidden_py'), 'py', recursive=True, include_hidden=True))
        b = list(f for f in search_files(self.get_locations('hidden_py'), 'py', recursive=False, include_hidden=False))
        c = list(f for f in search_files(self.get_locations('hidden_py'), 'py', recursive=False, include_hidden=True))
        d = list(f for f in search_files(self.get_locations('hidden_py'), 'py', recursive=True, include_hidden=False))
        self.assertEqual(len(a), 4)
        self.assertEqual(len(b), 1)
        self.assertEqual(len(c), 2)
        self.assertEqual(len(d), 1)

    @unittest.skipUnless(sys.platform.startswith('linux')
                         or sys.platform.startswith('darwin'), 'for Linux, Mac OS')
    def test_search_files_lin_mac(self):
        """Testing def search_files, def search_files returns generator.

        Expected behavior: return list with strings(full paths to files)
        """
        a = list(f for f in search_files(self.get_locations('test_hidden_linux'), '.', recursive=True, include_hidden=True))
        b = list(f for f in search_files(self.get_locations('test_hidden_linux'), '.', recursive=False, include_hidden=False))
        c = list(f for f in search_files(self.get_locations('test_hidden_linux'), '.', recursive=False, include_hidden=True))
        d = list(f for f in search_files(self.get_locations('test_hidden_linux'), '.', recursive=True, include_hidden=False))
        self.assertEqual(len(a), 3)
        self.assertEqual(len(b), 0)
        self.assertEqual(len(c), 1)
        self.assertEqual(len(d), 0)

    def test_count_files_by_extension(self):
        """Testing def count_files_by_ext.

        Expected behavior: return object <class 'collections.Counter'>
        :return:
        """
        result = count_files_by_extension(self.get_locations('data_for_tests'), no_feedback=True,
                                          recursive=False, include_hidden=False)
        self.assertEqual(str(result), "Counter({'html': 1, 'md': 1, '[no extension]': 1, 'py': 1})")

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
