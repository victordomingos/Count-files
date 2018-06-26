# Count Files [![Github commits (desde a última versão)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)
Um pequeno utilitário com interface de linha de comandos (CLI) escrito em 
Python para ajudar a contar ficheiros por extensão, numa determinada pasta.
Por predefinição, a aplicação contará os ficheiros recursivamente na pasta
de trabalho atual e em todas as suas subpastas e apresentará uma tabela
mostrando a frequência de cada extensão de ficheiro (p.ex.: .txt, .py,
.html, .css) e o número total de ficheiros encontrados. Quaisquer pastas ou
ficheiros escondidos serão ignorados por defeito.

Sistemas operativos suportados: Linux, Mac OS, Windows.

Ler o ficheiro README em outras línguas: [English](https://github.com/victordomingos/Count-files/blob/master/README.md) | [Русский язык](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)

![Captura de ecrã da aplicação Count-files](https://user-images.githubusercontent.com/18650184/39443000-1bd83b62-4cab-11e8-9942-242ba29232d7.png)


## Conteúdo  
- [Descrição](#descrição)  
- [Exemplos de utilização](#exemplos-de-utilização)  
- [Instalação e dependências](#instalação-e-dependências)  
- [Encontrou um bug ou tem uma sugestão?](#encontrou-um-bug-ou-tem-uma-sugestão)

## Descrição:

Opcionalmente, é possivel indicar um caminho para a pasta a processar. Se 
preferir, poderá deixar esse argumento vazio, e a aplicação irá contar os 
ficheiros da pasta atual.

Os argumentos optionais `-nr` ou `--no-recursion` dizem à aplicação para não
percorrer de forma recursiva todas as subpastas (ou seja, pesquisar apenas na
raiz da pasta indicada).

Por predefinição, a tabela será ordenada pela frequência das extensões dos 
nomes de ficheiros. Se preferir visualizar resultados ordenados alfabeticamente,
basta adicionar o argumento `-alpha` or `--sort-alpha`.

De modo semelhante, as opções `-nt` ou `--no-table` instruem a aplicação para
não mostrar uma tabela com a lista de todas as extensões encontradas e 
respetivas frequências, ou seja, apresentando apenas o número total de ficheiros.

Por predefinição, serão ignorados ficheiros e pastas

By default, it will ignore files and directories that are supposed to be
hidden, but you can add the `-a` or `--all` optional
switch argument to make it count all files.

Hidden files and directories  
Windows: files and directories for which FILE_ATTRIBUTE_HIDDEN is true  
Linux, Mac OS: those with names starting with "."(dot)

This utility can also be used to search for files that have a certain file extension
(using `-fe` or `--file-extension`) and, optionally, display a short preview (`-p`or 
`--preview`) for text files. The size of the preview text sample can optionally be
customized by using the `-ps` or `--preview-size` argument followed by an integer number.

The list of file types for which preview is available can be viewed with the `-st` or `--supported-types` argument.
The names of extensions are case sensitive. The results for `ini` and `INI` will be different.

By default, the result of a search by certain file extension is a list with the full paths of the files found.
If you only need the total number of files, use the `-nl` or `--no-list` argument.

The program's operating indicator is printing processed file names in one line.
File names are not displayed when searching for a particular extension, if there are no such files in the folder or if the files are hidden, and the argument `--all` is not specified.

Feedback is available by default for counting files by extension(table and no-table),
searching for files by extension(viewing mode no-list). Optional argument `-nf` or `--no-feedback` disables it.

Using the arguments `--no-feedback` and `--no-list` allows you to speed up the processing of files a little.

## Exemplos de utilização:

Get a little help about how to use this application:

`countfiles -h`  
`countfiles --help`


Get the version number of the program:

`countfiles -v`  
`countfiles --version`


Get the list of currently supported file types for preview:

`countfiles -st`  
`countfiles --supported-types`


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


Count all files in a given directory with recursion, ignoring hidden files and hidden subdirectories, without feedback:

`countfiles -nf ~/Documents`  
`countfiles --no-feedback ~/Documents`


Search recursively for any files that have a `.txt` extension, in a given directory, without list and without feedback:


`countfiles -nf -nl -fe txt ~/Documents`  
`countfiles --no-feedback --no-list --file-extension txt ~/Documents`


Search recursively for any files that have a `.css` extension, in a given directory:

`countfiles -fe css ~/Documents`  
`countfiles --file-extension css ~/Documents`


Search recursively for any files that have a `.py` extension, in a given directory, and display a 500 characters preview for each one:

`countfiles -fe py -p -ps 500 ~/Documents`   
`countfiles --file-extension py --preview --preview-size 500 ~/Documents`

Search recursively for any files that don't have any extension, in a given directory:

`countfiles -fe .  ~/Documents`  
`countfiles --file-extension . ~/Documents`


Recursively searching all files with extension or without it, in a given directory:  
(similar to counting recursively for any files, but the result is a list with paths)

`countfiles -fe ..  ~/Documents`  
`countfiles --file-extension .. ~/Documents`


## Instalação e dependências:

The current development version can be installed with `pip install -e`, followed by the path to the main project directory (the same directory that has the `setup.py` file). To run this application, you need to have a working Python 3.6+ instalation. We try to keep the external dependencies at a minimum, in order to keep compatibility with different plataforms, including Pythonista on iOS. At this moment, we require:

- puremagic==1.4

We plan to submit this to PyPI as soon as possible, in order to provide a more straight-forward instalation and upgrade process. While that doesn't happen, please feel free to take a look at the next section and maybe consider contributing to this project.


## Encontrou um bug ou tem uma sugestão?

Please let me know, by opening a new issue or a pull request.
