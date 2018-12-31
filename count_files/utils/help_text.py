"""HELP SYSTEM EXTENSION DOCS.

ALSO USE:

Get the standard argparse help with a brief description of all the arguments.
    count-files --help
Get this help system extension usage examples.
    count-files --args-help docs
Get a list of available keywords for search.
    count-files --args-help list
Web Docs in English, Portuguese, Russian and Ukrainian:
    https://github.com/victordomingos/Count-files#documentation

KEYWORD USAGE:

Keyword - argument or group name, certain search words for sorting.
    count-files -ah <keyword>
    count-files --args-help <keyword>
Show short help text: Keyword must be in upper case or with one letter in upper case.
    count-files --args-help <keyword in upper case>
Show more detailed help text: Keyword must be in lower case.
    count-files --args-help <keyword in lower case>

Search by short/long argument name:
Short argument name.
    count-files --args-help st
Long argument name.
    count-files --args-help supported-types
Partial argument name if it consists of two words.
    count-files --args-help supported
    count-files --args-help types

Sorting arguments by purpose:
Service arguments: display of help, version of the program etc.
(h or help, ah or args-help, v or version, st or supported-types)
All service arguments.
    count-files --args-help service
Get by name.
    count-files --args-help help

Common arguments: directory path and sorting settings that are common to search and count.
(path, a or all, c or case-sensitive, nr or no-recursion, nf or no-feedback)
All common arguments.
    count-files --args-help common
Get by name.
    count-files --args-help no-recursion

Special arguments: arguments for counting or searching files.
Count by extension: alpha or sort-alpha;
Total number of files: t or total;
Search by extension: fe or file-extension, fs or file-sizes, p or preview, ps or preview-size.
All special arguments.
    count-files --args-help special
Get by name.
    count-files --args-help file-extension

Sorting arguments by type:
    count-files --args-help positional
    count-files --args-help optional

Sorting arguments by group, including group description:
    count-files --args-help count
    count-files --args-help search
    count-files --args-help total

Get group description:
(count-group or cg, search-group or sg, total-group or tg)
    count-files --args-help count-group
    count-files --args-help tg

Get all group descriptions:
    count-files --args-help groups
"""
from count_files.settings import DOCUMENTATION_URL


docs = {
    'args': 'count-files --args-help docs',
    'desc': 'Get help system extension usage examples.'
}
keywords_list = {
    'args': 'count-files --args-help list',
    'desc': 'Get a list of available keywords for search.'
}
standard = {
    'args': 'count-files --help',
    'desc': 'Get the standard argparse help with a brief description of all the arguments.'
}
web = {
    'args': DOCUMENTATION_URL,
    'desc': 'Web Docs in English, Portuguese, Russian and Ukrainian:'
}

help_system_message_general = [standard, docs, keywords_list,  web]
help_system_message_list = [standard, docs, web]

arguments = [
    # common arguments(positional)
    'path',
    # service arguments(optional)
    'h', 'help', 'ah', 'args-help', 'v', 'version', 'st', 'supported-types',
    # common arguments(optional)
    'a', 'all', 'c', 'case-sensitive',
    'nr', 'no-recursion', 'nf', 'no-feedback',
    # special arguments(optional)
    'alpha', 'sort-alpha',
    'fe', 'file-extension', 'fs', 'file-sizes',
    'p', 'preview', 'ps', 'preview-size',
    't', 'total',
]

group_names = [
    # certain group description
    'cg', 'count-group', 'sg', 'search-group', 'tg', 'total-group',
    # all group descriptions
    'groups'
]
search_words = [
    # sorting by purpose
    'service', 'common', 'special',
    # sorting by argument type
    'positional', 'optional',
    # sorting by group, including group description
    'count', 'search', 'total',
]

