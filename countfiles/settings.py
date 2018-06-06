# encoding: utf-8
from itertools import chain

DEFAULT_PREVIEW_SIZE = 395

SUPPORTED_TYPES = {
    'text': ['py', 'txt', 'html', 'css', 'js', 'c'],
    #'image': ['jpg', 'png', 'gif'],
    #'pdf': ['pdf'],
}

not_supported_type_message = f'Sorry, there is no preview available for this file type. ' \
                             f'\nThis is the list of currently supported file types: ' \
                             f'{", ".join(sorted(list(chain.from_iterable(SUPPORTED_TYPES.values()))))}. ' \
                             f'\nYou may want to try again without preview.\n\n'
