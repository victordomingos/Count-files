**[English](https://github.com/victordomingos/Count-files/blob/master/README.md)** | [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md) | [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439; &#x44F;&#x437;&#x44B;&#x43A;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)
  
  
# Count Files [![Github commits (since latest release)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)

A command-line interface (CLI) utility written in Python to help you
counting or searching files with a specific extension, files without an extension or all files regardless of the extension, in the specified directory.

![Count Files_screenshot - counting files by extension](https://user-images.githubusercontent.com/18650184/42160179-29998a52-7dee-11e8-9813-b8594e50fe77.png)


## Documentation

- [English](https://countfiles.readthedocs.io/en/latest/)

## Installation

### On regular desktop operating systems

Count Files is a multiplatform application that can be installed using [pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip3 install count-files
```

The current development version can be installed with [`pip3 install -e`](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).

### On iPhone or iPad (in Pythonista 3 for iOS)

It may also be used on iOS (iPhone/iPad) using the [StaSh](https://github.com/ywangd/stash) 
command-line in the Pythonista 3 app.  
See [documentation](https://countfiles.readthedocs.io/en/latest/installation.html) for instructions. 

## Dependencies

To run this application, you need to have a working Python 3.6+ installation.

## How to use

To check the list of available options and their usage, you just need to use
one of the following commands:

```
count-files -h
```

```
count-files --help
```

By default, the program counts or searches for files recursively in current working directory and all of its subdirectories. Any hidden files or folders will be ignored.
The names of extensions are case insensitive by default. The results for `ini` and `INI` will be the same.

Optionally, you can pass it a path to the directory to scan, choose non-recursive counting or searching, process the file extensions with case-sensitive mode and enable search or counting in hidden files and folders.  
You can get additional information about the size of each found file and see a short preview for text files.  
See more about [CLI arguments](https://countfiles.readthedocs.io/en/latest/howtouse.html#cli-arguments).

The most simple form of usage is to type a simple command in the shell, without 
any arguments. It will display a table showing the frequency for 
each file extension (e.g.: .txt, .py, .html, .css) and the total number of 
files found.

```
count-files
```

Another main feature of this application consists in searching files by a 
given extension, which presents to the user a list of all found files paths.

```
count-files -fe txt [path]
```  
```
count-files --file-extension txt [path]
```

You can also count the total number of files with a certain extension.

```
count-files -t py [path]
```  
```
count-files --total py [path]
```

For information about files without an extension, specify a single dot as the extension name.


```
count-files -fe . [path]
```  
```
count-files --file-extension . [path]
```

```
count-files -t . [path]
```  
```
count-files --total . [path]
```

If you need all the files, regardless of the extension, specify two dots as the extension name.

```
count-files -fe .. [path]
```  
```
count-files --file-extension .. [path]
```

```
count-files -t .. [path]
```  
```
count-files --total .. [path]
```

## Did you find a bug or do you have a suggestion?

Please, open a new issue or a pull request to the [repository](https://github.com/victordomingos/Count-files).
