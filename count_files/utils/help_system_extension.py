"""HELP SYSTEM EXTENSION

"""
from textwrap import fill
from itertools import chain

from count_files.utils.help_text import indexes, docs_text, docs_groups_text, \
    docs_sort_text, docs_args_text, docs_list_text, docs_general_text
from count_files.settings import START_TEXT_WIDTH


def print_help_text(text: str):
    """Print an adaptive and formatted help text for section in docs.

    Sections:
    count-files --args-help docs [list, args, sort, groups]
    :param text: section text
    :return:
    """
    for item in text.split('\n'):
        print(fill(item, width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
    return


def search_in_help(topic: str):
    """Search for help text by topic(argument or group name, search words).

    Display corresponding help message for:
    count-files --args-help docs
        basic usage examples, this HELP SYSTEM EXTENSION DOCS
    count-files --args-help list
        available arguments, group_names, search_words
    count-files --args-help args
        more about search by short/long argument name
    count-files --args-help sort
        more about sorting arguments by purpose or type
    count-files --args-help groups
        more about sorting arguments by group.
    count-files --args-help <topic>
        searching or sorting using indexes from count_files.utils.help_text.py
        default: show long description for <keyword in lower case>,
        show short description for <keyword with all or one letter in upper case>
    :param topic: argument or group name, search words in lower or upper case
    :return:
    """
    key_lower = topic.lower()
    if key_lower == 'docs':
        print_help_text(docs_text)
    elif key_lower == 'args':
        print_help_text(docs_args_text)
    elif key_lower == 'sort':
        print_help_text(docs_sort_text)
    elif key_lower == 'groups':
        print_help_text(docs_groups_text)
    elif key_lower == 'list':
        print_help_text(docs_list_text)
    elif key_lower not in set(chain.from_iterable(indexes.keys())):
        print(fill(f'Not found: {topic}', width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
        print_help_text(docs_general_text)
    else:
        for k, v in indexes.items():
            if key_lower in k:
                print(fill(str(v[0]), width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
                # show long description
                if topic == key_lower:
                    print(fill(f'Long: {v[2]}', width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
                # show short description
                else:
                    print(fill(f'Short: {v[1]}', width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
