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
from countfiles.utils.file_handlers import search_files, count_file_extensions1, count_files_by_extension
from countfiles.__main__ import main_flow


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

    # cProfile.run("main_flow([location, '-a'])", sort='name')
    # cProfile.run("main_flow([location, '-a', '-fe', 'txt'])", sort='name')
    cProfile.run("data = count_files_by_extension(dirpath=location, no_feedback=False,"
                 "recursive=True, include_hidden=True)", sort='name')
    cProfile.run("data = search_files(dirpath=location, extension='', recursive=True, include_hidden=True); "
                 "counter = count_file_extensions1(file_paths=data, no_feedback=False)", sort='name')

