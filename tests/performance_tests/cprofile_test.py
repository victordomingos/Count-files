#!/usr/bin/env python3
"""https://docs.python.org/3.6/library/profile.html

profile.run(command, filename=None, sort=-1)
This function takes a single argument that can be passed to the exec() function,
and an optional file name.
The column headings include:
ncalls for the number of calls.
tottime for the total time spent in the given function (and excluding time made in calls to sub-functions)
percall is the quotient of tottime divided by ncalls
cumtime is the cumulative time spent in this and all subfunctions (from invocation till exit).
This figure is accurate even for recursive functions.
percall is the quotient of cumtime divided by primitive calls
filename:lineno(function) provides the respective data of each function
"""
import cProfile
import os
import sys

from count_files.utils.viewing_modes import show_result_for_search_files, show_2columns, show_result_for_total
from count_files.utils.file_handlers import search_files, count_files_by_extension
from count_files.__main__ import main_flow


def get_locations(*args):
    return os.path.normpath(os.path.join(os.path.expanduser('~/'), *args))


if __name__ == "__main__":

    if sys.platform.startswith('win'):
        location = get_locations('Count-files')
    elif sys.platform.startswith('darwin'):
        # specify folder
        pass
    elif sys.platform.startswith('linux'):
        # specify folder
        pass

    # Counter and count all files with all extensions, return table, feedback - file names
    """cProfile.run("data = count_files_by_extension("
                 "dirpath=location, no_feedback=False, recursive=True, include_hidden=False);"
                 "total_occurrences = sum(data.values());"
                 "max_word_width = max(map(len, data.keys()));"
                 "data = data.most_common();"
                 "show_2columns(data, max_word_width, total_occurrences)", sort='name')"""

    # generator and search files, return list, feedback - list itself
    """cProfile.run("data = (f for f in search_files(dirpath=location, extension='..', "
                 "recursive=True, include_hidden=True, case_sensitive=False));"
                 "len_files = show_result_for_search_files(files=data, "
                 "file_sizes=False, preview=False)",
                 sort='name')"""

    # generator and get total files, return list, feedback - file paths
    """cProfile.run("data = search_files(dirpath=location, extension='..', "
                 "recursive=True, include_hidden=True, case_sensitive=False);"
                 "len_files = show_result_for_total(files=data, "
                 "no_feedback=False)",
                 sort='name')"""

    # count
    # cProfile.run("main_flow([location])", sort='name')

    # search
    # cProfile.run("main_flow([location, '-fe', '..'])", sort='name')

    # total
    # cProfile.run("main_flow([location, '-t', '..'])", sort='name')

