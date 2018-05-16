# Count Files
A little command-line interface (CLI) utility written in Python to help you
count files, grouped by extension, in a directory. By default, it will count
files recursively in current working directory and all of its subdirectories,
and will display a table showing the frequency for each file extension (e.g.:
.txt, .py, .html, .css) and the total number of files found. Any hidden files
or folders (those with names starting with '.') are ignored by default.

![Count-files screenshot](https://user-images.githubusercontent.com/18650184/39443000-1bd83b62-4cab-11e8-9942-242ba29232d7.png)

Optionally, you can pass it a path to the directory to scan. If you prefer, you can leave that argument empty, and it will scan the current working directory.

The optional `-nr` or `--no-recursion` switch argument tells the
application not to scan recursively through the subdirectories.

By default, the table will be sorted by the file extension frequency. If you
prefer alphabetically sorted results, you just need to add the `-alpha` or `--sort-alpha` 
argument.

Similarly, the optional `-nt` or `--no-table` switch tells the application
not to show a table listing all the found file extensions and their respective
frequencies, so that it will only display the total number of files.

By default, it will ignore files and directories that are supposed to be
hidden (with names starting with '.', but you can add the `-a` or `--all` optional
switch argument to make it count all files.

This utility can also be used to search for files that have a certain file extension
(using `-fe` or `--file-extension`) and, optionally, display a short preview (`-p`or 
`--preview`) for text files. The size of the preview text sample can optionally be
customized by using the `-ps` or `--preview-size` argument followed by an integer number.


## Examples of usage:

Get a little help about how to use this application:

`countfiles -h`  
`countfiles --help`


Count all files in current working directory and all of its subdirectories, ignoring hidden files and hidden subdirectories:

`countfiles`


Count all files in current working directory and all of its subdirectories, including hidden files and hidden subdirectories:

`countfiles -a`  
`countfiles --all`


Count all files in current working directory, ignoring hidden files and hidden subdirectories, and without recursing through subdirectories:

`countfiles -nr`  
`countfiles --no-recursion`


Count all files in a given directory with recursion:

`countfiles ~/Documents`


Count all files in a given directory with recursion, but don't display a table, only the total number of files:

`countfiles -nt ~/Documents`  
`countfiles --no-table ~/Documents`


Count all files in a given directory without recursing through subdirectories, and sort the table alphabetically:

`countfiles -nr -alpha ~/Documents`  
`countfiles --no-recursion --sort-alpha ~/Documents`


Count all files in a given directory without recursing through subdirectories, including hidden files, and only displaying the total number of files (no table):

`countfiles -nr -nt -a ~/Documents`  
`countfiles --no-recursion --no-table --all ~/Documents`


Search recursively for any files that have a `.css` extension, in a given directory:

`countfiles -fe css ~/Documents`  
`countfiles --file-extension css ~/Documents`


Search recursively for any files that have a `.py` extension, in a given directory, and display a 500 characters preview for each one:

`countfiles -fe py -p -ps 500 ~/Documents`   
`countfiles --file-extension py --preview --preview-size 500 ~/Documents`

Search recursively for any files that don't have any extension, in a given directory:

`countfiles -fe .  ~/Documents`
`countfiles --file-extension . ~/Documents`


## Installation and dependencies:

The current development version can be installed with `pip install -e`, followed by the path to the main project directory (the same directory that has the `setup.py` file). To run this application, you need to have a working Python 3.6+ instalation. We try to keep the external dependencies at a minimum, in order to keep compatibility with different plataforms, including Pythonista on iOS. At this moment, we require:

- puremagic==1.4

We plan to submit this to PyPI as soon as possible, in order to provide a more straight-forward instalation and upgrade process. While that doesn't happen, please feel free to take a look at the next section and maybe consider contributing to this project.


## Did you find a bug or do you have a suggestion?

Please let me know, by opening a new issue or a pull request.
