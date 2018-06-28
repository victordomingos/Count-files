"""https://docs.python.org/3.6/library/timeit.html

Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)
Timer.repeat(repeat=3, number=1000000)
"""
import timeit
import sys
import os
from count_files.utils.file_handlers import search_files, count_files_by_extension
from count_files.__main__ import main_flow


def get_locations(*args):
    return os.path.normpath(os.path.join(os.path.expanduser('~/'), *args))


main_no_feedback_no_table = """
main_flow([location, '-a', '-nf', '-nt'])
"""

main_feedback_table = """
main_flow([location, '-a'])
"""

search_files_feedback = """
data = (f for f in search_files(dirpath=location, extension='.', recursive=True, include_hidden=True, case_sensitive=False))
"""

count_files_feedback = """
data = count_files_by_extension(dirpath=location, no_feedback=False, recursive=True, include_hidden=True)
"""

main_search_all = """
main_flow([location, '-a', '-fe', '..', '-nl'])
"""

main_count_all = """
main_flow([location, '-a', '-nf', '-nt'])
"""

if __name__ == "__main__":

    if sys.platform.startswith('win'):
        location = get_locations('Desktop')
    elif sys.platform.startswith('darwin'):
        # specify folder
        pass
    elif sys.platform.startswith('linux'):
        # specify folder
        pass

    stmts = [main_count_all, main_search_all]
    for s in stmts:
        t = timeit.Timer(stmt=s, globals=globals())
        print(s, t.repeat(repeat=3, number=1))
