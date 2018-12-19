#!/usr/bin/env python3
"""https://docs.python.org/3.6/library/timeit.html

Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)
Timer.repeat(repeat=3, number=1000000)
"""
import timeit
import sys
import os

from count_files.utils.file_handlers import search_files, count_files_by_extension
from count_files.__main__ import main_flow
from count_files.utils.file_handlers import get_total, get_total_by_extension


def get_locations(*args):
    return os.path.normpath(os.path.join(os.path.expanduser('~/'), *args))


main_fe = """
main_flow([location, '-a', '-fe', 'txt'])
"""

main_fe_fs = """
main_flow([location, '-a', '-fe', 'txt', '-fs'])
"""

search_files_feedback = """
data = (f for f in search_files(dirpath=location, extension='.', recursive=True, include_hidden=True, case_sensitive=False))
"""

count_files_feedback = """
data = count_files_by_extension(dirpath=location, no_feedback=False, recursive=True, include_hidden=True)
"""

total = """
r = get_total(location, include_hidden=True, no_feedback=False, recursive=True)
print('Result:', len(list(r)))
"""

total_by_extension = """
r = get_total_by_extension(location, extension='txt',
case_sensitive=False, include_hidden=True, no_feedback=False,
recursive=True)
print('Result:', len(list(r)))
"""

win_optim_test = """
main_flow([location, '-fe', '.'])
"""


if __name__ == "__main__":

    if sys.platform.startswith('win'):
        location = get_locations('Count-files')
    elif sys.platform.startswith('darwin'):
        # specify folder
        pass
    elif sys.platform.startswith('linux'):
        # specify folder
        pass

    # win optimization, skipping hidden root folders
    t = timeit.Timer(win_optim_test, globals=globals())
    print(win_optim_test, t.repeat(repeat=3, number=1))
    # t = timeit.Timer(total_by_extension, globals=globals())
    # print(total_by_extension, t.repeat(repeat=3, number=1))
    # t = timeit.Timer(main_fe, globals=globals())
    # print(main_fe, t.repeat(repeat=3, number=1))
