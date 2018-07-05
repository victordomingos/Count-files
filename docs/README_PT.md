[English](https://github.com/victordomingos/Count-files/blob/master/README.md) | **[Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md)** | [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439; &#x44F;&#x437;&#x44B;&#x43A;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)
  
 
# Count Files [![Github commits (desde a última versão)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)
Um pequeno utilitário de linha de comandos (CLI) escrito em Python para
ajudar a contar ficheiros por extensão, numa determinada pasta. 
Por predefinição, a aplicação contará os ficheiros recursivamente na pasta de 
trabalho atual e em todas as suas subpastas e apresentará uma tabela mostrando 
a frequência de cada extensão de ficheiro (p.ex.: .txt, .py, .html, .css) e o 
número total de ficheiros encontrados.

Sistemas operativos suportados: Linux, macOS, Windows. Pode ainda ser
utilizado em iOS (iPhone/iPad) utilizando a linha de comandos [StaSh](https://github.com/ywangd/stash)
na app Pythonista 3.


![Captura de ecrã da aplicação Count-files](https://user-images.githubusercontent.com/18650184/39443000-1bd83b62-4cab-11e8-9942-242ba29232d7.png)

## Conteúdo  
- **[Instalação e dependências](#instalação-e-dependências)**
   - [Em sistemas operativos de secretária](#em-sistemas-operativos-de-secretária)
   - [Em iPhone ou iPad (na app Pythonista 3 para iOS)](#em-iphone-ou-ipad-na-app-pythonista-3-para-ios)
  
- **[Como utilizar](#como-utilizar)**
   - [Argumentos da linha de comandos](#argumentos-da-linha-de-comandos)
   - [Obter ajuda sobre como usar esta aplicação](#obter-ajuda-sobre-como-usar-esta-aplicação)
   - [Pastas e ficheiros escondidos](#pastas-e-ficheiros-escondidos)
   - [Sensibilidade a maiúsculas/minúsculas](#sensibilidade-a-maiúsculas-minúsculas)
   - [Personalização da apresentação de resultados e feedback durante a operação](#personalização-da-apresentação-de-resultados-e-feedback-durante-a-operação)
   - [Exemplos práticos de utilização](#exemplos-práticos-de-utilização)
      - [Contar o número total de ficheiros numa pasta](#contar-o-número-total-de-ficheiros-numa-pasta)  
      - [Contar quantos ficheiros há de cada extensão](#contar-quantos-ficheiros-há-de-cada-extensão)
      - [Procurar ficheiros com uma extensão específica](#procurar-ficheiros-com-uma-extensão-específica)
      - [Procurar e listar ficheiros sem extensão](#procurar-e-listar-ficheiros-sem-extensão)
      - [Procurar e listar todos os ficheiros](#procurar-e-listar-todos-os-ficheiros)
      - [Outras funcionalidades](#outras-funcionalidades)
  
- **[Encontrou um bug ou tem uma sugestão?](#encontrou-um-bug-ou-tem-uma-sugestão)**



## Instalação e dependências:

### Em sistemas operativos de secretária

A atual versão de desenvolvimento pode ser instalada com o comando
`pip install -e`, seguido do caminho para a pasta principal do projeto (a
mesma pasta que contém o ficheiro `setup.py`). Para executar esta aplicação é
necessária uma instalação do Python 3.6 ou superior. Procuramos manter no
mínimo as dependências externas, de modo a manter a compatibilidade com
diferentes plataformas, incluindo Pythonista em iOS. Neste momento, requer:

- puremagic==1.4

Planeamos submeter esta aplicação ao PyPI tão brevemente quanto possível, para
permitir oferecer uma forma de instalação e atualização mais simples.
Enquanto isso não acontece, estejam à vontade para dar uma olhada na próxima
secção e talvez considerar contribuir também para este projeto.


### Em iPhone ou iPad (na app Pythonista 3 para iOS)

Primeiro, irá precisar de um ambiente Python e uma consola de linha de comandos
compatível com Python 3. No momento presente, isto significa que precisa de ter
instalada uma app chamada [Pythonista 3](http://omz-software.com/pythonista/)
(que é, entre outras coisas, um excelente ambiente para desenvolvimento e
execução de aplicações de Python puro em iOS). 

Depois, precisará de instalar a
[StaSh](https://github.com/ywangd/stash), que é uma consola de linha de
comandos baseada em Python, concebida especificamente para correr no
Pythonista. Irá permitir executar comandos bem úteis como `wget`, `git clone`,
`pip install` e muitos outros. Merece realmente um atalho no ecrã principal do
seu iPhone ou iPad. 

Depois de seguir as instruções para a instalação da StaSh,
poderá precisar de a atualizar para uma versão mais recente. Experimente este
comando:

```
selfupdate.py -f bennr01:command_testing
```

De seguida, force o encerramento do Pythonista, reiniciando-o de seguida, e
inicie novamente a StaSh. Deverá estar agora a correr em Python 3. Neste
momento, pode tentar instalar esta aplicação, diretamente a partir deste
repositório:

```
pip install victordomingos/Count-files
```

Se tudo correr bem, o comando acima deverá instalar quais quer dependências,
colocar um pacote chamado `count_files` dentro da pasta
`~/Documents/site-packages-3` e criar um *script* de execução chamado
`count-files.py` em `stash_extensions/bin`. Poderá precisar de descarregar
manualmente (recorda-se daquele comando `wget`?) um ficheiro chamado
`magic_data.json` do repositório [`puremagic`](https://github.com/cdgriffith/puremagic)
(por algum motivo, neste momento não está a instalar corretamente usando a
StaSh) e movê-lo para `~/Documents/site-packages-3/puremagic/`. De seguida,
force o encerramento do Pythonista, reinicie a app e inicie novamente a StaSh.
Já deverá conseguir executar esta aplicação diretamente a partir da consola
para contar quaisquer ficheiros que possa ter no ambiente do Pythonista.


## Como utilizar:

### Argumentos da linha de comandos

De um modo geral, podem ser indicados argumentos tanto na forma
abreviada como na forma extensa. Por exemplo: `-a` ou `--all`.

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

A forma mais simples de utilização consiste na introdução de um comando
simples na linha de comandos, sem quaisquer argumentos. Assim, para contar
todos os ficheiros na pasta atual e em todas as suas subpastas, ignorando
pastas e ficheiros escondidos:

```
count-files
```

Por predefinição, a aplicação contará os ficheiros recursivamente na pasta de
trabalho atual e em todas as suas subpastas e apresentará no final uma tabela
mostrando a frequência de cada extensão de ficheiro (p.ex.: .txt, .py, .html,
.css) e o número total de ficheiros encontrados. Quaisquer pastas ou ficheiros
escondidos serão ignorados por defeito.

Uma outra funcionalidade principal da aplicação consiste na pesquisa de
ficheiros pela sua extensão, que permite obter uma lista de todos os ficheiros
encontrados ou, opcionalmente, apenas o numero de ficheiros.

```
count-files -fe txt
````

```
count-files --file-extension txt
```

Opcionalmente, é possivel indicar um caminho para a pasta a processar. Se
preferir, poderá deixar esse argumento vazio, e a aplicação irá contar os
ficheiros da pasta atual. Para processar os ficheiros na sua pasta de 
utilizador, poderá indicar o caminho ```~```. No caso de haver espaços nos 
nomes de pastas ou ficheiros, o caminho deve ser especificado `"entre aspas"`. 

Exemplo para Windows:

```
count-files "~\Ambiente de Trabalho\Nova pasta"
```

Os argumentos optionais `-nr` ou `--no-recursion` dizem à aplicação para não
percorrer de forma recursiva todas as subpastas (ou seja, pesquisar apenas na
raiz da pasta indicada).


### Obter ajuda sobre como usar esta aplicação:

Para consultar a lista de opções disponíveis e o seu modo de funcionamento, 
basta utilizar um dos seguintes comando:

```
count-files -h
```

```
count-files --help
```

  
### Pastas e ficheiros escondidos

Por predefinição, serão ignorados ficheiros e pastas que é suposto estarem 
escondidos, mas é possível acrescentar os argumentos opcionais `-a` ou `--all` 
para incluir todos os ficheiros na contagem.

- Windows: ficheiros e pastas com em que o atributo FILE_ATTRIBUTE_HIDDEN é `True`.  
- Linux, macOS: aqueles cujos nomes começam por "." (ponto).
  

### Sensibilidade a maiúsculas/minúsculas

As extensões de ficheiros são tratadas sem distinguir maiúsculas/minúsculas.
Por exemplo, os resultados para `ini` e `INI` serão iguais. Para distinguir
maiúsculas/minúsculas, use a opção `-c` ou `--case-sensitive`.


### Personalização da apresentação de resultados e feedback durante a operação

Este utilitário pode ainda ser utilizado para procurar ficheiros que tenham no 
seu nome uma determinada extensão (utilizando `-fe` ou `--file-extension`) e, 
opcionalmente, apresentar uma pre-visualização breve (`-p`ou `--preview`) para 
ficheiros de texto. O tamanho do texto de pre-visualização pode ser, de forma 
opcional, personalizado através do argumento `-ps` ou `--preview-size` seguido 
de um número inteiro indicando o número de caracteres.

A lista de tipos de ficheiro para os quais está disponível a funcionalidade de 
pre-visualização pode ser consultada com o argumento `-st` ou 
`--supported-types`.

Por predefinição, o resultado da pesquisa por uma determinada extensão é 
apresentado sob a forma de uma lista com os caminhos completos dos ficheiros
encontrados. Se necessitar de informação sobre o tamanho de cada ficheiro, 
utilize o argumento `-fs` ou `--file-sizes`. Se pretender contar o número 
total de ficheiros com uma determinada extensão, sem extensão ou 
independentemente da extensão, utilize o argumento `-t` ou `--total`.
 
Durante a procura, o programa apresenta um indicador de operação, mostrando no 
ecrã, sucessivamente e numa única linha, os nomes de ficheiro processados. Os 
nomes de ficheiros não são contudo apresentados, ao buscar por uma determinada 
extensão, caso não sejam encontrados ficheiros que obedeçam aos critérios 
indicados nessa pasta, ou se os ficheiros estiverem escondidos e não tiver 
sido especificado o argumento `--all`.

Este mecanismo de feedback está ativo, de forma predefinida, ao contar 
ficheiros por extensão (com tabela) e ao contar o número total de ficheiros. 
A opção `-nf` ou `--no-feedback` desativa o feedback. A utilização da opção 
`--no-feedback` pode permitir obter um processamento um pouco mais rápido.
 
Ao procurar ficheiros por extensão (usando `-fe` ou `--file-extension`), 
o mecanismo de feedback apresentado é a própria lista de ficheiros.


### Exemplos práticos de utilização:

#### Contar o número total de ficheiros numa pasta

Argumentos na forma abreviada:
```
usage: count-files [-a] [-c] [-nr] [-nf] [-t TOTAL] [path]
```

Argumentos na forma extensa:
```
usage: count-files [--all] [--case-sensitive] [--no-recursion] [--no-feedback] [--total TOTAL] [path]
```

Para contar o número total de ficheiros, deverá especificar a extensão de 
ficheiro ou utilizar um ponto ```.``` para obter uma contagem dos ficheiros 
que não têm extensão. Também poderá utilizar dois pontos sem espaços ```..``` 
para obter uma contagem do número total de ficheiros com ou sem extensão.


Contar de forma recursiva o número total de ficheiros com uma extensão 
específica na pasta atual, incluindo subpastas e ficheiros escondidos:

```
count-files -a -t txt
```

```
count-files --all --total txt
```

Contar de forma recursiva o número total de ficheiros com uma extensão 
específica em maiúsculas:

```
count-files -t JPG -c
```

```
count-files --total JPG --case-sensitive
```

Contar de forma recursiva o número total de ficheiros na pasta atual que não 
têm extensão:

```
count-files -t .
```

```
count-files --total .
```

Contar o número total de ficheiros na pasta atual, independentemente de terem 
ou não uma extensão:

```
count-files -nr -t ..
```

```
count-files --no-recursion --total ..
```


#### Contar quantos ficheiros há de cada extensão

Argumentos na forma abreviada:
```
usage: count-files [-a] [-alpha] [-c] [-nr] [-nf] [path]
```

Argumentos na forma extensa:
```
usage: count-files [--all] [--sort-alpha] [--case-sensitive] [--no-recursion] [--no-feedback] [path]
```

Por predefinição, a tabela será ordenada pela frequência das extensões dos
nomes de ficheiros. Se preferir visualizar resultados ordenados
alfabeticamente, basta adicionar o argumento `-alpha` or `--sort-alpha`.

Contar todos os ficheiros na pasta atual e em todas as suas subpastas, 
ignorando pastas e ficheiros escondidos, sem distinção de 
maiúsculas/minúsculas:

```
count-files
```

Contar todos os ficheiros na pasta atual e em todas as suas subpastas, 
ignorando pastas e ficheiros escondidos, com distinção de 
maiúsculas/minúsculas:

```
count-files -c
```

```
count-files --case-sensitive
```

Contar todos os ficheiros na pasta atual e em todas as suas subpastas, 
incluindo pastas e ficheiros escondidos:

```
count-files -a
```
  
```
count-files --all
```


Contar todos os ficheiros na pasta atual, ignorando pastas e ficheiros 
escondidos, mas sem percorrer as suas subpastas:

```
count-files -nr
```
  
```
count-files --no-recursion
```


Contar todos os ficheiros numa determinada pasta e nas suas subpastas, 
ignorando pastas e ficheiros escondidos:

```
count-files ~/Documents
```



Contar todos os ficheiros numa determinada pasta, ignorando pastas e ficheiros 
escondidos, sem percorrer as subpastas, e ordenar alfabeticamente a tabela:

```
count-files -nr -alpha ~/Documents
```  

```
count-files --no-recursion --sort-alpha ~/Documents
```


Contar todos os ficheiros numa determinada pasta e nas suas subpastas, 
ignorando pastas e ficheiros escondidos, sem feedback relativo ao progresso da 
operação:

```
count-files -nf ~/Documents
```  

```
count-files --no-feedback ~/Documents
```


#### Procurar ficheiros com uma extensão específica

Argumentos na forma abreviada:
```
usage: count-files [-a] [-c] [-nr]
                   [-fe FILE_EXTENSION] [-fs]
                   [-p] [-ps PREVIEW_SIZE] [path]
```

Argumentos na forma extensa:
```
usage: count-files [--all] [--case-sensitive] [--no-recursion]
                   [--file-extension FILE_EXTENSION] [--file-sizes]
                   [--preview] [--preview-size PREVIEW_SIZE] [path]
```

Procurar recursivamente ficheiros que tenham a extensão `.txt`, numa 
determinada pasta, incluindo pastas e ficheiros escondidos:

```
count-files -a -fe txt ~/Documents
```

```
count-files --all --file-extension txt ~/Documents
```


Procurar recursivamente ficheiros com a extensão `.css`, numa determinada pasta, 
incluindo informação sobre o tamanho dos ficheiros:

```
count-files -fe css -fs ~/Documents
```  

```
count-files --file-extension css --file-sizes ~/Documents
```


Procurar recursivamente ficheiros que tenham a extensão `.py`, numa 
determinada pasta, e apresentar uma pre-visualização de 500 caracteres para 
cada um deles:

```
count-files -fe py -p -ps 500 ~/Documents
```   

```
count-files --file-extension py --preview --preview-size 500 ~/Documents
```


#### Procurar e listar ficheiros sem extensão

Utilize um único ponto ```.``` para procurar ficheiros que não tenham extensão. 
Por exemplo, ficheiros com nomes como `.gitignore`, `Procfile`, `_netrc`.

Procurar recursivamente ficheiros que não têm qualquer extensão no seu nome, 
numa determinada pasta:

```
count-files -fe .  ~/Documents
```  

```
count-files --file-extension . ~/Documents
```


#### Procurar e listar todos os ficheiros

Utilize dois pontos ```..``` sem espaço entre eles para procurar todos os 
ficheiros, independentemente de terem ou não extensão.

Procurar recursivamente todos os ficheiros com ou sem extensão, numa dada 
pasta (processo semelhante à contagem de ficheiros recursiva, mas aqui o 
resultado é uma lista com os caminhos dos ficheiros encontrados):

```
count-files -fe ..  ~/Documents
```
  
```
count-files --file-extension .. ~/Documents
```


#### Outras funcionalidades

Consultar o número da versão do programa:

```
count-files -v
```

```
count-files --version
```

Consultar a lista dos tipos de ficheiro atualmente suportados para a
funcionalidade de pre-visualização:

```
count-files -st
```

```
count-files --supported-types
```

   
## Encontrou um bug ou tem uma sugestão?

Por favor avise-nos, abrindo um novo *issue* ou *pull request*.
