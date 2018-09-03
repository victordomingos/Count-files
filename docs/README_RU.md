[English](https://github.com/victordomingos/Count-files/blob/master/README.md) | [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md) | **[&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)** | [&#x423;&#x43A;&#x440;&#x430;&#x457;&#x43D;&#x441;&#x44C;&#x43A;&#x430;](https://github.com/victordomingos/Count-files/blob/master/docs/README_UA.md)
  
  
# Count Files [![Github commits (since latest release)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)

Утилита командной строки (CLI), написанная на Python. C помощью этой CLI можно подсчитать или найти файлы с определенным расширением, без расширения или все файлы, независимо от расширения, в указанном каталоге.

![Count Files_screenshot - counting files by extension](https://user-images.githubusercontent.com/18650184/42160179-29998a52-7dee-11e8-9813-b8594e50fe77.png)


## Документация

- [Английский](https://countfiles.readthedocs.io/en/latest/)

## Установка

### На настольные операционные системы

Count Files - это кроссплатформенная программа, которая может быть установлена с помощью [pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip3 install count-files
```

Текущую версию разработки проекта можно установить с [`pip3 install -e`](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs).

### На iPhone или iPad (в Pythonista 3 для iOS)

Также может использоваться
на iOS (iPhone/iPad) с помощью командной строки [StaSh](https://github.com/ywangd/stash) в приложении Pythonista 3.  
Более подробное описание в [документации](https://countfiles.readthedocs.io/en/latest/installation.html) по установке. 

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

По умолчанию программа считает или ищет файлы рекурсивно в текущем рабочем каталоге и во всех его подкаталогах. Скрытые файлы и папки игнорируются. Расширения по умолчанию не чувствительны к регистру. Результаты для `ini` и `INI` будут одинаковыми.

Вы можете явно указать path к нужной папке, выбрать нерекурсивный способ подсчета или поиска, найти файлы по расширению с учетом регистра, включить подсчет или поиск в скрытых файлах и папках.  
Также доступно получение дополнительной информации о размере каждого найденного файла и короткий предварительный просмотр для текстовых файлов.  
Более подробно: [аргументы CLI](https://countfiles.readthedocs.io/en/latest/howtouse.html#cli-arguments).

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

Также вы можете подсчитать только общее количество файлов с определенным расширением.

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

Если нужны все файлы независимо от их расширения, укажите две точки в качестве названия расширения.

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

## Вы нашли ошибку или у Вас есть предложения по улучшению?

Пожалуйста, задайте вопрос в разделе Issues или откройте pull request в [репозитории](https://github.com/victordomingos/Count-files).