# all argument and group names descriptions(short and long help text)
args = {
    'help': {
        'name': '-h, --help',
        'short': 'Built-in argparse help system with a brief description of all the arguments. '
                 'Show help message and exit.',
        'long': 'Built-in argparse help system with a brief description of all the arguments. '
                'Show help message and exit. '
                'Usage: count-files -h or count-files --help.'
    },
    'args-help': {
        'name': '-ah ARGUMENT, --args-help ARGUMENT',
        'short': 'Search in help by keyword - argument or group name(count, search, total). '
                 'Show more detailed help text: count-files -ah docs. '
                 'Show list of argument or group names: count-files -ah list. '
                 'Usage: count-files -ah <keyword>.',
        'long': 'Show more detailed help text: count-files -ah docs.'
    },
    'version': {
        'name': '-v, --version',
        'short': "Show program's version number and exit.",
        'long': "Show program's version number and exit. "
                'Usage: count-files -v or count-files --version.'
    },
    'supported-types': {
        'name': '-st, --supported-types',
        'short': 'The list of currently supported file types for preview.',
        'long': 'Show a list of currently supported file types for preview and exit. '
                'Usage: count-files -st or count-files --supported-types.'
    },
    'path': {
        'name': 'path',
        'short': 'The path to the folder containing the files to be counted.',
        'long': 'The path to the folder containing the files to be counted. '
                'If you leave this argument empty, it will scan the current working directory. '
                "To process files in the user's home directory, you can use ~ (tilde). "
                'For example: count-files ~/Documents <arguments>. '
                'Common argument for counting and searching by extension '
                'or counting the total number of files.'
    },
    'all': {
        'name': '-a, --all',
        'short': 'Include hidden files and directories.',
        'long': 'Include hidden files and directories. '
                'By default, it will ignore files and directories that are supposed to be hidden. '
                'In Windows, files and directories considered hidden by this application '
                'are those for which the FILE_ATTRIBUTE_HIDDEN attribute is set to true. '
                'In Linux, macOS, iOS and other Unix-like operating systems, '
                'a file or directory is considered to be hidden if its name starts with a "." (dot). '
                'Common argument for counting and searching by extension '
                'or counting the total number of files.'
    },
    'no-recursion': {
        'name': '-nr, --no-recursion',
        'short': "Don't recurse through subdirectories.",
        'long': "The optional '-nr' or '--no-recursion' switch argument "
                "tells the application not to scan recursively through the subdirectories."
                'Common argument for counting and searching by extension '
                'or counting the total number of files.'
    },
    'case-sensitive': {
        'name': '-c, --case-sensitive',
        'short': 'Treat file extensions with case sensitiveness.',
        'long': 'The names of extensions are case insensitive by default. '
                'The results for ini and INI will be the same. '
                'To distinguish between similar extensions in different cases, '
                'use the -c or --case-sensitive switch argument.'
                'Common argument for counting and searching by extension '
                'or counting the total number of files.'
    },
    'no-feedback': {
        'name': '-nf, --no-feedback',
        'short': "Turns off the program's operating indicator (printing processed file names in one line).",
        'long': "Don't show the program's operating indicator (printing processed file names in one line). "
                'Feedback is available by default for counting files by extension '
                '(table) and for counting the total number of files (-t or --total). '
                'This option disables it. '
                'For searching by extension feedback is a list of the found file paths.'
    },
    'total-group': {
        'name': 'Total number of files',
        'short': 'Displaying the number of files that either have a certain extension or no extension at all. '
                 'Usage: count-files [-a, --all] [-c, --case-sensitive] '
                 '[-nr, --no-recursion] [-nf, --no-feedback] '
                 '[-t EXTENSION, --total EXTENSION] [path].',
        'long': 'Displaying the number of files that either have a certain extension or no extension at all. '
                'To count the total number of files, '
                'the number of files with a specific extension '
                'or the number of files without any extension '
                'you can use the -t or --total argument and specify the name of the extension. '
                'Usage: count-files [-a, --all] [-c, --case-sensitive] '
                '[-nr, --no-recursion] [-nf, --no-feedback] '
                '[-t EXTENSION, --total EXTENSION] [path].'
    },
    'total': {
        'name': '-t EXTENSION, --total EXTENSION',
        'short': 'Get the total number of files in the directory. Specify the extension name.',
        'long': 'Get the total number of files in the directory. Specify the extension name.'
                'If you only need the total number of all files, '
                'or the number of files with a certain extension or without it. '
                'To count the total number of files, you must specify the name of the extension. '
                'Example: count-files --total txt ~/Documents <arguments>. '
                'Use a single dot "." to get the total number of files that do not have an extension. '
                'Example: count-files --total . ~/Documents <arguments>. '
                'Use two dots without spaces ".." to get the total number of files, with or without a file extension. '
                'Example: count-files --total .. ~/Documents <arguments>. '
    },
    'count-group': {
        'name': 'File counting by extension',
        'short': 'Counting all files in the specified directory, by file extension. '
                 'By default, it displays some feedback while scanning and '
                 'it presents a table with file extensions sorted by frequency. '
                 'Usage: count-files [-a, --all] [-alpha, --sort-alpha] '
                 '[-c, --case-sensitive] [-nr, --no-recursion] [-nf, --no-feedback] [path]',
        'long': 'Counting all files in the specified directory, by file extension. '
                'By default, it displays some feedback while scanning and '
                'it presents a table with file extensions sorted by frequency '
                '(e.g.: .txt, .py, .html, .css) and the total number of files found. '
                'All file extensions in the table will be displayed in uppercase (default). '
                'Example: count-files <arguments>. '
                'Usage: count-files [-a, --all] [-alpha, --sort-alpha] '
                '[-c, --case-sensitive] [-nr, --no-recursion] [-nf, --no-feedback] [path]'
    },
    'sort-alpha': {
        'name': '-alpha, --sort-alpha',
        'short': 'Sort the table alphabetically, by file extension.',
        'long': 'By default, result of file counting by extension is a table '
                'that lists all the file extensions found '
                'and displays the frequency for each file extension. '
                'To sort the extensions alphabetically, use the -alpha or --sort-alpha argument. '
                'Example: count-files ---sort-alpha ~/Documents <arguments>.'
    },
    'search-group': {
        'name': 'File searching by extension',
        'short': 'Searching for files that have a given extension. '
                 'By default, it presents a simple list with full file paths. '
                 'Optionally, it may also display a short text preview for each found file. '
                 'Usage: count-files [-a, --all] [-c, --case-sensitive] '
                 '[-nr, --no-recursion] [-fe FILE_EXTENSION, --file-extension FILE_EXTENSION] '
                 '[-fs, --file-sizes] [-p, --preview] [-ps PREVIEW_SIZE, --preview-size PREVIEW_SIZE] [path]',
        'long': 'Searching for files that have a given extension. '
                'This utility can be used to search for files that have a certain file extension '
                '(using -fe or --file-extension) and, optionally, '
                'display a short preview (-p or --preview) for text files. '
                'The size of the preview text sample can be customized '
                'by using the -ps or --preview-size argument '
                'followed by an integer number specifying the number of characters to present. '
                'By default, the result of a search by a certain file extension '
                'is a list of the full paths of the files found. '
                'If you need information about the size of the files, '
                'use the -fs or --file-sizes argument. '
                'Usage: count-files [-a, --all] [-c, --case-sensitive] '
                '[-nr, --no-recursion] [-fe FILE_EXTENSION, --file-extension FILE_EXTENSION] '
                '[-fs, --file-sizes] [-p, --preview] [-ps PREVIEW_SIZE, --preview-size PREVIEW_SIZE] [path]'
    },
    'file-extension': {
        'name': '-fe FILE_EXTENSION, --file-extension FILE_EXTENSION',
        'short': 'Search files by file extension. Specify the extension name.',
        'long': 'Searching and listing files by extension. Specify the extension name. '
                'Example: count-files --file-extension txt ~/Documents <arguments>. '
                'Use a single dot "." to search for files without any extension. '
                'Files with names such as .gitignore, Procfile, _netrc '
                'are considered to have no extension in their name.'
                'Example: count-files --file-extension . ~/Documents <arguments>. '
                'Use two dots without spaces ".." to search for all files '
                'with or without file extensions in their names. '
                'Example: count-files --file-extension .. ~/Documents <arguments>. '
    },
    'preview': {
        'name': '-p, --preview',
        'short': 'Display a short preview (only available for text files).',
        'long': 'Display a short preview (only for text files). '
                'Preview is available as an option when searching files '
                'using the -fe or --file-extension argument. '
                'The default text preview size depends on the terminal width settings. '
                'You can change this value by specifying the argument -ps or --preview-size '
                'followed by an integer (the number of characters to display from each file). '
                'Example: count-files --file-extension txt --preview ~/Documents <arguments>.'
    },
    'preview-size': {
        'name': '-ps PREVIEW_SIZE, --preview-size PREVIEW_SIZE',
        'short': 'Specify the number of characters to be displayed from each found file.',
        'long': 'Specify the number of characters to be displayed from each found file. '
                'Preview text files is available as an option when searching files '
                'using the --file-extension and --preview argument. '
                'The default text preview size depends on the terminal width settings. '
                'You can change this value by specifying the argument -ps or --preview-size '
                'followed by an integer (the number of characters to display from each file). '
                'Example: count-files --file-extension txt --preview --preview-size 50 '
                '~/Documents <arguments>.'
    },
    'file-sizes': {
        'name': '-fs, --file-sizes',
        'short': 'Show size info for each '
                 'found file when using -fe or --file_extension. '
                 'Additional information: total combined size and average file size.',
        'long': 'Show size info for each '
                'found file when using -fe or --file_extension. '
                'Additional information: total combined size and average file size. '
                'Example: count-files --file-extension txt --file-sizes ~/Documents <arguments>.'
    }
}


