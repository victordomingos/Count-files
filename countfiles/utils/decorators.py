import datetime
from functools import wraps
import traceback


def exceptions_decorator(func, logger=None):
    """
    Registration and interception of the main exceptions
    :param func: executable function
    :param logger: the logging object
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # print(datetime.datetime.now())
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print('Exit')
        except Exception:
            msg = traceback.format_exc().splitlines()[-1] \
                  + ' in def ' + func.__name__
            if logger:
                logger.exception(msg)
            print(msg)
            print('Sorry, an error occurred while retrieving data')
    return wrapper

