import unittest
import os
from countfiles.utils.word_counter import WordCounter


class TestWordCounter(unittest.TestCase):
    """
    Testing WordCounter class methods
    """

    def setUp(self):
        self.counter = WordCounter()

    def get_locations(self, *args):
        print('LOCATION: ', os.path.join(os.path.dirname(__file__), *args))
        return os.path.join(os.path.dirname(__file__), *args)

    def test_get_files_by_extension_py(self):
        """
        Recursively counting all files.
        Call WordCounter class methods get_files_by_extension
        with:
        location =  ~/.../tests/data_for_tests
        file extension = py
        :return: conformity to number of .py files
        """
        self.assertEqual(self.counter.get_files_by_extension(location=self.get_locations('data_for_tests'),
                                                             extension='py', recursion=True), 1)

    def test_get_files_by_extension(self):
        """
        Recursively counting all files.
        Call WordCounter class methods get_files_by_extension
        with loop over dictionary:
        location =  ~/.../tests/data_for_tests/django_staticfiles_for_test
        file extension = extensions[key]
        :return: conformity to extensions[value]
        """
        location = self.get_locations('data_for_tests', 'django_staticfiles_for_test')
        extensions = {'py': 0, 'json': 1, 'woff': 12}
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(self.counter.get_files_by_extension(location=location, extension=k, recursion=True), v)

    def test_show_total(self):
        """
        init self.counters = dict()
        :return:
        """
        self.assertEqual(self.counter.show_total(), 0)


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