# indexes for searching in help text and sorting arguments
indexes = {
    ('h', 'help', 'service', 'optional'):
        [args['help']['name'], args['help']['short'],  args['help']['long']],
    ('ah', 'args-help', 'args', 'help', 'service', 'optional'):
        [args['args-help']['name'], args['args-help']['short'], args['args-help']['long']],
    ('v', 'version', 'service', 'optional'):
        [args['version']['name'], args['version']['short'], args['version']['long']],
    ('st', 'supported-types', 'supported', 'types', 'service', 'optional'):
        [args['supported-types']['name'], args['supported-types']['short'], args['supported-types']['long']],

    ('path', 'common', 'positional'):
        [args['path']['name'], args['path']['short'], args['path']['long']],
    ('a', 'all', 'common', 'optional'):
        [args['all']['name'], args['all']['short'], args['all']['long']],
    ('nr', 'no-recursion', 'no', 'recursion', 'common', 'optional'):
        [args['no-recursion']['name'], args['no-recursion']['short'], args['no-recursion']['long']],
    ('c', 'case-sensitive', 'case', 'sensitive', 'common', 'optional'):
        [args['case-sensitive']['name'], args['case-sensitive']['short'], args['case-sensitive']['long']],
    ('nf', 'no-feedback', 'no', 'feedback', 'common', 'optional'):
        [args['no-feedback']['name'], args['no-feedback']['short'], args['no-feedback']['long']],

    ('total-group', 'groups', 'total', 'group', 'tg'):
        [args['total-group']['name'], args['total-group']['short'], args['total-group']['long']],
    ('t', 'total', 'extension', 'special', 'optional'):
        [args['total']['name'], args['total']['short'], args['total']['long']],

    ('count-group', 'groups', 'count', 'group', 'cg'):
        [args['count-group']['name'], args['count-group']['short'], args['count-group']['long']],
    ('alpha', 'sort-alpha', 'count', 'special', 'optional'):
        [args['sort-alpha']['name'], args['sort-alpha']['short'], args['sort-alpha']['long']],

    ('search-group', 'groups', 'search', 'group', 'sg'):
        [args['search-group']['name'], args['search-group']['short'], args['search-group']['long']],
    ('fe', 'file-extension', 'file', 'extension', 'search', 'special', 'optional'):
        [args['file-extension']['name'], args['file-extension']['short'], args['file-extension']['long']],
    ('p', 'preview', 'search', 'special', 'optional'):
        [args['preview']['name'], args['preview']['short'], args['preview']['long']],
    ('ps', 'preview-size', 'preview', 'size', 'search', 'special', 'optional'):
        [args['preview-size']['name'], args['preview-size']['short'], args['preview-size']['long']],
    ('fs', 'file-sizes', 'file', 'sizes', 'search', 'special', 'optional'):
        [args['file-sizes']['name'], args['file-sizes']['short'], args['file-sizes']['long']]
}


if __name__ == '__main__':
    pass
