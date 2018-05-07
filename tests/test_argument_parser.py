import unittest
import os
from countfiles import parser, main_flow
from argparse import ArgumentError


class TestArgumentParser(unittest.TestCase):
    """
    Testing a parser with different arguments
    """

    def setUp(self):
        self.parser = parser

    def get_locations(self, *args):
        print('LOCATION: ', os.path.join(os.path.dirname(__file__), *args))
        return os.path.join(os.path.dirname(__file__), *args)

    def test_countfiles_fe_py(self):
        """
        Equivalent to "python countfiles.py ~/.../tests/data_for_tests -fe py"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args([self.get_locations('data_for_tests'), '-fe', 'py'])), 1)

    def test_countfiles_all_nt(self):
        """
        Equivalent to "python countfiles.py ~/.../tests/data_for_tests -a -nt"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args([self.get_locations('data_for_tests'), '-a', '-nt'])), 622)

    def test_countfiles_nt_fe_woff(self):
        """
        Equivalent to "python countfiles.py ~/.../tests/data_for_tests/django_staticfiles_for_test -nt -fe woff"
        :return:
        """
        self.assertEqual(main_flow(args=self.parser.parse_args(
            [self.get_locations('data_for_tests', 'django_staticfiles_for_test'), '-nt', '-fe', 'woff'])), 12)

    def test_countfiles_fe(self):
        """
        Equivalent to
        "python countfiles.py ~/.../tests/data_for_tests/django_staticfiles_for_test -fe {extension}"
        :return:
        """
        location = self.get_locations('data_for_tests', 'django_staticfiles_for_test')
        extensions = {'py': 0, 'json': 1, 'woff': 12}
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                args = self.parser.parse_args([location, '-fe', f'{k}'])
                self.assertEqual(main_flow(args=args), v)


# from root directory:

# run all tests in test_argument_parser.py
# python -m unittest tests/test_argument_parser.py

# run all tests for class TestArgumentParser
# python -m unittest tests.test_argument_parser.TestArgumentParser

# run test for def test_countfiles_fe in class TestArgumentParser
# python -m unittest tests.test_argument_parser.TestArgumentParser.test_countfiles_fe

# run test for def test_countfiles_all_nt in class TestArgumentParser
# python -m unittest tests.test_argument_parser.TestArgumentParser.test_countfiles_all_nt

# or run file in PyCharm

if __name__ == '__main__':
    unittest.main()
