#!/usr/bin/env python3
import unittest
import os
import sys
from collections import Counter

from count_files.utils.file_handlers import get_file_extension, group_ext_by_type
from count_files.platforms import get_current_os
from count_files.utils.file_preview import generate_preview, generic_text_preview


current_os = get_current_os()


class TestSomeFunctions(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def get_locations(self, *args):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), *args))

    def test_get_file_extension(self):
        """Testing def get_file_extension.

        Extract only the file extension from a given path.
        Expected behavior: return extension name (txt, py) or '.' (for files without extension)
        :return:
        """
        extensions_dict = {'file.py': 'py', '.gitignore': '.', 'image.JPG': 'JPG',
                           'file': '.', '.hidden_file.txt': 'txt',
                           '.hidden.file.txt': 'txt', 'select2.3805311d5fc1.css.gz': 'gz'
                           }
        for k, v in extensions_dict.items():
            with self.subTest(k=k, v=v):
                self.assertEqual(get_file_extension(k, case_sensitive=True), v)

    # test case_sensitive param (search, count, total)
    def test_search_files_case_sensitive(self):
        """Testing def search_files, case_sensitive param. For all OS.

        :return:
        if not case_sensitive: returns a list with all found files(txt, TXT, Txt and so on).
        if case_sensitive: returns a list of files with extensions that exactly match the query.
        """
        a = list(f for f in current_os.search_files(self.get_locations('data_for_tests'),
                                                    'txt', recursive=False,
                                                    include_hidden=False, case_sensitive=False))
        b = list(f for f in current_os.search_files(self.get_locations('data_for_tests'),
                                                    'txt', recursive=False,
                                                    include_hidden=False, case_sensitive=True))
        c = list(f for f in current_os.search_files(self.get_locations('data_for_tests'),
                                                    'TXT', recursive=False,
                                                    include_hidden=False, case_sensitive=True))
        d = list(f for f in current_os.search_files(self.get_locations('data_for_tests'),
                                                    'Txt', recursive=False,
                                                    include_hidden=False, case_sensitive=False))
        self.assertEqual(len(a), 2)
        self.assertEqual(len(b), 1)
        self.assertEqual(len(c), 1)
        self.assertEqual(len(d), 2)

    def test_count_files_by_extension_case_sensitive(self):
        """Testing def count_files_by_extension, case_sensitive and recursive params. For all OS.

        Expected behavior: return object <class 'collections.Counter'>
        :return:
        """
        counter = Counter({'TXT': 2, 'HTML': 1, 'MD': 1, '[no extension]': 1, 'PY': 1})
        counter1 = Counter({'gz': 3, 'txt': 2, 'md': 2, '[no extension]': 2, 'py': 2,
                           'TXT': 1, 'html': 1, 'json': 1, 'css': 1, 'woff': 1})
        result = current_os.count_files_by_extension(self.get_locations('data_for_tests'),
                                                     no_feedback=True, recursive=False,
                                                     include_hidden=False, case_sensitive=False)
        result1 = current_os.count_files_by_extension(self.get_locations('data_for_tests'),
                                                      no_feedback=True, recursive=True,
                                                      include_hidden=False, case_sensitive=True)
        self.assertEqual(result, counter)
        self.assertEqual(result1, counter1)

    # tests for is_hidden_file_or_dir()
    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_is_hidden_file_or_dir_win(self):
        """Testing def is_hidden_file_or_dir.

        Checking the presence of FILE_ATTRIBUTE_HIDDEN for file or folder.
        Expected behavior: if any part of filepath(parent folders, final file/folder) is hidden return True
        :return:
        """
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'folder_hidden_for_win')), True)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'not_nidden_folder')), False)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'not_nidden_folder', 'hidden_for_win.xlsx')), True)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_windows', 'folder_hidden_for_win', 'not_hidden.py')), True)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('os_file', '0-NonPersonalRecommendations-https∺∯∯next-services.apps.microsoft.com'
                                          '∯search∯6.3.9600-0∯776∯ru-RU_en-US.en.uk.ru∯c∯UA∯cp∯10005001∯'
                                          'BrowseLists∯lts∯5.3.4∯cid∯0∯pc∯0∯pt∯x64∯af∯0∯lf∯1.dat')), False)

    @unittest.skipUnless(sys.platform.startswith('linux')
                         or sys.platform.startswith('darwin') or sys.platform.startswith('haiku'), 'for Linux, Mac OS')
    def test_is_hidden_file_or_dir_lin_mac(self):
        """Testing def is_hidden_file_or_dir.

        Check for the presence of a '/.' in the path.
        Expected behavior: if any part of filepath(parent folders, final file/folder) is hidden return True
        :return:
        """
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', '.ebookreader')), True)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', 'not_hidden_folder')), False)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', 'not_hidden_folder', '.hidden_for_linux')), True)
        self.assertEqual(current_os.is_hidden_file_or_dir(
            self.get_locations('test_hidden_linux', '.ebookreader', 'not_hidden.txt')), True)

    # tests related to preview
    # TODO
    def test_generate_preview(self):
        pass

    def test_generic_text_preview_errors(self):
        # win denied_result: TEXT_PREVIEW_ERROR: [Errno 13] Permission denied: 'path\to\data_for_tests'
        denied_result = generic_text_preview(filepath=self.get_locations('data_for_tests'), max_size=1)
        # win no_file: TEXT_PREVIEW_ERROR: [Errno 2] No such file or directory: 'path\to\data_for_tests\no'
        no_file = generic_text_preview(filepath=self.get_locations('data_for_tests', 'no'), max_size=1)
        # win not_implemented: TEXT_PREVIEW_ERROR: 'charmap' codec can't decode byte 0x98 in position 579:
        # character maps to <undefined>
        not_implemented = generic_text_preview(
            filepath=self.get_locations('data_for_tests', 'django_staticfiles_for_test', 'admin',
                                        'fonts', 'LICENSE.txt.gz'), max_size=1)
        self.assertEqual('TEXT_PREVIEW_ERROR' in denied_result, True)
        self.assertEqual('TEXT_PREVIEW_ERROR' in no_file, True)
        self.assertEqual('TEXT_PREVIEW_ERROR' in not_implemented, True)

    def test_generic_text_preview_excerpt(self):
        empty_file = generic_text_preview(filepath=self.get_locations(
            'data_for_tests', 'ext_in_lowercase.txt'), max_size=1)
        excerpt_result = generic_text_preview(filepath=self.get_locations(
            'data_for_tests', 'py_file_for_tests.py'), max_size=1)
        self.assertEqual(empty_file, '')
        self.assertEqual(excerpt_result, '#')

    # tests related to hidden folders and files (search, count, total)
    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_search_files_win(self):
        """Testing def search_files, include_hidden and recursive params.

        def search_files returns generator.
        Expected behavior: return list with strings(full paths to files)
        """
        a = list(f for f in current_os.search_files(self.get_locations('hidden_py'),
                                                    'py', recursive=True,
                                                    include_hidden=True, case_sensitive=False))
        b = list(f for f in current_os.search_files(self.get_locations('hidden_py'),
                                                    'py', recursive=False,
                                                    include_hidden=False, case_sensitive=False))
        c = list(f for f in current_os.search_files(self.get_locations('hidden_py'),
                                                    'py', recursive=False,
                                                    include_hidden=True, case_sensitive=False))
        d = list(f for f in current_os.search_files(self.get_locations('hidden_py'),
                                                    'py', recursive=True,
                                                    include_hidden=False, case_sensitive=False))
        self.assertEqual(len(a), 4)
        self.assertEqual(len(b), 1)
        self.assertEqual(len(c), 2)
        self.assertEqual(len(d), 1)

    @unittest.skipUnless(sys.platform.startswith('linux')
                         or sys.platform.startswith('darwin') or sys.platform.startswith('haiku'), 'for Linux, Mac OS')
    def test_search_files_lin_mac(self):
        """Testing def search_files, include_hidden and recursive params.

        def search_files returns generator.
        Expected behavior: return list with strings(full paths to files)
        """
        a = list(f for f in current_os.search_files(self.get_locations('test_hidden_linux'),
                                                    '.', recursive=True,
                                                    include_hidden=True, case_sensitive=False))
        b = list(f for f in current_os.search_files(self.get_locations('test_hidden_linux'),
                                                    '.', recursive=False,
                                                    include_hidden=False, case_sensitive=False))
        c = list(f for f in current_os.search_files(self.get_locations('test_hidden_linux'),
                                                    '.', recursive=False,
                                                    include_hidden=True, case_sensitive=False))
        d = list(f for f in current_os.search_files(self.get_locations('test_hidden_linux'),
                                                    '.', recursive=True,
                                                    include_hidden=False, case_sensitive=False))
        self.assertEqual(len(a), 3)
        self.assertEqual(len(b), 0)
        self.assertEqual(len(c), 1)
        self.assertEqual(len(d), 0)

    @unittest.skipUnless(sys.platform.startswith('win'), 'for Windows')
    def test_count_files_by_extension_win(self):
        """Testing def count_files_by_extension, include_hidden and recursive params.

        Expected behavior: return object <class 'collections.Counter'>
        :return:
        """
        counter = Counter({'TXT': 1, 'XLSX': 1})
        counter1 = Counter({'txt': 2, 'py': 2, 'xlsx': 2})
        counter2 = Counter({'TXT': 1})
        counter3 = Counter({'txt': 2})
        result_r = current_os.count_files_by_extension(
            self.get_locations('test_hidden_windows'), no_feedback=True,
            recursive=True, include_hidden=False, case_sensitive=False)
        result_r_hidden = current_os.count_files_by_extension(
            self.get_locations('test_hidden_windows'), no_feedback=True,
            recursive=True, include_hidden=True, case_sensitive=True)
        result_nr = current_os.count_files_by_extension(
            self.get_locations('test_hidden_windows'), no_feedback=True,
            recursive=False, include_hidden=False, case_sensitive=False)
        result_nr_hidden = current_os.count_files_by_extension(
            self.get_locations('test_hidden_windows'), no_feedback=True,
            recursive=False, include_hidden=True, case_sensitive=True)
        self.assertEqual(result_r, counter)
        self.assertEqual(result_r_hidden, counter1)
        self.assertEqual(result_nr, counter2)
        self.assertEqual(result_nr_hidden, counter3)

    @unittest.skipUnless(sys.platform.startswith('linux')
                         or sys.platform.startswith('darwin') or sys.platform.startswith('haiku'), 'for Linux, Mac OS')
    def test_count_files_by_extension_lin_mac(self):
        """Testing def count_files_by_extension, include_hidden and recursive params.

        Expected behavior: return object <class 'collections.Counter'>
        :return:
        """
        counter = Counter({'TXT': 2})
        counter1 = Counter({'[no extension]': 3, 'TXT': 3})
        counter2 = Counter({'TXT': 1})
        counter3 = Counter({'[no extension]': 1, 'TXT': 1})
        result_r = current_os.count_files_by_extension(
            self.get_locations('test_hidden_linux'), no_feedback=True,
            recursive=True, include_hidden=False, case_sensitive=False)
        result_r_hidden = current_os.count_files_by_extension(
            self.get_locations('test_hidden_linux'), no_feedback=True,
            recursive=True, include_hidden=True, case_sensitive=False)
        result_nr = current_os.count_files_by_extension(
            self.get_locations('test_hidden_linux'), no_feedback=True,
            recursive=False, include_hidden=False, case_sensitive=False)
        result_nr_hidden = current_os.count_files_by_extension(
            self.get_locations('test_hidden_linux'), no_feedback=True,
            recursive=False, include_hidden=True, case_sensitive=False)
        self.assertEqual(result_r, counter)
        self.assertEqual(result_r_hidden, counter1)
        self.assertEqual(result_nr, counter2)
        self.assertEqual(result_nr_hidden, counter3)

    def test_search_files_by_pattern(self):
        """Testing def search_files_by_pattern.

        Search for file names matching given pattern(including extension).
        https://docs.python.org/3/library/fnmatch.html
        Unix shell-style wildcards: *, ?, [seq], [!seq]
        * - matches everything, ? - matches any single character
        [seq] - matches any character in seq, [!seq] - matches any character not in seq
        For a literal match, wrap the meta-characters in brackets.
        For example, '[?]' matches the character '?'.
        Note that the filename separator ('/' on Unix) is not special to this module.
        Similarly, filenames starting with a period are not special for this module,
        and are matched by the * and ? patterns.
        :return:
        """
        # extensions: html, json, woff
        ext_result = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                             pattern='*.????', recursive=True,
                                                             include_hidden=False, case_sensitive=False))
        # word in filename
        word_result = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                              pattern='*test*', recursive=True,
                                                              include_hidden=False, case_sensitive=False))
        # case-sensitive
        case_result = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                              pattern='LICENSE*', recursive=True,
                                                              include_hidden=False, case_sensitive=True))
        partial_case_result = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                                      pattern='*.Md', recursive=True,
                                                                      include_hidden=False, case_sensitive=True))
        partial_case_result1 = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                                       pattern='*.Md', recursive=True,
                                                                       include_hidden=False, case_sensitive=False))
        upper_case_result = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                                    pattern='*.MD', recursive=True,
                                                                    include_hidden=False, case_sensitive=False))
        upper_case_result1 = list(current_os.search_files_by_pattern(dirpath=self.get_locations('data_for_tests'),
                                                                     pattern='*.MD', recursive=True,
                                                                     include_hidden=False, case_sensitive=True))
        self.assertEqual(len(ext_result), 3)
        self.assertEqual(len(word_result), 3)
        self.assertEqual(len(case_result), 4)
        self.assertEqual(len(partial_case_result), 0)
        self.assertEqual(len(partial_case_result1), 2)
        self.assertEqual(len(upper_case_result), 2)
        self.assertEqual(len(upper_case_result1), 0)

    def test_group_ext_by_type_default(self):
        from count_files.utils.group_extensions import ext_and_group_dict
        counter0 = Counter({'PYC': 42, 'TXT': 27, 'PY': 24, 'MD': 15, '[no extension]': 9,
                           'PNG': 8, 'MP4': 5, 'FLV': 5, 'RST': 4, 'GZ': 3, 'BAT': 1,
                            'MP3': 1, 'JSON': 1, 'WOFF': 1})
        result0 = {'archives': [('GZ', 3)], 'audio': [('MP3', 1)], 'audio/video': [('MP4', 5)],
                   'data': [('JSON', 1)], 'documents': [('TXT', 27), ('MD', 15), ('RST', 4)],
                   'executables': [('BAT', 1)], 'fonts': [('WOFF', 1)], 'images': [('PNG', 8)],
                   'python': [('PYC', 42), ('PY', 24)], 'videos': [('FLV', 5)],
                   'other': [('[no extension]', 9)]}
        storage0 = group_ext_by_type(data=counter0.most_common(), ext_and_group=ext_and_group_dict)

        counter1 = Counter({'pyc': 42, 'txt': 26, 'py': 24, 'md': 15, '[no extension]': 9,
                            'TXT': 1, 'html': 1})
        result1 = {'archives': [], 'audio': [], 'audio/video': [], 'data': [],
                   'documents': [('txt', 26), ('md', 15), ('TXT', 1)],
                   'executables': [], 'fonts': [], 'images': [],
                   'python': [('pyc', 42), ('py', 24)], 'videos': [],
                   'other': [('[no extension]', 9), ('html', 1)]}
        storage1 = group_ext_by_type(data=counter1.most_common(), ext_and_group=ext_and_group_dict)

        self.assertDictEqual(storage0, result0)
        self.assertDictEqual(storage1, result1)

    def test_group_ext_by_type_arbitrary(self):
        ext_and_group_dict = {'mp3': 'media', 'mp4': 'media',  'png': 'media',
                              'md': 'markup', 'rst': 'markup',
                              'sqlite3': 'databases', 'sqlitedb': 'databases'}
        counter0 = Counter({'PYC': 42, 'TXT': 27, 'PY': 24, 'MD': 15, '[no extension]': 9,
                           'PNG': 8, 'MP4': 5, 'FLV': 5, 'RST': 4, 'GZ': 3, 'BAT': 1,
                            'MP3': 1, 'JSON': 1, 'WOFF': 1})
        result0 = {'databases': [],
                   'markup': [('MD', 15), ('RST', 4)],
                   'media': [('PNG', 8), ('MP4', 5), ('MP3', 1)],
                   'other': [('PYC', 42), ('TXT', 27), ('PY', 24), ('[no extension]', 9),
                             ('FLV', 5), ('GZ', 3), ('BAT', 1), ('JSON', 1), ('WOFF', 1)]}
        storage0 = group_ext_by_type(data=counter0.most_common(), ext_and_group=ext_and_group_dict)
        self.assertDictEqual(storage0, result0)


# from root directory:

# run all tests in test_some_functions.py
# python -m unittest tests/test_some_functions.py

# run all tests for class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions

# run test for def test_generic_text_preview_excerpt in class TestSomeFunctions
# python -m unittest tests.test_some_functions.TestSomeFunctions.test_generic_text_preview_excerpt

# or run file in PyCharm


if __name__ == '__main__':
    unittest.main()
