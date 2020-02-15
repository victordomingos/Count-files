[English](https://github.com/victordomingos/Count-files/blob/master/README.md) | [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md) | **[&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)** | [&#x423;&#x43A;&#x440;&#x430;&#x457;&#x43D;&#x441;&#x44C;&#x43A;&#x430;](https://github.com/victordomingos/Count-files/blob/master/docs/README_UA.md)
  
  
# Count Files [![Github commits (since latest release)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)

Утилита командной строки (CLI), написанная на Python. C помощью этой CLI можно подсчитать или найти файлы с определенным расширением, без расширения или все файлы, независимо от расширения, в указанном каталоге.

![Count Files_screenshot - counting files by extension](https://user-images.githubusercontent.com/18650184/42160179-29998a52-7dee-11e8-9813-b8594e50fe77.png)


## Документация

- [Английский](https://countfiles.readthedocs.io/en/latest/)
- [Русский](https://github.com/victordomingos/Count-files/tree/master/docs/documentation_ru/README.md)

## Установка

### На настольные операционные системы

Count Files - это кроссплатформенная программа, которая может быть легко установлена с помощью [pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip3 install count-files
```

Если вас интересует текущая версия разработки, вы можете клонировать этот git-репозиторий и установить ее с помощью [`pip3 install -e`](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs). Однако обратите внимание, что только выпущенные версии будут стабильными и полезными. Текущая development версия может быть нестабильной и содержать баги.

### На iPhone или iPad (в Pythonista 3 для iOS)

Также может использоваться
на iOS (iPhone/iPad) с помощью командной строки [StaSh](https://github.com/ywangd/stash) в приложении Pythonista 3.  
Более подробное описание в [документации](https://github.com/victordomingos/Count-files/tree/master/docs/documentation_ru/installation.md) по установке. 

## Зависимости

Для работы приложения требуется версия Python 3.6+.

## Как использовать

Чтобы проверить список доступных аргументов, вам просто нужно использовать одну из следующих команд:

```
count-files -h
```

```
count-files --help
```

По умолчанию программа считает или ищет файлы рекурсивно в текущем рабочем каталоге и во всех его подкаталогах.  
Для полностью поддерживаемых операционных систем (Linux, macOS, iOS, Windows) 
любые скрытые файлы или папки по умолчанию игнорируются. 
Для других операционных систем, в которых можно запускать Python, 
возможность включения/исключения скрытых файлов на данный момент недоступна. И в результате все файлы будут включены.  
Расширения по умолчанию не чувствительны к регистру. Результаты для `ini` и `INI` будут одинаковыми.

Вы можете явно указать path к нужной папке, выбрать нерекурсивный способ подсчета или поиска, найти файлы по расширению с учетом регистра, включить подсчет или поиск в скрытых файлах и папках.  
При подсчете всех файлов по расширению (таблица):  
можно отсортировать расширения по алфавиту.  
При поиске файлов по расширению (аргумент `--file-extension`):  
доступно получение дополнительной информации о размере каждого найденного файла и короткий предварительный просмотр для текстовых файлов.  
При подсчете общего количества файлов (аргумент `--total`):  
вы также можете получить список папок, в которых находятся найденные файлы, количество найденных файлов в каждой папке и общий суммарный размер этих файлов.  
Более подробно: [аргументы CLI](https://github.com/victordomingos/Count-files/blob/master/docs/documentation_ru/howtouse.md#аргументы-cli).

Наиболее простой формой использования является ввод команды без всяких аргументов. Результатом будет таблица, показывающая частоту для каждого расширения файла (например: .txt, .py, .html, .css) и общее количество найденных файлов.

```
count-files
```

С помощью CLI можно искать файлы с определенным расширением. Результат поиска - список с полными путями ко всем найденным файлам.

```
count-files -fe txt [path]
```  
```
count-files --file-extension txt [path]
```

Также вы можете подсчитать только общее количество файлов с определенным расширением, без списка.

```
count-files -t py [path]
```  
```
count-files --total py [path]
```

Для получения информации о файлах без расширения, укажите одну точку в качестве названия расширения.

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

Если нужно получить список путей ко всем файлам или подсчитать общее их количество независимо от расширения, укажите две точки в качестве названия расширения.

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

Вы также можете искать файлы по шаблону, с использованием символов подстановки:  `*`, `?`, `[seq]`, `[!seq]`.

```
count-files -fm *.py? [path]
```
```
count-files --filename-match *.py? [path]
```

## Вы нашли ошибку или у Вас есть предложения по улучшению?

Пожалуйста, задайте вопрос в разделе Issues или откройте pull request в [репозитории](https://github.com/victordomingos/Count-files).
