#!/usr/bin/env python3
import traceback
from functools import wraps

from count_files.settings import BUG_REPORT_URL


def exceptions_decorator(func):
    """Registration and interception of the main exceptions.

    :param func: executable function
    :param logger: the logging object
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print('The execution of the program was interrupted.')
        except Exception:
            print(traceback.format_exc())
            print('Sorry, an error occurred while retrieving data.\n'  
                  f'You can report a problem at {BUG_REPORT_URL}')
    return wrapper
