#!/usr/bin/env python3
# encoding: utf-8
import os
import puremagic
import itertools

from pathlib import Path

from countfiles.utils.file_handlers import get_file_extension
from countfiles.settings import SUPPORTED_TYPES


def generate_preview(filepath: str, max_size=390) -> str:
    """ Detect filetype and generate a human readable text preview

    Detects filetype and returns a string if there is a compatible text
    preview method available. For text files, the preview will be the first
    `max_size` characters. For other file types, a selection of their
    metadata could be shown.
    """
    f = Path(os.path.expanduser(filepath))
    filetype = ""
    excerpt = ""
    extension = get_file_extension(filepath)

    try:
        my_file = puremagic.magic_file(filepath)
        if my_file:
            filetype = " ".join(str(i) for i in next(itertools.chain(my_file)))
    except Exception as e:
        # print("ERROR 1:", e)
        pass

    # TODO: Check if there is a specific file preview method
    print('EXT:', extension)
    print('TYPE:', filetype)

    if extension in SUPPORTED_TYPES['text']:
        try:
            excerpt = f.read_text(errors="replace")[0:max_size].replace('\n', ' ')
        except Exception as e:
            print("ERROR 2:", e)

    #elif extension in SUPPORTED_TYPES['image']:
    #    pass

    #elif extension in SUPPORTED_TYPES['pdf']:
    #    pass


    # This part of the code is currently not being used anymore, since
    # main_flow() only calls this function whenever it finds a known file type.
    """
    # If no specific previewers were found, use the generic text/bytes preview:
    else:
        try:
            excerpt = f.read_text(errors="replace")[0:max_size].replace('\n', ' ')
        except Exception as e:
            print("ERROR 2:", e)

            try:
                excerpt = f.read_bytes()[0:max_size]
            except Exception as e:
                print("ERROR 3:", e)
    """

    if excerpt:
        return f"Format: {filetype}\n{excerpt}"
    else:
        return f"Format: {filetype}\n[No preview available for this file.]"
