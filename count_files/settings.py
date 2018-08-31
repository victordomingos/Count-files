#!/usr/bin/env python3
# encoding: utf-8
import shutil


BUG_REPORT_URL = 'https://github.com/victordomingos/Count-files/issues'

TERM_WIDTH, _ = shutil.get_terminal_size((80, 24))
DEFAULT_PREVIEW_SIZE = 5 * TERM_WIDTH  # 5 lines of text preview
START_TEXT_WIDTH = TERM_WIDTH if TERM_WIDTH < 100 else 100
DEFAULT_EXTENSION_COL_WIDTH = 9
DEFAULT_FREQ_COL_WIDTH = 5
MAX_TABLE_WIDTH = 80

SUPPORTED_TYPES = {
    'all_extensions': ['..'],
    'no_extension': ['.'],
    'text': ['py', 'txt', 'html', 'css', 'js', 'c', 'md', 'json'],
}

supported_type_info_message = f'This is the list of currently supported file types for preview: ' \
                              f'{", ".join(sorted(SUPPORTED_TYPES["text"]))}.\n' \
                              f'Previewing files without extension is not supported. ' \
                              f'You can use the "--preview" argument together with the search ' \
                              f'for all files regardless of the extension ("--file-extension .."). ' \
                              f'In this case, the preview will only be displayed for files with a supported extension.'

not_supported_type_message = f'Sorry, there is no preview available for this file type. ' \
                             f'You may want to try again without preview.\n' \
                             f'{supported_type_info_message}'
