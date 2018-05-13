import unittest
import os
from countfiles.utils.file_handlers import get_file_extension, has_extension
from countfiles.utils.file_handlers import get_files_without_extension


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


# from root directory:

# run all tests in test_some_functions.py
# python -m unittest tests/test_some_functions.py

# run all tests for class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions

# run test for def test_get_file_extension in class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions.test_has_extension

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
