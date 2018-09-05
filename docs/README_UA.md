[English](https://github.com/victordomingos/Count-files/blob/master/README.md) | [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md) | [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md) | **[&#x423;&#x43A;&#x440;&#x430;&#x457;&#x43D;&#x441;&#x44C;&#x43A;&#x430;](https://github.com/victordomingos/Count-files/blob/master/docs/README_UA.md)**
  
  
# Count Files [![Github commits (since latest release)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)

Утиліта командного рядка (CLI), написана на Python. З допомогою цієї програми можна підраховувати та шукати файли з певним розширенням, без розширення чи всі файли, незалежно від їх розширення, в обраній директорії.

![Count Files_screenshot - counting files by extension](https://user-images.githubusercontent.com/18650184/42160179-29998a52-7dee-11e8-9813-b8594e50fe77.png)


## Документація

- [Англійська](https://countfiles.readthedocs.io/en/latest/)

## Встановлення

### На десктопні операційні системи

Count Files - це кросплатформна програма, яка може бути легко встановлена з допомогою [pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip3 install count-files
```

Якщо вас цікавить поточна версія розробки, ви можете клонувати цей git-репозиторій та встановити її за допомогою [`pip3 install -e`](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs). Проте зверніть увагу, що тільки випущені версії будуть стабільними та корисними. Поточна development версія може бути нестабільною та містити баги.

### На iPhone чи iPad (в Pythonista 3 для iOS)

Також може використовуватися на iOS (iPhone/iPad) з допомогою командного рядка [StaSh](https://github.com/ywangd/stash) у додатку Pythonista 3.  
Більш детальний опис у [документації](https://countfiles.readthedocs.io/en/latest/installation.html) по встановленню. 

## Залежності

Для запуску потрібна версія Python 3.6+.

## Як використовувати

Щоб отримати список доступних аргументів та короткий опис їх застосування просто введіть одну з наступних команд:

```
count-files -h
```

```
count-files --help
```

За замовчуванням програма здійснює підрахунок чи пошук файлів рекурсивно в поточному робочому каталозі та в усіх його підкаталогах. Приховані файли та каталоги ігноруються.
Розширення за замовчуванням не чутливі до регістру. Результат для `ini` та `INI` буде однаковий.

Ви маєте змогу вказати path до потрібної папки, обрати нерекурсивний підрахунок чи пошук, шукати файли враховуючи регістр розширення, включити підрахунок чи пошук у прихованих файлах та папках.  
Також доступне отримання додаткової інформації про розмір кожного знайденого файлу та короткий попередній перегляд для текстових файлів.  
Більш детально: [аргументи CLI](https://countfiles.readthedocs.io/en/latest/howtouse.html#cli-arguments).

Найбільш простим способом використання є просто ввести команду без будь-яких додаткових аргументів. Результатом цього буде таблиця, що показує частоту для кожного розширення файлу (наприклад: .txt, .py, .html, .css) та загальну кількість знайдених файлів.

```
count-files
```

Інша головна особливість цієї програми полягає у пошуку файлів з визначеним розширенням. Результат такого пошуку - список всіх знайдених шляхів до файлів.

```
count-files -fe txt [path]
```  
```
count-files --file-extension txt [path]
```

Також можна підраховувати тільки загальну кількість файлів з певним розширенням, без списку.

```
count-files -t py [path]
```  
```
count-files --total py [path]
```

Для отримання інформації про файли без розширення, використовуйте одну крапку як назву для розширення.

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

Якщо потрібно отримати список шляхів до всіх файлів або підрахувати загальну їх кількість незалежно від розширення, використовуйте дві крапки як назву для розширення.

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

## Ви знайшли помилку чи маєте пропозиції щодо вдосконалення?

Будь ласка, поставте питання в розділі Issues або відкрийте pull request у [репозиторії](https://github.com/victordomingos/Count-files).
