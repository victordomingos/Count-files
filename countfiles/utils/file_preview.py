import os
import puremagic
import itertools

from pathlib import Path


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
        mf = puremagic.magic_file(filepath)
        if mf:
            filetype = " ".join(str(i) for i in next(itertools.chain(mf)))
            filetype += "\n"
    except Exception as e:
        print(e)
        filetype = ""

    try:
        excerpt = f.read_text(errors="replace")[0:max_size].replace('\n', ' ')
    except Exception as e:
        print(e)
        excerpt = f.read_bytes()[0:max_size]

    return f"{filetype}{excerpt}"
