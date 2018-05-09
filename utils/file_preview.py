import puremagic
#import fleep
from pathlib import Path

import os

TEXTFILES = [ "txt", "md", "htm", "html", "py", "js", "json"]

def generate_preview(filepath: str, max_size=390) -> str:
    """ Detect filetype and generate a human readable text preview """
    #ftypes = magic_file(filepath)
    extension = os.path.splitext(filepath)[1][1:]

    if extension in TEXTFILES:
        f = Path(os.path.expanduser(filepath))
        preview = f.read_text(errors="replace")[0:max_size].replace('\n', ' ')
        return preview
    else:
        # Testing fleep...
        #with open(filepath, "rb") as file:
        #    info = fleep.get(file.read(128))

        #return info.mime[0]  # prints ['image/png']

        ext = puremagic.from_file(filepath)
        mf = puremagic.magic_file(filepath)
        print("PMagic ext:", ext)
        print("PMagic magicfile:", mf)









