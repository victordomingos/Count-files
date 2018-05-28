import unittest
import os
from countfiles.utils.word_counter import get_files_by_extension, show_2columns


class TestWordCounter(unittest.TestCase):
    """Testing word_counter.py functions"""

    def get_locations(self, *args):
        print('LOCATION: ', os.path.normpath(os.path.join(os.path.dirname(__file__), *args)))
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    # Testing the result of this function is not necessary now,
    # because it duplicates the tests for def search_files, def human_mem_size and def generate_preview.
    def test_get_files_by_extension(self):
        """Testing def get_files_by_extension.

        :return:
        """
        pass

    # TODO
    def test_show_2columns(self):
        self.assertEqual(show_2columns([]), None)

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
