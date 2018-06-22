# Countfiles

Python package and Command Line Interface, CLI.

---
Последнее обновление описания: 21.06.2018
## Описание проекта
Утилита для получения информации о файлах в заданной директории.
Доступные опции: подсчет всех файлов, независимо от их типа, или поиск файлов с определенным расширением.
## Технические требования
- Python 3.6.x
- Поддерживаемые операционные системы: Windows, Linux, Mac OS
## Зависимости
- [puremagic==1.4](https://pypi.org/project/puremagic/)
## Как установить
Установка может быть выполнена с помощью [pip](https://pypi.org/project/pip/)

Пример с [pip [options] [-e] <vcs project url>](https://pip.pypa.io/en/stable/reference/pip_install/#usage):

```
pip install -e git+https://github.com/victordomingos/Count-files.git#egg=destination_folder_name
```

## Как использовать CLI

Вызов справки:

```
python -m countfiles -h
```

```
usage: countfiles [-h] [-v] [-st] [-a] [-nr] [-nf] [-alpha] [-nt]
                  [-fe FILE_EXTENSION] [-p] [-ps PREVIEW_SIZE] [-nl]
                  [path]

Count files, grouped by extension, in a directory. By default, it will count
files recursively in current working directory and all of its subdirectories,
and will display a table showing the frequency for each file extension (e.g.:
.txt, .py, .html, .css) and the total number of files found. Any hidden files
or folders are ignored by default.(Windows: files and directories for which
FILE_ATTRIBUTE_HIDDEN is true; Linux, Mac OS: those with names starting with
'.')

positional arguments:
  path                  The path to the folder containing the files to be
                        counted.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -st, --supported-types
                        The list of currently supported file types for
                        preview.
  -a, --all             Include hidden files and directories. Windows: files
                        and directories for which FILE_ATTRIBUTE_HIDDEN is
                        true; Linux, Mac OS: those with names starting with
                        '.'(dot)
  -nr, --no-recursion   Don't recurse through subdirectories.
  -nf, --no-feedback    Don't show the program's operating indicator(printing
                        processed file names in one line). Feedback is
                        available by default for counting files by
                        extension(table and no-table), searching for files by
                        extension(viewing mode no-list). This option disables
                        it.

File counting by extension:
  Counting all files in the specified directory with or without extensions.
  Default settings: recursively count all files, ignoring hidden files and
  directories; path - the current working directory; view mode - a table
  with file extensions sorted by frequency; feedback - printing processed
  file names in one line, use '-nf' to disable it. Usage: countfiles [-a]
  [-nr] [-nf] [-alpha] [-nt] [path]

  -alpha, --sort-alpha  Sort the table alphabetically, by file extension.
  -nt, --no-table       Don't show the table, only the total number of files.

File searching by extension:
  Search for files with a given extension. Default settings: recursively
  search all files, ignoring hidden files and directories; path - the
  current working directory; view mode - a list with full file paths;
  preview size - ... chars; feedback - printing processed file names in one
  line(available by default only for '-nl' or '--no-list', use '-nf' to
  disable it). Usage: countfiles [-a] [-nr] [-nf] [-fe FILE_EXTENSION] [-p]
  [-ps PREVIEW_SIZE] [-nl] [path]

  -fe FILE_EXTENSION, --file-extension FILE_EXTENSION
                        Search files by file extension (use a single dot '.'
                        to search for files without any extension).
  -p, --preview         Display a short preview (only available for text files
                        when using '-fe' or '--file_extension').
  -ps PREVIEW_SIZE, --preview-size PREVIEW_SIZE
                        Specify the number of characters to be displayed from
                        each found file when using '-p' or '--preview'.
  -nl, --no-list        Don't show the list, only the total number of files
                        and information about file sizes.
```

Аргументы могут быть указаны как в короткой, так и в длинной форме. Например: ```-a``` или ```--all```.

### Выбор директории для подсчета/поиска файлов
Если позиционный аргумент ```path``` не указан, то будет проверена текущая рабочая директория.
Выбрать директорию можно следующими способами.
#### Перейти в нужную папку

Windows:

```
cd C:\Users\Username\PycharmProjects
```

```
C:\Users\Username\PycharmProjects>python -m countfiles <arguments>
```

Linux, Mac OS: TODO

#### Указать полный путь

Windows:

```
python -m countfiles E:\Книги <arguments>
```

Если в названиях папок присутствуют пробелы, то path следует указать в кавычках:

```
python -m countfiles "C:\Users\Username\Pictures\Снимки экрана" <arguments>
```

Linux, Mac OS: TODO

#### Для обработки файлов в домашнем каталоге пользователя можно использовать ```~```

Windows:

```
python -m countfiles ~\Desktop <arguments>
```

Linux, Mac OS: TODO

### Включение или исключение скрытых файлов и папок

По умолчанию скрытые файлы и папки игнорируются, для их обработки используйте аргумент ```--all```.

#### Скрытые файлы и папки
- Windows: файлы и папки для которых установлен FILE_ATTRIBUTE_HIDDEN
- Linux, Mac OS: файлы и папки имена которых начинаются с точки ```.```

### Рекурсивный или нерекурсивный подсчет/поиск файлов

По умолчанию используется рекурсивный способ, укажите аргумент ```--no-recursion``` если нет необходимости в информации о файлах из субдиректорий.

### Особенности поиска файлов по расширению

Названия расширений чувствительны к регистру. Результаты для ```ini``` и ```INI``` будут разными.

Для поиска файлов без расширения используйте символ ```.``` (точка)

Примечание: файлы с именами типа ```.gitignore```, ```Procfile```, ```_netrc```.

```
python -m countfiles --file-extension . <arguments>
```

### Возможность отображения предварительного просмотра для некоторых типов файлов (доступно для опции поиска по определенному расширению)
  - для получения справки о расширениях файлов, для которых доступно превью, используйте аргумент ```--supported-types```
  - для включения отображения предварительного просмотра укажите аргумент ```--preview```
  - количество символов для просмотра по умолчанию зависит от настроек ширины терминала и может быть изменено с помощью ```--preview-size```

### Отключение индикатора работы программы

Программа динамично отображает имена обрабатываемых файлов в терминале если они соответствуют запросу.

Имена файлов не отображаются:
- при поиске по определенному расширению, если искомых файлов в папке нет
- если файлы являются скрытыми, а аргумент ```--all``` не указан

Индикатор работы программы включен для подсчета всех файлов и для поиска по расширению с использованием аргумента ```--no-list```. Для его отключения используйте ```--no-feedback```. Это также позволит несколько ускорить обработку файлов.

### Выбор режима просмотра результатов

#### Режимы просмотра по умолчанию:
- для подсчета всех файлов это таблица  с расширениями файлов, отсортированными по частоте
- для поиска по расширению это список с полными путями к найденным файлам, информация об их общем количестве и размерах

#### Изменение настроек просмотра:
- для опции подсчета используйте аргумент ```--sort-alpha``` для сортировки таблицы по алфавиту, для отображения только общего количества наденных файлов используйте аргумент ```--no-table```
- при поиске по расширению используйте аргумент ```--no-list``` для отображения только количества наденных файлов, их общего объема, среднего, минимального и максимального размера файла

### Примеры

Аргументы можно указывать в любом порядке.

#### Подсчет файлов всех типов

```countfiles [-a] [-nr] [-nf] [-alpha] [-nt] [path]```

Подсчет со значениями по умолчанию:

рекурсивно, в текущей рабочей директории, игнорируя скрытые файлы и папки, индикатор работы программы включен.

```
python -m countfiles
```

Результат: таблица  с расширениями файлов, отсортированными по частоте.

Recursively counting all files, ignoring hidden files and directories, in ...

| EXTENSION | FREQ. |
| --- | ---: |
| py | 17 |
| txt | 8 |
| [no extension] | 3 |
| TOTAL: | 28 |

---

Подсчет с выбранными аргументами:

без рекурсии, в указанной директории, включая скрытые файлы и папки, индикатор работы программы выключен.

```
python -m countfiles --all --no-recursion --no-feedback --no-table ~/path
```

Результат: отображение только общего количества наденных файлов.

Counting files, including hidden files and directories, in ...

Total number of files in selected directory: 8.

---

#### Поиск всех файлов с определенным расширением:

```countfiles [-a] [-nr] [-nf] [-fe FILE_EXTENSION] [-p] [-ps PREVIEW_SIZE] [-nl] [path]```

Подсчет со значениями по умолчанию:

рекурсивно, в текущей рабочей директории, без превью, игнорируя скрытые файлы и папки.

```
python -m countfiles --file-extension txt
```

Результат: список с полными путями к файлам с данным расширением (индикатором работы программы является сам список). Дополнительно предоставляется информация об общем количестве и размерах файлов.

Recursively searching all files with extension .txt, ignoring hidden files and directories, in ...

full/path/to/changelog.txt (3.0 KiB)

full/path/to/requirements.txt (16.0 B)

. . .

   Found 15 file(s).

   Total combined size: 19.4 KiB.

   Average file size: 1.3 KiB (max: 11.3 KiB, min: 3.0 B).

---

Подсчет с выбранными аргументами:

без рекурсии, в указанной директории, исключая скрытые файлы и папки, предварительный просмотр в размере 100 символов.

```
python -m countfiles ~/path --file-extension py --no-recursion --preview --preview-size 100
```

Результат: список с полными путями к файлам и превью, если оно доступно для данного типа файлов (индикатором работы программы является сам список). Дополнительно предоставляется информация об общем количестве и размерах файлов.

Searching files with extension .py, ignoring hidden files and directories, in ...

full/path/to/py_file_for_tests.py (76.0 B)

–––––––––––––––––––––––––––––––––––

Format: .py text/plain Python file 0.9

#!/usr/bin/env python3 """ A file with the extension .py to run tests """

–––––––––––––––––––––––––––––––––––

   Found 1 file(s).

   Total combined size: 76.0 B.

   Average file size: 76.0 B (max: 76.0 B, min: 76.0 B).

---

Подсчет с выбранными аргументами, без списка:

рекурсивно, в указанной директории, включая скрытые файлы и папки, без превью, индикатор работы программы включен.

```
python -m countfiles ~/path --file-extension . --all --no-list
```

Результат: отображение только количества найденных файлов, их общего объема, среднего, минимального и максимального размера файла.

Recursively searching all files without any extension, including hidden files and directories, in ...

   Found 4 file(s).

   Total combined size: 2.8 KiB.

   Average file size: 713.0 B (max: 2.6 KiB, min: 49.0 B).

---

### Вы нашли ошибку или у Вас есть предложения по улучшению?

Пожалуйста, задайте вопрос или оставьте комментарий в разделе Issues.