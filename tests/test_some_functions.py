import unittest
import os
import sys
from countfiles.utils.file_handlers import get_file_extension, has_extension,\
    get_files_without_extension, non_recursive_search, recursive_search


class TestSomeFunctions(unittest.TestCase):

    def setUp(self):
        self.extensions_dict = {'file.py': ('py', True), '.gitignore': ('[no extension]', False),
                                'file': ('[no extension]', False), '.hidden_file.txt': ('txt', True),
                                '.hidden.file.txt': ('txt', True), 'select2.3805311d5fc1.css.gz': ('gz', True)}

    def get_locations(self, *args):
        print('LOCATION: ', os.path.join(os.path.dirname(__file__), *args))
        return os.path.join(os.path.dirname(__file__), *args)

    def test_get_file_extension(self):
        """Testing def get_file_extension.

        Expected behavior:
        Extract only the file extension from a given path.
        If the file name does not have an extension, return '[no extension]'.
        :return:
        """
        for k, v in self.extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(get_file_extension(k), v[0])

    def test_has_extension(self):
        """Testing def has_extension.

        Expected behavior:
        Check if a filename has an extension, return bool.
        :return:
        """
        for k, v in self.extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(has_extension(self.get_locations('data_for_tests', k)), v[1])

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

    # only hidden files, hidden folders are not processed in def non_recursive_search for Windows
    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_non_recursive_search_win(self):
        result_false = non_recursive_search(self.get_locations('test_hidden_windows'), platform_name='win', hidden=False)
        result_true = non_recursive_search(self.get_locations('test_hidden_windows'), platform_name='win', hidden=True)
        self.assertEqual(len(result_false), 1)
        self.assertEqual(len(result_true), 2)

    # only hidden files, hidden folders are not processed in def recursive_search for Windows
    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_recursive_search_win(self):
        result_false = recursive_search(self.get_locations('test_hidden_windows'), platform_name='win', hidden=False)
        result_true = recursive_search(self.get_locations('test_hidden_windows'), platform_name='win', hidden=True)
        self.assertEqual(len(result_false), 3)
        self.assertEqual(len(result_true), 6)

    # hidden files and folders
    @unittest.skipUnless(sys.platform.startswith('linux'), 'for Linux')
    def test_non_recursive_search_linux(self):
        result_false = non_recursive_search(self.get_locations('test_hidden_linux'), platform_name='linux', hidden=False)
        result_true = non_recursive_search(self.get_locations('test_hidden_linux'), platform_name='linux', hidden=True)
        self.assertEqual(len(result_false), 1)
        self.assertEqual(len(result_true), 2)

    # hidden files and folders
    @unittest.skipUnless(sys.platform.startswith('linux'), 'for Linux')
    def test_recursive_search_linux(self):
        result_false = recursive_search(self.get_locations('test_hidden_linux'), platform_name='linux', hidden=False)
        result_true = recursive_search(self.get_locations('test_hidden_linux'), platform_name='linux', hidden=True)
        self.assertEqual(len(result_false), 2)
        self.assertEqual(len(result_true), 6)

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
