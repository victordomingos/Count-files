import unittest
import os
from contextlib import redirect_stdout
import filecmp
from countfiles.utils.word_counter import get_files_by_extension, show_2columns
from countfiles.utils.file_handlers import count_files_by_extension


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

    def test_show_2columns(self):
        test1 = self.get_locations('compare_tables', 'test_2columns_sorted.txt')
        test2 = self.get_locations('compare_tables', 'test_2columns_most_common.txt')
        data = count_files_by_extension(dirpath=self.get_locations('data_for_tests'),
                                        include_hidden=False, recursive=True)
        with open(test1, 'w') as f:
            with redirect_stdout(f):
                show_2columns(sorted(data.items()))
        with open(test2, 'w') as f:
            with redirect_stdout(f):
                show_2columns(data.most_common())
        self.assertEqual(filecmp.cmp(test1, self.get_locations('compare_tables', '2columns_sorted.txt'),
                                     shallow=False), True)
        self.assertEqual(filecmp.cmp(test2, self.get_locations('compare_tables', '2columns_most_common.txt'),
                                     shallow=False), True)

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
