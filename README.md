# Count Files
A little command-line interface (CLI) utility written in Python to help you count files, grouped by
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

## Dependencies:

To run this application, you just need to have a working Python 3.6+ instalation. No further dependencies.

The main file should have the execution permission bit set (`chmod +x`on Unix-like systems) and should be in a directory listed in the PATH environment variable (usually Python's `site-packages`).

I agree there should be a more straight-forward instalation process. While that doesn't happen, please feel free to take a look at the next section and maybe consider contributing to this project.

## Did you find a bug or do you have a suggestion?

Please let me know, by opening a new issue.