from itertools import chain


SUPPORTED_TYPES = {
                    'text': ['py', 'txt', 'html', 'css', 'js', 'c'],
                    'image': ['jpg', 'png', 'gif'],
                    'pdf': ['pdf'],
                }

not_supported_type_message = f'No preview available for this file type. ' \
                             f'Supported types: ' \
                             f'{", ".join(sorted(list(chain.from_iterable(SUPPORTED_TYPES.values()))))}. ' \
                             f'Try without preview.'
