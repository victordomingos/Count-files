import unittest
from utils.file_handlers import get_file_extension


class TestSomeFunctions(unittest.TestCase):

    def setUp(self):
        self.extensions_dict = {'file.py': 'py', 'file.png': 'png', '.gitignore': 'gitignore', 'file': '[no extension]'}

    def test_get_file_extension(self):
        for k, v in self.extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(get_file_extension(k), v)


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
