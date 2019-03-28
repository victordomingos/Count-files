"""HELP SYSTEM EXTENSION.
Interactive Help based on https://docs.python.org/3/library/cmd.html
"""
from textwrap import fill
from itertools import chain
import cmd

from count_files.utils.help_text import indexes, docs_text, docs_groups_text, \
    docs_sort_text, docs_args_text, docs_list_text, docs_general_text
from count_files.settings import START_TEXT_WIDTH


class HelpCmd(cmd.Cmd):
    """Count Files Help. Search in help text by topic.

    Start this interactive help: count-files --help-cmd
    help> help
    basic usage examples, this HelpCmd examples
    help> list
    available arguments, group_names, search_words
    help> args
    more about search by short/long argument name
    help> sort
    more about sorting arguments by purpose or type
    help> groups
    more about sorting arguments by group
    help> <topic>
    search by argument or group name, certain search words
    """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Count Files Help! Type "help" or "?" to list commands.\n' \
                     'Enter the name of the argument or group to get help text.\n' \
                     'To quit, just type "quit".\n'
        self.prompt = 'help> '

    def do_help(self, arg):
        """More about Count Files Help usage, type "help"."""
        self.print_help_text(docs_text)

    def do_quit(self, arg):
        """Exit the Count Files Help by entering "quit"."""
        print('Exit the Count Files Help.')
        return True

    def emptyline(self):
        """Method called when an empty line is entered in response to the prompt."""
        print('Please enter command name(cmd, help, quit) or search word.')

    def default(self, arg: str):
        """Search in help text."""
        self.search_in_help(arg)

    def print_help_text(self, text: str):
        """Print an adaptive and formatted help text for section or search results.

        Sections: help> [list, args, sort, groups]
        Search: help> argument or group name
        :param text: section, argument or group help text
        :return:
        """
        for item in text.split('\n'):
            print(fill(item, width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
        return

    def search_in_help(self, topic: str):
        """Search for help text by topic(argument or group name, search words).

        Display corresponding help message for:
        help> [list, args, sort, groups]
        help> <topic>
        searching or sorting using indexes from count_files.utils.help_text.py
        default: show long description for <topic in lower case>,
        show short description for <topic with all or one letter in upper case>
        :param topic: argument or group name, search words in lower or upper case
        :return:
        """
        key_lower = topic.lower()
        if key_lower == 'args':
            self.print_help_text(docs_args_text)
        elif key_lower == 'sort':
            self.print_help_text(docs_sort_text)
        elif key_lower == 'groups':
            self.print_help_text(docs_groups_text)
        elif key_lower == 'list':
            self.print_help_text(docs_list_text)
        elif key_lower not in set(chain.from_iterable(indexes.keys())):
            print(fill(f'Not found: {topic}', width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
            self.print_help_text(docs_general_text)
        else:
            for k, v in indexes.items():
                if key_lower in k:
                    print(fill(str(v[0]), width=START_TEXT_WIDTH, initial_indent=' ' * 2, subsequent_indent=' ' * 2))
                    # show long description
                    if topic == key_lower:
                        print(fill(f'{v[2]}', width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
                    # show short description
                    else:
                        print(fill(f'{v[1]}', width=START_TEXT_WIDTH, initial_indent=' ' * 6, subsequent_indent=' ' * 6))
