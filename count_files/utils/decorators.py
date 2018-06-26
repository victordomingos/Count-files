import traceback
import logging
import os
import sys
from functools import wraps
from count_files.settings import LOG_FOLDER, CLI_LOG_FILE, BUG_REPORT_URL


cli_logger = logging.getLogger('cli')
cli_logger.setLevel(logging.INFO)
if not os.path.isdir(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)
fh = logging.FileHandler(LOG_FOLDER+os.sep+CLI_LOG_FILE)
fr = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(fr)
cli_logger.addHandler(fh)


def exceptions_decorator(func, logger=cli_logger):
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
            msg = f'{traceback.format_exc().splitlines()[-1]} in def {func.__name__}'
            logger.info(f'Input: {sys.argv}')
            logger.exception(msg)
            print('Sorry, an error occurred while retrieving data.\n'
                  f'Short description: {msg}. Details: {LOG_FOLDER+os.sep+CLI_LOG_FILE}.\n'
                  f'You can report a problem at {BUG_REPORT_URL}')
    return wrapper
