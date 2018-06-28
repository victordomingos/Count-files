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
from count_files.utils.word_counter import show_result_for_search_files, show_2columns
from count_files.utils.file_handlers import search_files, count_files_by_extension
from count_files.__main__ import main_flow


def get_locations(*args):
    return os.path.normpath(os.path.join(os.path.expanduser('~/'), *args))


if __name__ == "__main__":

    if sys.platform.startswith('win'):
        location = get_locations('Desktop')
    elif sys.platform.startswith('darwin'):
        # specify folder
        pass
    elif sys.platform.startswith('linux'):
        # specify folder
        pass

    # count all files
    # cProfile.run("main_flow([location, '-a'])", sort='name')
    # if extension thread, search for txt extension
    # cProfile.run("main_flow([location, '-a', '-fe', 'txt'])", sort='name')

    # Counter and count all files with all extensions, return table, feedback - file names
    cProfile.run("data = count_files_by_extension(dirpath=location, no_feedback=False,"
                 "recursive=True, include_hidden=True); show_2columns(data.most_common())", sort='name')

    # generator and search all files with all extensions, return list, feedback - list itself
    cProfile.run("data = (f for f in search_files(dirpath=location, extension='..', "
                 "recursive=True, include_hidden=True, case_sensitive=False));"
                 "len_files = show_result_for_search_files(files=data, "
                 "no_list=False, no_feedback=False, preview=False)",
                 sort='name')

