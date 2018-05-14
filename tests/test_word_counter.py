import unittest
import os
from countfiles.utils.word_counter import WordCounter


class TestWordCounter(unittest.TestCase):
    """Testing WordCounter class methods"""

    def setUp(self):
        self.counter = WordCounter()

    def get_locations(self, *args):
        print('LOCATION: ', os.path.normpath(os.path.join(os.path.dirname(__file__), *args)))
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    # 2018-05-12: ignoring hidden files and directories - not implemented for def get_files_by_extension
    # and not covered by tests for this function
    def test_get_files_by_extension_py(self):
        """Testing def get_files_by_extension.

        Recursively counting all files.
        Call WordCounter class method get_files_by_extension with:
        location =  ~/.../tests/data_for_tests
        file extension = py
        :return: conformity to number of .py files
        """
        self.assertEqual(self.counter.get_files_by_extension(location=self.get_locations('data_for_tests'),
                                                             extension='py', recursion=True), 2)
        self.assertEqual(self.counter.get_files_by_extension(location=self.get_locations('data_for_tests'),
                                                             extension='py', recursion=False), 1)

    def test_get_files_by_extension(self):
        """Testing def get_files_by_extension.

        Call WordCounter class method get_files_by_extension.
        with loop over dictionary:
        location =  ~/.../tests/data_for_tests
        file extension = extensions[key]
        :return: conformity to extensions[value]
        """
        location = self.get_locations('data_for_tests')
        extensions = {'py': 2, 'json': 1, 'woff': 1, '.': 2}
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(self.counter.get_files_by_extension(location=location, extension=k, recursion=True), v)

    # Return len(files)
    def test_get_files_by_extension_nr(self):
        """Testing def get_files_by_extension.

        Call WordCounter class method get_files_by_extension.
        with loop over dictionary:
        location =  ~/.../tests/data_for_tests
        file extension = extensions[key]
        :return: conformity to extensions[value]
        """
        location = self.get_locations('data_for_tests')
        extensions = {'py': 1, 'json': 0, 'woff': 0, '.': 1}
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(self.counter.get_files_by_extension(location=location, extension=k, recursion=False), v)

    def test_show_total(self):
        """Testing def show_total.

        Call WordCounter class method show_total.
        init self.counters = dict()
        total = sum(self.counters.values())
        :return:
        """
        self.assertEqual(self.counter.show_total(), 0)

    # TODO
    def test_show_2columns(self):
        self.assertEqual(self.counter.show_2columns([]), None)

# from root directory:
# run all tests in test_word_counter.py
# python -m unittest tests/test_word_counter.py
# run all tests for class TestWordCounter
# python -m unittest tests.test_word_counter.TestWordCounter
# run test for def test_get_files_by_extension in class TestWordCounter
# python -m unittest tests.test_word_counter.TestWordCounter.test_get_files_by_extension

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
