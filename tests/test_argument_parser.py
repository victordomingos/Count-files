#!/usr/bin/env python3
import unittest
import os

from count_files.__main__ import main_flow
from count_files.platforms import get_current_os


class TestArgumentParser(unittest.TestCase):
    """Testing a parser with different arguments"""

    def get_locations(self, *args):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    # counting total number of files
    def test_countfiles_all_t(self):
        """Testing def main_flow.

        Recursive/non recursive counting.
        Testing for hidden files is not carried out here.
        There are no hidden files or folders in data_for_tests.
        Equivalent to "count-files ~/.../tests/data_for_tests -a -t .."
        Passed: path exists and not hidden.
        :return:
        """
        self.assertEqual(main_flow([self.get_locations('data_for_tests'), '-t', '..']), 16)
        self.assertEqual(main_flow([self.get_locations('data_for_tests'), '-t', '..', '-nr']), 6)

    # search by extension
    def test_countfiles_fe(self):
        """Testing def main_flow.

        Recursive default counting.
        Equivalent to
        "count-files ~/.../tests/data_for_tests/django_staticfiles_for_test -fe {extension}"
        Non recursive counting.
        Equivalent to
        "count-files ~/.../tests/data_for_tests/django_staticfiles_for_test -nr -fe {extension}"
        There are no hidden files or folders in data_for_tests.
        Passed: path exists and not hidden.
        :return:
        """
        location = self.get_locations('data_for_tests')
        extensions = {'py': 2, 'json': 1, 'woff': 1, '.': 2, 'TXT': 3, 'txt': 3, '..': 16}
        nr_extensions = {'css': 0, '.': 1, 'TXT': 1, 'txt': 1, '..': 6}
        # case-insensitive and recursive
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(main_flow([location, '-fe', f'{k}']), v)
        # case-sensitive and non-recursive
        for k, v in nr_extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(main_flow([location, '-nr', '-c', '-fe', f'{k}']), v)

    def test_countfiles_fe_and_preview(self):
        """Testing def main_flow.

        Passed: --preview for supported types.
        Not a visual presentation(other tests), but the fact that there is no SystemExit.
        :return:
        """
        location = self.get_locations('data_for_tests')
        extensions = {'json': 1, 'TXT': 3, '..': 16}
        # case-insensitive and recursive + preview
        for k, v in extensions.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(main_flow([location, '-fe', f'{k}', '-p', '-ps', '5']), v)

    # tests for hidden files: Windows, Linux, Mac OS, iOS, Haiku; skip: BaseOS
    def test_for_hidden(self):
        """Testing def main_flow.

        Equivalent to
        "count-files ~/.../tests/data_for_tests -nr -t .."
        and "count-files ~/.../tests/data_for_tests -nr -a -t .."
        :return:
        """
        current_os = get_current_os()
        if current_os.name == 'WinOS':
            self.assertEqual(main_flow([self.get_locations('test_hidden_windows'), '-nr', '-t', '..']), 1)
            self.assertEqual(main_flow([self.get_locations('test_hidden_windows'), '-nr', '-t', '..', '-a']), 2)
        elif current_os.name == 'UnixOS':
            self.assertEqual(main_flow([self.get_locations('test_hidden_linux'), '-nr', '-t', '..']), 1)
            self.assertEqual(main_flow([self.get_locations('test_hidden_linux'), '-nr', '-t', '..', '-a']), 2)
        else:
            # raise unittest exception
            self.skipTest('For BaseOS, hidden file detection is currently not available.')

    # SystemExit, parser.exit(status=0). No files were found.
    def test_parser_exit_no_data(self):
        """Testing def main_flow. Count group.

        No files were found in the specified directory.
        :return:
        """
        try:
            # count group, if not data
            location = self.get_locations('data_for_tests', 'django_staticfiles_for_test', 'admin', 'css')
            main_flow([location, '-nr'])
        except SystemExit as e:
            # not error, the folder is empty
            self.assertEqual(e.code, 0)

    # SystemExit, parser.exit(status=1). The path does not exist, Preview for an unsupported file type.
    def test_parser_exit(self):
        """Check if all checks are performed in CLI.

        1-2-3)The path does not exist, or there may be a typo in it.
        4)Preview for an unsupported file type(no extension).
        5)Preview for an unsupported file type(not in SUPPORTED_TYPES).
        :return:
        """
        args_dict = {(self.get_locations('not_exists'),): 1,
                     (self.get_locations('not_exists'), '-t', 'txt'): 1,
                     (self.get_locations('not_exists'), '-fe', '..'): 1,
                     # -fe used, no preview to count and -t
                     (self.get_locations('data_for_tests'), '-fe', '.', '-p'): 1,
                     (self.get_locations('data_for_tests'), '-fe', 'woff', '-p'): 1}
        for k, v in args_dict.items():
            with self.subTest(k=k, v=v):
                try:
                    main_flow(k)
                # should return parser.exit(status=1)
                except SystemExit as se:
                    # main_flow return parser.exit(status=0) for count_group if check is not effected in CLI
                    self.assertEqual(se.code, v)
                except Exception as e:
                    self.fail(f'Unexpected exception raised: {e}')
                else:
                    # main_flow return total_result for --total if check is not effected in CLI
                    # main_flow return len(files) for -fe .. if check is not effected in CLI
                    self.fail('SystemExit not raised')

    # SystemExit, parser.exit(status=1). Not counting any files, because location include hidden folders.
    def test_parser_exit_for_hidden(self):
        """Check if all checks are performed in CLI.

        If include_hidden=False and hidden folder in path:
        In this case, the hidden folder is skipped(default settings)
        and, accordingly, the files are not count at all.
        TODO: revise the check for cases when:
        count-files ~/Documents/not_hidden_subfolder/hidden_folder
        You can count files in Documents, not_hidden_subfolder and not count them in a hidden_folder.
        :return:
        """
        current_os = get_current_os()
        # if not include_hidden and current_os.is_hidden_file_or_dir(location)
        if current_os.name == 'WinOS':
            args_dict = {(self.get_locations('test_hidden_windows', 'folder_hidden_for_win'),): 1,
                         (self.get_locations('test_hidden_windows', 'folder_hidden_for_win'), '-t', 'txt'): 1,
                         (self.get_locations('test_hidden_windows', 'folder_hidden_for_win'), '-fe', '..'): 1}
        elif current_os.name == 'UnixOS':
            args_dict = {(self.get_locations('test_hidden_linux', '.ebookreader'),): 1,
                         (self.get_locations('test_hidden_linux', '.ebookreader'), '-t', 'txt'): 1,
                         (self.get_locations('test_hidden_linux', '.ebookreader'), '-fe', '..'): 1}
        else:
            # raise unittest exception
            self.skipTest('For BaseOS, hidden file detection is currently not available.')

        for k, v in args_dict.items():
            with self.subTest(k=k, v=v):
                try:
                    main_flow(k)
                # should return parser.exit(status=1)
                except SystemExit as se:
                    # main_flow return parser.exit(status=0) for count_group if check is not effected in CLI
                    self.assertEqual(se.code, v)
                except Exception as e:
                    self.fail(f'Unexpected exception raised: {e}')
                else:
                    # main_flow return total_result for --total if check is not effected in CLI
                    # main_flow return len(files) for -fe .. if check is not effected in CLI
                    self.fail('SystemExit not raised')


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
