# encoding: utf-8
import shutil
from itertools import chain


TERM_WIDTH, _ = shutil.get_terminal_size((80,24))
DEFAULT_PREVIEW_SIZE = 5 * TERM_WIDTH  # 5 lines of text preview


SUPPORTED_TYPES = {
    'text': ['py', 'txt', 'html', 'css', 'js', 'c'],
    'image': ['jpg', 'png', 'gif'],
    'pdf': ['pdf'],
}

not_supported_type_message = f'Sorry, there is no preview available for this file type. ' \
                             f'\nThis is the list of currently supported file types: ' \
                             f'{", ".join(sorted(list(chain.from_iterable(SUPPORTED_TYPES.values()))))}. ' \
                             f'\nYou may want to try again without preview.\n\n'

supported_type_info_message = f'This is the list of currently supported file types for preview: ' \
                              f'{", ".join(sorted(list(chain.from_iterable(SUPPORTED_TYPES.values()))))}. '
