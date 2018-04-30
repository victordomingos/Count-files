# Count Files
A little CLI utility written in Python to help you count files, grouped by
extension, in a directory. By default, it will count files recursively in
current working directory and all of its subdirectories, and will display a
table showing the frequency for each file extension (e.g.: .txt, .py, .html,
.css) and the total number of files found.

Optionally, you can pass it a path to the directory to scan. If you or leave
that argument empty and it will scan the current working directory.

The optional `-nr` (i.e., "no recursion") switch argument tells the
application not to scan recursively through the subdirectories.

Similarly, the optional `-nt` (i.e., "no table") switch tells the application
not to show a table listing all the found file extensions and their respective
frequencies, so that it will only display the total number of files.


## Examples of usage:

Count all files in current working directory and all of its subdirectories:

`countfiles.py`


Get a little help about how to use this application:

`countfiles.py -h`
`countfiles.py --help`


Count all files in current working directory without recursing through subdirectories:

`countfiles.py -nr`


Count all files in a given directory with recursion:

`countfiles.py ~/Documents`


Count all files in a given directory with recursion, but don't display a table, only the total number of files:

`countfiles.py ~/Documents`


Count all files in a given directory without recursing through subdirectories:

`countfiles.py -nr ~/Documents`


## Did you find a bug or do you have a suggestion?

Please let me know, by opening a new issue.