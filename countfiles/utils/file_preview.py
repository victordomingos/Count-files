#!/usr/bin/env python3

import os
import puremagic
import itertools

from pathlib import Path

SUPPORTED_TYPES = {
    'text': ['py', 'txt', 'html', 'css', 'js', 'c'],
    'image': ['jpg', 'png', 'gif'],
    'pdf': ['pdf'],
}

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

    # TODO: Check if there is a specific file preview method
    

    # If no specific previewers were found, use the generic text/bytes preview:
    try:
        my_file = puremagic.magic_file(filepath)
        if my_file:
            filetype = " ".join(str(i) for i in next(itertools.chain(my_file)))
            filetype += "\n"
    except Exception as e:
        #print("ERROR 1:", e)
        pass

    try:
        excerpt = f.read_text(errors="replace")[0:max_size].replace('\n', ' ')
    except Exception as e:
        print("ERROR 2:", e)

        try:
            excerpt = f.read_bytes()[0:max_size]
        except Exception as e:
            print("ERROR 3:", e)




    if filetype:
        if filetype in SUPPORTED_TYPES:
            return f"Format: {filetype}{excerpt}"
        else:
            return f"Format: {filetype}[No preview available for this file.]"
    else:
        return f'Unknown filetype'
