[English](https://github.com/victordomingos/Count-files/blob/master/README.md) | **[Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/README_PT.md)** | [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md) | [&#x423;&#x43A;&#x440;&#x430;&#x457;&#x43D;&#x441;&#x44C;&#x43A;&#x430;](https://github.com/victordomingos/Count-files/blob/master/docs/README_UA.md)
  
 
# Count Files [![Github commits (desde a última versão)](https://img.shields.io/github/commits-since/victordomingos/Count-files/latest.svg)](https://github.com/victordomingos/Count-files)
Um utilitário de linha de comandos (CLI) escrito em Python para
ajudar a contar ficheiros por extensão, numa determinada pasta. 

![Captura de ecrã da aplicação Count-files - contar ficheiros por extensão](https://user-images.githubusercontent.com/18650184/42160179-29998a52-7dee-11e8-9813-b8594e50fe77.png)


## Documentation

* [English](https://countfiles.readthedocs.io/en/latest/)
* [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/Documentation_PT.md)
* [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;](https://github.com/victordomingos/Count-files/blob/master/docs/README_RU.md)
* [&#x423;&#x43A;&#x440;&#x430;&#x457;&#x43D;&#x441;&#x44C;&#x43A;&#x430;](https://github.com/victordomingos/Count-files/blob/master/docs/README_UA.md)


## Dependências:

Para executar esta aplicação é necessária uma instalação do Python 3.6 ou superior.


## Instalação

### Em sistemas operativos de secretária

Count Files é uma aplicação multi-plataforma executada em Python e pode ser 
instalada de forma muito simples, usando o [pip](https://pip.pypa.io/en/stable/quickstart/): 

```
pip3 install count-files
```

Caso tenha interesse na atual versão de desenvolvimento, poderá clonar este 
repositório git e instalá-lo usando `pip install -e`. De realçar, contudo, que 
o código em fase de desenvolvimento é frequentemente instável e com 
*bugs*, pelo simples motivo de que é um trabalho ainda em curso.


### Em iPhone ou iPad (na app Pythonista 3 para iOS)

Também é possível utilizar esta aplicação em iOS (iPhone/iPad), usando a linha 
de comandos da [StaSh](https://github.com/ywangd/stash), na alicação 
[Pythonista 3](http://omz-software.com/pythonista/). Por favor, consulte a 
[documentação]() para mais informações. 


## Como utilizar:

Para consultar a lista de opções disponíveis e o seu modo de funcionamento, 
basta utilizar um dos seguintes comandos:

```
count-files -h
```

```
count-files --help
```

Por predefinição, a aplicação contará os ficheiros recursivamente na pasta de
trabalho atual e em todas as suas subpastas. Quaisquer pastas ou ficheiros
escondidos serão ignorados por defeito. As extensões de ficheiros são tratadas 
sem distinguir maiúsculas/minúsculas. Por exemplo, os resultados para `ini` e 
`INI` serão iguais. 

Opcionalmente, é possivel indicar um caminho para a pasta a processar, optar 
por contagem ou pesquisa não recursiva, processar as extensões de ficheiros com 
distinção de maiúsculas/minúsculas e ativar a contagem ou pesquisa em pastas
e ficheiros escondidos. Na documentação da aplicação poderá encontrar 
informação completa sobre os 
[argumentos de linha de comandos](https://github.com/victordomingos/Count-files/blob/master/docs/Documentation_PT.md#argumentos-da-linha-de-comandos).

A forma mais simples de utilização consiste na introdução de um comando
simples na linha de comandos, sem quaisquer argumentos, o que permite obter 
uma tabela com a frequência de cada extensão de ficheiro (p. ex.: .txt, .py, 
.html, .css) e o número total de ficheiros.

```
count-files
```



Uma outra funcionalidade principal da aplicação consiste na pesquisa de
ficheiros por uma dada extensão, que permite obter uma lista dos caminhos 
completos para todos os ficheiros encontrados.

```
count-files -fe txt [caminho]
````

```
count-files --file-extension txt [caminho]
```

Também é possível contar o número total de ficheiros com uma certa extensão, 
sem os listar.


```
count-files -t py [caminho]
```


```
count-files --total py [caminho]
```

Para obter informação sobre ficheiros que não têm extensão no seu nome, basta 
indicar um ponto no lugar da extensão:
 
```
count-files -fe . [caminho]
```
```
count-files --file-extension . [caminho]
```
```
count-files -t . [caminho]
```
```
count-files --total . [caminho]
```

Caso necessite de listar ou contar todos os ficheiros, independentemente da 
sua extensão, especifique dois pontos no lugar da extensão:

```
count-files -fe .. [caminho]
```
```
count-files --file-extension .. [caminho]
```
```
count-files -t .. [caminho]
```
```
count-files --total .. [caminho]
```

Procure por arquivos, usando wildcards: `*`, `?`, `[seq]`, `[!seq]`.

```
count-files -fm *.py? [caminho]
```
```
count-files --filename-match *.py? [caminho]
```
   
## Encontrou um *bug* ou tem uma sugestão?

Por favor avise-nos, abrindo um novo *issue* ou *pull request*.
