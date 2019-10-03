#!/usr/bin/env python3
"""https://docs.python.org/3.6/library/timeit.html

Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)
Timer.repeat(repeat=3, number=1000000)
"""
import timeit
import sys
import os

from count_files.platforms import get_current_os
from count_files.__main__ import main_flow
from count_files.utils.viewing_modes import show_2columns, \
    show_result_for_total, show_result_for_search_files


def get_locations(*args):
    return os.path.normpath(os.path.join(os.path.expanduser('~/'), *args))


current_os = get_current_os()

main_c = """
main_flow([location])
"""

main_fe = """
main_flow([location, '-fe', 'txt'])
"""

main_t = """
main_flow([location, '-t', 'txt'])
"""

search_by_extension = """
data = (f for f in current_os.search_files(dirpath=location, extension='..',
recursive=True, include_hidden=False, case_sensitive=False))
len_files = show_result_for_search_files(files=data, file_sizes=False, preview=False)
"""

count_by_extension = """
data = current_os.count_files_by_extension(dirpath=location, no_feedback=False, 
recursive=True, include_hidden=False)
total_occurrences = sum(data.values())
max_word_width = max(map(len, data.keys()))
data = data.most_common()
show_2columns(data, max_word_width, total_occurrences)
"""

total_and_extension = """
data = current_os.search_files(dirpath=location, extension='..',
recursive=True, include_hidden=False, case_sensitive=False)
len_files = show_result_for_total(files=data, show_folders=True, 
total_size=True, no_feedback=False, recursive=True)
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

    # t = timeit.Timer(main_t, globals=globals())
    # print(main_t, t.repeat(repeat=3, number=1))

    # t = timeit.Timer(search_by_extension, globals=globals())
    # print(search_by_extension, t.repeat(repeat=3, number=1))

    # t = timeit.Timer(count_by_extension, globals=globals())
    # print(count_by_extension, t.repeat(repeat=3, number=1))

    # t = timeit.Timer(total_and_extension, globals=globals())
    # print(total_and_extension, t.repeat(repeat=3, number=1))
