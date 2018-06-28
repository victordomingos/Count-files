#!/usr/bin/env python3

import unittest
import os
import sys
from count_files.__main__ import main_flow


class TestArgumentParser(unittest.TestCase):
    """Testing a parser with different arguments"""

    def get_locations(self, *args):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    # thread - ...or do other stuff, i.e., counting files.
    def test_countfiles_all_nt(self):
        """Testing def main_flow.

        Recursive/non recursive counting.
        Testing for hidden files is not carried out here.
        Equivalent to "python __main__.py ~/.../tests/data_for_tests -a -nt"
        :return:
        """
        self.assertEqual(main_flow([self.get_locations('data_for_tests'), '-nt']), 16)
        self.assertEqual(main_flow([self.get_locations('data_for_tests'), '-nt', '-nr']), 6)

    # thread - if search_by_extension:
    def test_countfiles_fe(self):
        """Testing def main_flow.

        Recursive default counting.
        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests/django_staticfiles_for_test -fe {extension}"
        Non recursive counting.
        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests/django_staticfiles_for_test -nr -fe {extension}"
        :return:
        """
        location = self.get_locations('data_for_tests')
        extensions = {'py': 2, 'json': 1, 'woff': 1, '.': 2, 'TXT': 3, 'txt': 3}
        nr_extensions = {'css': 0, '.': 1, 'TXT': 1, 'txt': 1}
        # case-insensitive and recursive
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(main_flow([location, '-fe', f'{k}']), v)
        # case-sensitive and non-recursive
        for k, v in nr_extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(main_flow([location, '-nr', '-c', '-fe', f'{k}']), v)

    @unittest.skipIf(sys.platform.startswith("win"), "not for Windows")
    def test_for_hidden(self):
        """Testing def main_flow.

        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests -nr"
        and "python __main__.py ~/.../tests/data_for_tests -nr -a"
        :return:
        """
        self.assertEqual(main_flow([self.get_locations('test_hidden_linux'), '-nr', '-nt']), 1)
        self.assertEqual(main_flow([self.get_locations('test_hidden_linux'), '-nr', '-nt', '-a']), 2)

    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_for_hidden_win(self):
        """Testing def main_flow.

        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests -nr"
        and "python __main__.py ~/.../tests/data_for_tests -nr -a"
        :return:
        """
        self.assertEqual(main_flow([self.get_locations('test_hidden_windows'), '-nr', '-nt']), 1)
        self.assertEqual(main_flow([self.get_locations('test_hidden_windows'), '-nr', '-nt', '-a']), 2)

# from root directory:

# run all tests in test_argument_parser.py
# python -m unittest tests/test_argument_parser.py

# run all tests for class TestArgumentParser
# python -m unittest tests.test_argument_parser.TestArgumentParser

# run test for def test_for_hidden in class TestArgumentParser
# python -m unittest tests.test_argument_parser.TestArgumentParser.test_for_hidden

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
