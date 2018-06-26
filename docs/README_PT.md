[English](https://github.com/victordomingos/Count-files/blob/master/README.md) | **[Português](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md)** | [Russian](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)
  
 
# Count Files [![Github commits (desde a última versão)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)
Um pequeno utilitário com interface de linha de comandos (CLI) escrito em 
Python para ajudar a contar ficheiros por extensão, numa determinada pasta. 
Por predefinição, a aplicação contará os ficheiros recursivamente na pasta de 
trabalho atual e em todas as suas subpastas e apresentará uma tabela mostrando 
a frequência de cada extensão de ficheiro (p.ex.: .txt, .py, .html, .css) e o 
número total de ficheiros encontrados. Quaisquer pastas ou ficheiros 
escondidos serão ignorados por defeito.

Sistemas operativos suportados: Linux, macOS, Windows. Pode ainda ser 
utilizado em iOS (iPhone/iPad) utilizando a linha de comandos [StaSh](https://github.com/ywangd/stash) 
na app Pythonista 3.


![Captura de ecrã da aplicação Count-files](https://user-images.githubusercontent.com/18650184/39443000-1bd83b62-4cab-11e8-9942-242ba29232d7.png)


## Conteúdo  
- [Descrição](#descrição)  
   - Ficheiros e pastas escondidos
   - Personalização da apresentação de resultados e feedback durante a operação
- [Exemplos de utilização](#exemplos-de-utilização)  
   - Contar quantos ficheiros há de cada extensão
   - Procurar ficheiros com uma extensão específica
   - Procurar e listar ficheiros sem extensão
   - Procurar e listar todos os ficheiros
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
nomes de ficheiros. Se preferir visualizar resultados ordenados 
alfabeticamente, basta adicionar o argumento `-alpha` or `--sort-alpha`.

De modo semelhante, as opções `-nt` ou `--no-table` instruem a aplicação para
não mostrar uma tabela com a lista de todas as extensões encontradas e 
respetivas frequências, ou seja, apresentando apenas o número total de 
ficheiros.
  
  
### Ficheiros e pastas escondidos

Por predefinição, serão ignorados ficheiros e pastas que é suposto estarem 
escondidos, mas é possível acrescentar os argumentos opcionais `-a` ou `--all` 
para incluir todos os ficheiros na contagem.

- Windows: ficheiros e pastas com em que o atributo FILE_ATTRIBUTE_HIDDEN é `True`.  
- Linux, macOS: aqueles cujos nomes começam por "." (ponto).
  
  
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

As extensões de ficheiros são tratadas com sensibilidade a maiúsculas/minúsculas. 
Por exemplo, os resultados para `ini` e `INI` serão diferentes.

Por predefinição, o resultado da pesquisa por uma determinada extensão é 
apresentado sob a forma de uma lista com os caminhos completos dos ficheiros
encontrados. Caso apenas necessite do número total de ficheiros, sem a lista, 
basta utilizar o argumento `-nl` or `--no-list`.

Durante a procura, o programa apresenta um indicador de operação, mostrando no 
ecrã, sucessivamente e numa única linha, os nomes de ficheiro processados. Os 
nomes de ficheiros não são contudo apresentados, ao buscar por uma determinada 
extensão, caso não sejam encontrados ficheiros que obedeçam aos critérios 
indicados nessa pasta, ou se os ficheiros estiverem escondidos e não tiver 
sido especificado o argumento `--all`.

Este mecanismo de feedback está ativo, de forma predefinida, ao contar 
ficheiros por extensão (com ou sem tabela) e ao procurar ficheiros por 
extensão (no modo de visualização `-nl`/`--no-list`). A opção `-nf` ou 
`--no-feedback` desativa o feedback. A utilização das opções `--no-feedback` 
e `--no-list` pode permitir obter um processamento um pouco mais rápido.
 
 
## Exemplos de utilização:

Obter ajuda sobre como usar esta aplicação:

`countfiles -h`  
`countfiles --help`


Consultar o número da versão do programa:

`countfiles -v`  
`countfiles --version`


### Contar quantos ficheiros há de cada extensão

Consultar a lista dos tipos de ficheiro atualmente suportados para a 
funcionalidade de pre-visualização:

`countfiles -st`  
`countfiles --supported-types`

Contar todos os ficheiros na pasta atual e em todas as suas subpastas, 
ignorando pastas e ficheiros escondidos:

`countfiles`


Contar todos os ficheiros na pasta atual e em todas as suas subpastas, 
incluindo pastas e ficheiros escondidos:

`countfiles -a`  
`countfiles --all`


Contar todos os ficheiros na pasta atual, ignorando pastas e ficheiros 
escondidos, mas sem percorrer as suas subpastas:

`countfiles -nr`  
`countfiles --no-recursion`


Contar todos os ficheiros numa determinada pasta e nas suas subpastas, 
ignorando pastas e ficheiros escondidos:

`countfiles ~/Documents`


Contar todos os ficheiros numa determinada pasta e nas suas subpastas, mas 
sem mostrar uma tabela, apenas o número total de ficheiros:

`countfiles -nt ~/Documents`  
`countfiles --no-table ~/Documents`


Contar todos os ficheiros numa determinada pasta, ignorando pastas e ficheiros 
escondidos, sem percorrer as subpastas, e ordenar alfabeticamente a tabela:

`countfiles -nr -alpha ~/Documents`  
`countfiles --no-recursion --sort-alpha ~/Documents`


Contar todos os ficheiros numa determinada pasta, incluindo pastas e ficheiros 
escondidos, sem percorrer as subpastas, e apresentar apenas o número total de 
ficheiros (sem tabela):

`countfiles -nr -nt -a ~/Documents`  
`countfiles --no-recursion --no-table --all ~/Documents`


Contar todos os ficheiros numa determinada pasta e nas suas subpastas, 
ignorando pastas e ficheiros escondidos, sem feedback relativo ao progresso da 
operação:

`countfiles -nf ~/Documents`  
`countfiles --no-feedback ~/Documents`



### Procurar ficheiros com uma extensão específica

Procurar recursivamente ficheiros que tenham a extensão `.txt`, numa 
determinada pasta, sem lista e sem feedback relativo ao progresso da operação:

`countfiles -nf -nl -fe txt ~/Documents`  
`countfiles --no-feedback --no-list --file-extension txt ~/Documents`


Procurar recursivamente ficheiros com a extensão `.css`, numa determinada pasta:

`countfiles -fe css ~/Documents`  
`countfiles --file-extension css ~/Documents`


Procurar recursivamente ficheiros que tenham a extensão `.py`, numa 
determinada pasta, e apresentar uma pre-visualização de 500 caracteres para 
cada um deles:

`countfiles -fe py -p -ps 500 ~/Documents`   
`countfiles --file-extension py --preview --preview-size 500 ~/Documents`


### Procurar e listar ficheiros sem extensão

Procurar recursivamente ficheiros que não têm qualquer extensão no seu nome, 
numa determinada pasta:

`countfiles -fe .  ~/Documents`  
`countfiles --file-extension . ~/Documents`


### Procurar e listar todos os ficheiros

Procurar recursivamente todos os ficheiros com ou sem extensão, numa dada 
pasta (processo semelhante à contagem de ficheiros recursiva, mas aqui o 
resultado é uma lista com os caminhos dos ficheiros encontrados):

`countfiles -fe ..  ~/Documents`  
`countfiles --file-extension .. ~/Documents`


## Instalação e dependências:

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


## Encontrou um bug ou tem uma sugestão?

Por favor avise-nos, abrindo um novo *issue* ou *pull request*.
