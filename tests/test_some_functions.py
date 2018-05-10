import unittest
import os
from countfiles.utils.file_handlers import get_file_extension
from countfiles.utils.file_handlers import get_files_without_extension_path, get_files_without_extension_scandir
from countfiles.utils.word_counter import WordCounter

class TestSomeFunctions(unittest.TestCase):

    def setUp(self):
        self.extensions_dict = {'file.py': 'py', 'file.png': 'png', '.gitignore': '[no extension]', 'file': '[no extension]'}

    def get_locations(self, *args):
        print('LOCATION: ', os.path.join(os.path.dirname(__file__), *args))
        return os.path.join(os.path.dirname(__file__), *args)

    def test_get_file_extension(self):
        for k, v in self.extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(get_file_extension(k), v)

    # LOCATION: ~/tests/data_for_tests for both, location contains 1 file without extension
    # Return [WindowsPath('C:/../tests/data_for_tests/no_extension')]. Don't recurse through subdirectories.
    @unittest.expectedFailure
    def test_get_files_without_extension_path(self):
        self.assertEqual(get_files_without_extension_path(path=self.get_locations('data_for_tests')), [])

    # Return [<DirEntry 'no_extension'>]. Don't recurse through subdirectories.
    @unittest.expectedFailure
    def test_get_files_without_extension_scandir(self):
        self.assertEqual(get_files_without_extension_scandir(path=self.get_locations('data_for_tests')), [])

    # Return len(files). Don't recurse through subdirectories.
    def test_get_files_by_extension_for_no_ext(self):
        self.assertEqual(WordCounter.get_files_by_extension(location=self.get_locations('data_for_tests'),
                                                            extension='.', recursion=False), 1)


# from root directory:

# run all tests in test_some_functions.py
# python -m unittest tests/test_some_functions.py

# run all tests for class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions

# run test for def test_get_file_extension in class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions.test_get_file_extension

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
