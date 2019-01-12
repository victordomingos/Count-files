"""HELP SYSTEM EXTENSION

"""
from textwrap import fill
from itertools import chain
from typing import List

from count_files.utils.help_text import help_system_message_general, \
   help_system_message_list, arguments, group_names, search_words, indexes
from count_files.utils import help_text
from count_files.settings import START_TEXT_WIDTH


def print_help_message(title: str, help_system_message: str or List[dict]):
    """Print an adaptive and formatted help message.

    :param title: headline
    :param help_system_message: string or List[dict] with args example and description
    :return:
    """
    if isinstance(help_system_message, str):
        print(fill(title, width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
        print(fill(help_system_message, width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
        return
    else:
        print(fill(title, width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
        for item in help_system_message:
            print(fill(item['desc'], width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
            print(fill(item['args'], width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
        return


def search_in_help(keyword: str):
    """Search for help text by keyword(argument or group name, search words).

    Display corresponding help message for:
    count-files --args-help docs
        print help_text.__doc__
        this HELP SYSTEM EXTENSION DOCS from count_files.utils.help_text.py
    count-files --args-help list
        print arguments, group_names, search_words from count_files.utils.help_text.py
    count-files --args-help <keyword>
        searching or sorting using indexes from count_files.utils.help_text.py
        default: show long description for <keyword in lower case>,
        show short description for <keyword with all or one letter in upper case>
    :param keyword: argument or group name, search words in lower or upper case
    :return:
    """
    key_lower = keyword.lower()
    if key_lower == 'docs':
        for item in help_text.__doc__.split('\n'):
            print(fill(item,  width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
    elif key_lower == 'list':
        print('  KEYWORDS:')
        print_help_message('Available arguments:', ', '.join(arguments))
        print_help_message('Available group names:', ', '.join(group_names))
        print_help_message('Available search words:', ', '.join(search_words))
        print_help_message('ALSO USE:', help_system_message_list)
    elif key_lower not in set(chain.from_iterable(indexes.keys())):
        print(fill(f'Not found: {keyword}', width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
        print_help_message('ALSO USE:', help_system_message_general)
    else:
        for k, v in indexes.items():
            if key_lower in k:
                print(fill(str(v[0]), width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
                # show long description
                if keyword == key_lower:
                    print(fill(f'Long: {v[2]}', width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
                # show short description
                else:
                    print(fill(f'Short: {v[1]}', width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
