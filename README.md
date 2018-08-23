**[English](https://github.com/victordomingos/Count-files/blob/master/README.md)** | [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md) | [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439; &#x44F;&#x437;&#x44B;&#x43A;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)
  
  
# Count Files [![Github commits (since latest release)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)

A command-line interface (CLI) utility written in Python to help you
count files, grouped by extension, in a directory. By default, it will count
files recursively in current working directory and all of its subdirectories,
and will display a table showing the frequency for each file extension (e.g.:
.txt, .py, .html, .css) and the total number of files found.

Supported operating systems: Linux, Mac OS, Windows. It may also be used on 
iOS (iPhone/iPad) using the [StaSh](https://github.com/ywangd/stash) 
command-line in the Pythonista 3 app.


![Count Files_screenshot - counting files by extension](https://user-images.githubusercontent.com/18650184/42160179-29998a52-7dee-11e8-9813-b8594e50fe77.png)


## Contents
- **[Installation and dependencies](#installation-and-dependencies)**
   - [On regular desktop operating systems](#on-regular-desktop-operating-systems)
   - [On iPhone or iPad (in Pythonista 3 for iOS)](#on-iphone-or-ipad-in-pythonista-3-for-ios)
  
- **[How to use](#how-to-use)**  
   - [CLI arguments](#cli-arguments)
   - [Getting help on how to use this application](#getting-help-on-how-to-use-this-application)
   - [Hidden files and directories](#hidden-files-and-directories)
   - [Case sensitivity](#case-sensitivity)
   - [Customizing display of results and operation feedback](#customizing-display-of-results-and-operation-feedback)  
   - [Examples of practical usage](#examples-of-practical-usage)  
      - [Counting the total number of files in the directory](#counting-the-total-number-of-files-in-the-directory)  
      - [Counting how many files are there for each extension](#counting-how-many-files-are-there-for-each-extension)  
      - [Searching for files with a specific extension](#searching-for-files-with-a-specific-extension)
      - [Searching and listing files without extension](#searching-and-listing-files-without-extension)
      - [Searching and listing all files](#searching-and-listing-all-files)
      - [Other features](#other-features)
  
- **[Did you find a bug or do you have a suggestion?](#did-you-find-a-bug-or-do-you-have-a-suggestion)**


## Installation and dependencies:

### On regular desktop operating systems

The current development version can be installed with `pip install -e`,
followed by the path to the main project directory (the same directory that
has the `setup.py` file). To run this application, you need to have a working
Python 3.6+ installation.

We plan to submit this to PyPI as soon as possible, in order to provide a more
straight-forward installation and upgrade process. While that doesn't happen,
please feel free to take a look at the last section and maybe consider
contributing to this project.

### On iPhone or iPad (in Pythonista 3 for iOS)

First you will need a Python environment and a command-line shell compatible
with Python 3. Presently, it means you need to have an app called
[Pythonista 3](http://omz-software.com/pythonista/) (which is, among other
things, a very nice environment for developing and/or running pure Python
applications on iOS). 

Then you need to install
[StaSh](https://github.com/ywangd/stash), which is a Python-based shell
application for Pythonista. It will enable you to use useful commands like
`wget`, `git clone`, `pip install` and many others. It really deserves an home
screen shortcut on your iPhone or iPad. 

After following the instructions for
StaSh installation, you may need to update it to a more recent version. Try
this command:

```
selfupdate.py -f bennr01:command_testing
```

Then force-quit and restart Pythonista and launch StaSh again. It should now
be running in Python 3. You may now try to install this application, directly
from this git repository:

```
pip install victordomingos/Count-files
```

If all goes well, it should place a new `count_files`
package inside the `~/Documents/site-packages-3/` folder and create an
entry point script named `count-files.py` in `stash_extensions/bin`. Then force-quit and
launch StaSh again. You should now be able to run this application directly
from the shell to count any files that you may have inside your Pythonista
environment.


## How to use:

### CLI arguments

Arguments can be specified in both short and long form. For example: `-a` or `--all`.

```
usage: count-files [-h] [-v] [-st] [-a]
                   [-c] [-nr] [-nf] [-t TOTAL]
                   [-alpha] [-fe FILE_EXTENSION] [-fs]
                   [-p] [-ps PREVIEW_SIZE] [path]
```

```
usage: count-files [--help] [--version] [--supported-types] [--all]
                   [--case-sensitive] [--no-recursion] [--no-feedback] [--total TOTAL]
                   [--sort-alpha] [--file-extension FILE_EXTENSION] [--file-sizes]
                   [--preview] [--preview-size PREVIEW_SIZE] [path]
```

The most simple form of usage is to type a simple command in the shell, without 
any arguments. So, to count all files in current working directory and all of 
its subdirectories, ignoring hidden files and hidden subdirectories:

`count-files`

By default, it will count files recursively in current working directory and 
all of its subdirectories, and will display a table showing the frequency for 
each file extension (e.g.: .txt, .py, .html, .css) and the total number of 
files found. Any hidden files or folders will be ignored by default.

Another main feature of this application consists in searching files by a 
given extension, which presents to the user a list of all found files or, 
as an option, only the total number of matching files found.

```
count-files -fe txt
```

```
count-files --file-extension txt
```

Optionally, you can pass it a path to the directory to scan. If you prefer, you 
can leave that argument empty, and it will scan the current working directory.

To process files in the user's home directory, you can use ```~```

If there are spaces in the folder names, then `path` should be specified in quotation marks. Example for Windows:
```
count-files "~\Desktop\New folder"
```
The optional `-nr` or `--no-recursion` switch argument tells the
application not to scan recursively through the subdirectories.



### Getting help on how to use this application

To check the list of available options and their usage, you just need to use
one of the following commands:

```
count-files -h
```

```
count-files --help
```

  
### Hidden files and directories  

By default, it will ignore files and directories that are supposed to be
hidden, but you can add the `-a` or `--all` optional
switch argument to make it count all files.

Windows: files and directories for which FILE_ATTRIBUTE_HIDDEN is true  
Linux, Mac OS: those with names starting with "."(dot)
  

### Case sensitivity

The names of extensions are case insensitive by default. The results for
`ini` and `INI` will be the same. To distinguish between similar
extensions in different cases, use the `-c` or `--case-sensitive` switch
argument.


### Customizing display of results and operation feedback

This utility can also be used to search for files that have a certain file extension
(using `-fe` or `--file-extension`) and, optionally, display a short preview (`-p`or 
`--preview`) for text files. The size of the preview text sample can optionally be
customized by using the `-ps` or `--preview-size` argument followed by an integer number 
specifying the number of characters to present.

The list of file types for which preview is available can be viewed with
the `-st` or `--supported-types` argument.

By default, the result of a search by certain file extension is a list with 
the full paths of the files found. If you need information about the size of the files, use the `-fs` or `--file-sizes` argument.

If you only need the total number of all files, number of files with a certain extension or without it 
use the `-t` or `--total` argument.

The program's operating indicator is printing processed file names in one line.
File names are not displayed when searching for a particular extension, if 
there are no such files in the folder or if the files are hidden, and the 
argument `--all` is not specified.

Feedback is available by default for counting files by extension (table)
 and for counting the total number of files. Optional 
argument `-nf` or `--no-feedback` disables it.

Using the `--no-feedback` argument allows you to speed up the 
processing of files a little.

To search for files by extension (using `-fe` or `--file-extension`) feedback is the list itself.
  
  
  
  By default, the table will be sorted by the file extension frequency. If you
prefer alphabetically sorted results, you just need to add the `-alpha` or 
`--sort-alpha` argument.

  
### Examples of practical usage:

#### Counting the total number of files in the directory

Short form of arguments  
```
usage: count-files [-a] [-c] [-nr] [-nf] [-t TOTAL] [path]
```
Long form of arguments  
```
usage: count-files [--all] [--case-sensitive] [--no-recursion] [--no-feedback] [--total TOTAL] [path]
```

To count the total number of files, you must specify
the name of the extension or use a single dot ```.``` to get the total number of files without any extension.  
Use two dots without spaces ```..``` to get the total number of all files with or without the extension.

Recursively count the total number of files with a specific extension in the current directory, including hidden files and hidden subdirectories:

```
count-files -a -t txt
```

```
count-files --all --total txt
```

Recursively count the total number of files with a specific extension in uppercase:

```
count-files -t JPG -c
```

```
count-files --total JPG --case-sensitive
```

Recursively count the total number of files without any extension:

```
count-files -t .
```

```
count-files --total .
```

Counting the total number of files in the current directory, regardless of the extension and without recursion:
```
count-files -nr -t ..
```

```
count-files --no-recursion --total ..
```

#### Counting how many files are there for each extension

Short form of arguments  
```
usage: count-files [-a] [-alpha] [-c] [-nr] [-nf] [path]
```
Long form of arguments  
```
usage: count-files [--all] [--sort-alpha] [--case-sensitive] [--no-recursion] [--no-feedback] [path]
```

By default, the table will be sorted by the file extension frequency. If you
prefer alphabetically sorted results, you just need to add the `-alpha` or 
`--sort-alpha` argument.

  
  
Count all files in current working directory and all of its subdirectories, 
ignoring hidden files and hidden subdirectories:  
In this case, the file extensions in the table will be displayed in uppercase (default).

```
count-files
```

Count all files in current working directory and all of its subdirectories, 
ignoring hidden files and hidden subdirectories, with `--case-sensitive` argument:  
In this case, the file extensions in the table will be displayed as is (in lowercase and uppercase).

```
count-files -c
```

```
count-files --case-sensitive
```

Count all files in current working directory and all of its subdirectories, 
including hidden files and hidden subdirectories:

```
count-files -a
```  

```
count-files --all
```


Count all files in current working directory, ignoring hidden files and hidden 
subdirectories, and without recursing through subdirectories:

```
count-files -nr
```  

```
count-files --no-recursion
```


Count all files in a given directory with recursion:

```
count-files ~/Documents
```


Count all files in a given directory without recursing through subdirectories, 
and sort the table alphabetically:

```
count-files -nr -alpha ~/Documents
```  

```
count-files --no-recursion --sort-alpha ~/Documents
```


Count all files in a given directory with recursion, ignoring hidden files and 
hidden subdirectories, without feedback:

```
count-files -nf ~/Documents
```  

```
count-files --no-feedback ~/Documents
```


### Searching for files with a specific extension

Short form of arguments  
```
usage: count-files [-a] [-c] [-nr]
                   [-fe FILE_EXTENSION] [-fs]
                   [-p] [-ps PREVIEW_SIZE] [path]
```

Long form of arguments  
```
usage: count-files [--all] [--case-sensitive] [--no-recursion]
                   [--file-extension FILE_EXTENSION] [--file-sizes]
                   [--preview] [--preview-size PREVIEW_SIZE] [path]
```

Search recursively for any files that have a `.txt` extension, including hidden files, in a given 
directory:

```
count-files -a -fe txt ~/Documents
```
  
```
count-files --all --file-extension txt ~/Documents
```


Search recursively for any files that have a `.css` extension, in a given directory, including information about the size of the files:

```
count-files -fe css -fs ~/Documents
```  

```
count-files --file-extension css --file-sizes ~/Documents
```


Search recursively for any files that have a `.py` extension, in a given 
directory, and display a 500 characters preview for each one:

```
count-files -fe py -p -ps 500 ~/Documents
```   

```
count-files --file-extension py --preview --preview-size 500 ~/Documents
```


#### Searching and listing files without extension

Use a single dot ```.``` to search for files without any extension.  
Note: files with names such as `.gitignore`,` Procfile`, `_netrc`.

Search recursively for any files that don't have any extension, in a given directory:

```
count-files -fe .  ~/Documents
```
  
```
count-files --file-extension . ~/Documents
```


#### Searching and listing all files

Use two dots without spaces ```..``` to search for all files with or without the extension.

Recursively searching all files with extension or without it, in a given directory:  
(similar to counting recursively for any files, but the result is a list with paths)

```
count-files -fe ..  ~/Documents
```
  
```
count-files --file-extension .. ~/Documents
```


#### Other features

Check the version number of the program:

```
count-files -v
```  

```
count-files --version
```


Get the list of currently supported file types for preview:

```
count-files -st
```
  
```
count-files --supported-types
```


## Did you find a bug or do you have a suggestion?

Please let me know, by opening a new issue or a pull request.
