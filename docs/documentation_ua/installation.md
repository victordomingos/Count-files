## Встановлення та залежності

- [На десктопні операційні системи](#На-десктопні-операційні-системи)
- [На iPhone чи iPad (в Pythonista 3 для iOS)](#На-iphone-чи-ipad-в-pythonista-3-для-ios)

### На десктопні операційні системи

Count Files - це кросплатформна програма, 
яка може бути легко встановлена з допомогою 
[pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip3 install count-files
```

Якщо вас цікавить поточна версія розробки, 
ви можете клонувати цей git-репозиторій та встановити її за допомогою 
[`pip3 install -e`](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs). 
Проте зверніть увагу, що тільки випущені версії будуть стабільними та корисними. 
Поточна development версія може бути нестабільною та містити баги.

### На iPhone чи iPad (в Pythonista 3 для iOS)

Вам будуть потрібні середовище і оболонка командного рядка, сумісні з Python 3. 
Наразі це означає, що вам потрібен додаток 
[Pythonista 3](http://omz-software.com/pythonista/) 
(який є дуже гарним середовищем для розробки та/або запуску Python-програм на iOS).  
Далі потрібно встановити [StaSh](https://github.com/ywangd/stash), 
Bash-подібний додаток для Pythonista. 
Це дозволить вам використовувати такі команди, 
як `wget`, ` git clone`, `pip install` та ін. 
Він дійсно заслуговує на ярлик на головному екрані вашого iPhone або iPad.

Після виконання інструкцій по встановленню StaSh 
вам може знадобитися оновити його до останньої версії. 
Спробуйте цю команду:

```
selfupdate.py -f dev
```

Потім потрібно вийти та перезапустити Pythonista і знову запустити StaSh. 
Тепер можна спробувати встановити програму безпосередньо з git-сховища:

```
pip install count-files
```

Якщо все пройде добре, у папці `~/Documents/site-packages-3/` з'явиться новий пакет 
`count_files` та буде створено entrypoint script з іменем `count-files.py` у `stash_extensions/bin`. 
Потім знову потрібно перезапустити StaSh. 
Тепер ви можете використовувати цей додаток безпосередньо з оболонки, 
щоб підрахувати всі файли всередині вашого середовища Pythonista.

Якщо вас цікавить поточна версія розробки, 
ви можете клонувати цей git-репозиторій у додаток Pythonista використовуючи StaSh. 
Ви також можете встановити її безпосередньо за допомогою 
[pip](https://pip.pypa.io/en/stable/quickstart/):

```
pip3 install victordomingos/Count-files
```

Проте зверніть увагу, що тільки випущені версії будуть стабільними та корисними. 
Поточна development версія може бути нестабільною та містити баги.
