#!/usr/bin/env python3

import unittest
import os
import sys
from countfiles.__main__ import parser, main_flow


class TestArgumentParser(unittest.TestCase):
    """Testing a parser with different arguments"""

    def setUp(self):
        self.parser = parser

    def get_locations(self, *args):
        print('LOCATION: ', os.path.normpath(os.path.join(os.path.dirname(__file__), *args)))
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    # 2018-05-12: ignoring hidden files and directories - not implemented for Windows
    # python __main__.py ~/.../tests/data_for_tests -a -nt and
    # python __main__.py ~/.../tests/data_for_tests -nt return the same for Windows
    def test_countfiles_all_nt(self):
        """Testing def main_flow.

        Recursive default counting.
        Equivalent to "python __main__.py ~/.../tests/data_for_tests -a -nt"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests'), '-a', '-nt'])), 16)
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests'), '-a', '-nt', '-nr'])), 4)

    # 2018-05-12: ignoring hidden files and directories - not implemented for def get_files_by_extension
    # and not covered by tests for -fe
    def test_countfiles_fe_py(self):
        """Testing def main_flow.

        Recursive default counting.
        Equivalent to "python __main__.py ~/.../tests/data_for_tests -fe py"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args([self.get_locations('data_for_tests'), '-fe', 'py'])), 2)
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests'), '-fe', 'py', '-nr'])), 1)

    def test_countfiles_nt_fe_woff(self):
        """Testing def main_flow.

        Recursive default counting.
        Equivalent to "python __main__.py ~/.../tests/data_for_tests/django_staticfiles_for_test -nt -fe woff"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests', 'django_staticfiles_for_test'), '-nt', '-fe', 'woff'])), 1)
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests', 'django_staticfiles_for_test'), '-nt', '-nr', '-fe', 'woff'])), 0)

    def test_countfiles_fe(self):
        """Testing def main_flow.

        Recursive default counting.
        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests/django_staticfiles_for_test -fe {extension}"
        :return:
        """
        location = self.get_locations('data_for_tests', 'django_staticfiles_for_test')
        extensions = {'py': 1, 'json': 1, 'woff': 1}
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                args = self.parser.parse_args([location, '-fe', f'{k}'])
                self.assertEqual(main_flow(args=args), v)

    def test_countfiles_fe_dot(self):
        """Testing def main_flow.

        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests -fe . -nr"
        and "python __main__.py ~/.../tests/data_for_tests -fe ."
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests'), '-fe', '.', '-nr'])), 1)
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests'), '-fe', '.'])), 2)

    # TODO: add 1 hidden file and check it on Unix
    #@unittest.skipIf(sys.platform.startswith("win"), "not for Windows")
    def test_for_hidden(self):
        """Testing def main_flow.

        Equivalent to
        "python __main__.py ~/.../tests/data_for_tests -nr"
        and "python __main__.py ~/.../tests/data_for_tests -nr -a"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('test_hidden_linux'), '-nr', '-nt'])), 1)
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('test_hidden_linux'), '-nr', '-nt', '-a'])), 2)

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
