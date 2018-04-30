# Count Files
A little CLI utility written in Python to help you count files, grouped by
extension, in a directory. You can either pass it the path to the directory to
scan, or leave that argument empty and it will scan the current working
directory. The -nr (i.e., "no recursion") switch tells the application not to
scan recursively through the subdirectories.


## Examples of usage:

- Count all files in current working directory and all of its subdirectories:

```
countfiles.py
```

- Count all files in current working directory without recursing through subdirectories:

```
countfiles.py -nr
```

- Count all files in a given directory with recursion:

```
countfiles.py ~/Documents
```


- Count all files in a given directory without recursing through subdirectories:

```
countfiles.py -nr ~/Documents
```
