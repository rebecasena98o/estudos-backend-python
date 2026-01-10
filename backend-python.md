

**Negrito**
*Itálico*
~~Riscado~~

# Bootcamp Back-End Python - DIO

## 📌 Módulo 1 – Fundamentos de Python

### 🔹 Variáveis
- *Usadas para armazenar valores*
- *Tipagem dinâmica*
- *Consomem 24 bytes de armazenamento na memória*
- *Não permanecem com o mesmo valor durante a execução do código*
- *No Python, não é necessário definir o tipo de dado da variável, pois ele já faz isso automaticamente (por isso não podemos simplesmente criar uma variável sem atribuir um valor)*

```python
age = 19
name = 'Rebeca'

print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')

age, name = (4, 'Pato')
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade')
```
### 🔹Constantes
- *Armazena valores*
- *Nasce com um valor e permanece com ele até o final da execução do programa*
- *imutável*
- *Não existe uma palavra reservada em Python para informar ao interpretador que o valor é constante (usa-se a convenção, que diz ao porgramador se a variável é uma constante - letras maíusculas)*

```python
ALTURA = 1.69
```

---

### 🔹"built-in types"
- *Tipos integrados*
- *vêm predefinidos em uma linguagem de programação*
- *Representação e manipulação de dados/informações no código*

##### 🔸 Exemplos:

```python
idade = 20 (int)
nome = "Rebeca" (str)
peso = 58.3 (float)
pato = true (bool)
list_1 = ["New York", "Brasil", "Alemanha", "Grécia"] (list, range, tuple)
this_city = {
    'city' : 'Berlin',
    'country' : 'Germany',
    'population' : 3645000
} (dict)
```

---
### 🔹 Operadores Aritméticos
- *Executam operações matemáticas, como adição, subtração com operandos, multiplicação, etc.*

```python
# Adição
print(1 + 1)
>>> 2

# Subtração
print(10 - 2)
>>> 8

# Multiplicação
print(4 * 3)
>>> 12

# Divisão
print( 12 / 3)
>>> 4.0

# Divisão inteira
print(12 // 2)
>>> 6

# Módulo
print( 10 % 3)
>>> 1

# Exponenciação
print(2 ** 3)
>>> 8
```
---
### 🔹 Precedência de operadores
- *Operações que devem ser executadas primeiro - regra matemática*
- *A ordem altera o valor final*
(ex: x = 10 - 5 *2)
- *Definições da ordem:*
> Parêntesis

> Expoentes

> Multiplicações e divisões (da esquerda para a direita)

> Somas e subtrações (da esquerda para a direita)

```python
print(10 - 5 * 2)
>>> 0

print((10 5) * 2)
>>> 10

print(10 ** 2 * 2)
>>> 200

print(10 **(2 * 2))
>>> 10000

print(10 / 2 * 4)
>>> 20.0
```
---
### 🔹 Operadores de comparação
- *Comparar dois valores (A e B)*

```python
saldo = 450
saque = 200

print(saldo == saque)
>>> False

print(saldo != saque)
>>> True

print(saldo > saque)
>>> True

print(saldo >= saque)
>>> True

print(saldo < saque)
>>> False

print(saldo <= saque)
>>> False
```
---
### 🔹 Operadores de atribuição

- *Utilizados para definir o valor inicial ou sobrescrever o valor de uma variável*

```python
saldo = 500

print(saldo)
>>> 500

#Atribuição com soma
saldo = 500
saldo += 200

print(saldo)
>>> 700

#Atribuição com divisão
saldo = 500
saldo /= 5

print(saldo)
>>> 100.0

saldo = 500
saldo //= 5

print(saldo)
>>> 100

#Atribuição com módulo
saldo = 500
saldo %= 480

print(saldo)
>>> 20

#Atribuição com exponenciação

saldo = 80
saldo **= 2

print(saldo)
>>> 6400
```
---
### 🔹 Operadores lógicos
- *Utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica*
- *Quando um operador de comparação é utilizado, o resultado retornado é um booleano*

```python
saldo = 1000
saque = 200
limite = 100

saldo >= saque
>>> True

saque <= limite
>>> False

#Operador E

saldo >= saque and saque <= limite
>>> False

#Operador OU

saldo >= saque or saque <= limite
>>> True

#Operador Negação
contatos_emergencia = []

not 1000 > 1500 #false
>>> True 
# um falso - True (inverso da verdade) no not

not contatos_emergencia
>>> True #inverso da verdade - lista vazia em pyhton é falso

not "saque 1500;"
>>> False #string com valor - verdadeira - tem valor

not ""
>>> True #String vazia - Falso - inverso

#Parênteses

saldo = 1000
saque = 350
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
>>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque )
>>> True
```
---
### 🔹 Operadores de identidade
- *Operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória*

```python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

#Operador is // obj A is obj B
curso is nome_curso
>>> True

#ambos utilizam a mesma região de memória
curso is not nome_curso
>>> False

saldo is limite
>>> True
```
---
### 🔹 Operadores de associação
- *Utilizados para verificar se um objeto está presente em uma sequência*

```python
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
>>> True

"maça" not in Frutas
>>> True

200 in saques
>>> False
```
---
### 🔹 Indentação e blocos
- *Identar código é uma forma de manter o código fonte mais legível e manutenível (passível de ser mantido). Mas em Python ela exerce um segundo papel, através da ondentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina*
- *As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. (chaves - Java e C)*
- *Existe uma convenção em Python que define um novo bloco: a cada novo bloco adicionamos 4 novos espaços em branco por nível de identação*

```python
def sacar (self, valor: float) -> None: #início do bloco do método

    if self.saldo >= valor: # início do bloco do if
        self.saldo -= valor

    #fim do bloco do if
#fim do bloco do método
```
---

### 🔹 Estruturas Condicionais
- *Permitem o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas*

#### 🔸 if
- *Único desvio*
- *O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas*

```python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")    
```

#### 🔸 if/else
- *Dois desvios*
- *Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código do else será executado*

```python
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")    
```

#### 🔸if/elif/else
- *Mais de dois desvios*
- *O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado*
- *sem limite de elif - evite criar muitos - aumento de complexidade do código*

```python
opcao = int(input("Informe uma opção: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")    

else:
    print("Opção inválida!")    
```

#### 🔸if aninhado

- *Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else*

```python
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
    print("Saque realizado com uso do cheque especial!")    
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
    print("Saldo insuficiente!")    
```

#### 🔸if ternário
- *Permite escrever uma condição em uma única linha*
- *Composto por três partes:*
> retorno caso a expressão retorne verdadeiro

> expressão lógica

> retorno caso a expressão não seja atendida

```python
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
```
---
### 🔹 Estruturas de repetição
- *Estruturas utilizadas para repetir um trecho de código em um determinado número de vezes*
- *Esse número pode ser conhecido previamente ou determinado atráves de uma expressão lógica*

```python
a = int(input("Informe um número inteiro: "))

print(a)

repita 2 vezes:
    a += 1
    print(a)
```
#### 🔸for
- *Usado para percorrer um objeto iterável*
- *Faz sentido usá-lo quando sabemos o número exato de vezes que nosso bloco de código deve ser executado ou queremos percorrer um objeto iterável*

```python
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #Adiciona quebra de linha        
```
#### 🔸função range
- *É uma função built-in do Python, usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo)*
- *Se usarmos range(i,j) será produzido:*
> i, i + 1, i + 2, i + 3, ..., j - 1
- *Ela recebe 3 argumentos: stop(obrigatório), start(opcional) e step (opcional)*

```python
#range(stop) -> range object
# range(start, stop[, step]) -> range object

list(range(4))
>>> [0, 1, 2, 3]   
```
##### 🔸 Range com for

```python
for numero in range(0, 11):
    print(numero, end=" ")

>>> 0 1 2 3 4 5 6 7 8 9 10

# exibindo a tabuada do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")

>>> 0 5 10 15 20 25 30 35 40 45 50    
```

#### 🔸While
- *É usado para repetir um bloco de código várias vezes*
- *quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado*

```python
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

```
---

## 📌 Módulo 2 – Funções

### 🔹 Funções simples
```python
def saudacao(nome):
    return f"Olá, {nome}"
```
---
### 🔹 Funções de entrada e saída
##### 🔸 input
- *A função builtin input é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.*
```python
nome = input("informe o seu nome: ")
>>> informe o seu nome:
```

##### 🔸 Print
- *A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos (significa que ele pode receber qualquer número de referências de objetos - do zero a muitos argumentos) e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.*

```python
nome = "Rebeca"
sobrenome = "Sena"
print(nome, sobrenome)

print(nome, sobrenome, end="...\n")

//parâmetros para a função - termina em três pontos e há quebra de linha

print(nome, sobrenome, sep="#")
//separador - padrão - espaço vazio - jogo da velha


>>> Rebeca Sena
>>> Rebeca Sena...
>>>Rebeca#Sena
```
---
### 🔹 Outras funções 
##### 🔸 Dir
- *Sem argumentos, retorna a lista de nomes no escopo local  atual.* 
- *Com um argumento, retorna uma lista de atributos válidos para o objeto.*

```python
dir()
dir(100)
```

##### 🔸 Help
- *Invoca o sistema de ajuda integrado.* 
- *É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável.*

```python
help()
help(100)
```
---
## 📌 Módulo 3 – Convertendo tipos
- *É necessário converter o tipo de uma variável para manipula-la de forma diferente*

```python
//inteiro para float
preco = 100
print (preco)
>>> 10

preco = float(preco)
print (preco)
>>> 10.0

preco = 10/2
print(preco)
>>> 5.0

//float para inteiro

preco = 10.30
print (preco)
>>> 10.3

preco = int(preco)
print (preco)
>>> 10
```

### 🔹 Conversão por divisão
```python
preco = 10
print (preco)
>>> 10

print (preco / 2)
>>> 5.0

print (preco // 2)
>>> 5
```

### 🔹 Númerico para String
```python
preco = 10.50
idade = 28

print(str(preco))
>>> 10.5

print(str(idade))
>>> 28

texto = f"idade {idade} preco {preco}"
print(texto)
>>> idade 28 preco 10.5
```

### 🔹 Inverso
```python
preco = "10.50"
idade = "28"

print(float(preco))
>>> 10.50

print(int(idade))
>>> 28
```
---
## 📌 Módulo 4 – Manipulando Strings
> *Métodos úteis para manipular objetos do tipo string, como interpolar valores de variáveis e entender como funciona o fatiamento*
### 🔹Maiúscula, minúscula e título

```python
curso = "pYtHoN"

print(curso.upper())
>>> PYTHON

print(curso.lower())
>>> python

print(curso.title())
>>> Python
```
### 🔹 Eliminando espaços em branco

```python
curso = "     Python"

print(curso.strip())
>>> "Python" #esquerda e direita

print(curso.lstrip())
>>> "Python " #esquerda

print(curso.rstrip())
>>> " Python" #direita
```

### 🔹 Junções e centralização

```python
curso = "Python"

print(curso.center(10, "#"))
>>> "##Python##" #2 no começo, 2 no fim, centralização

print(".".join(curso))
>>> "P.y.t.h.o.n" #letra a letra
```

### 🔹 Interpolação de variáveis
- *Há três formas de interpolar variáveis em strings, a primeira é usando o sinal %, a segunda é utilizando o método format e a última é utilizando f strings* 


##### 🔸Old style %

- *Não recomendada e seu uso em Python 3 é raro*

```python
nome = "Rebeca"
idade = 25
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s. " % (nome, idade, profissao, linguagem))

>>> Olá, me chamo Rebeca. Eu tenho 25 anos de idade, trabalho com Programadora e estou matriculado no curso de Python
```

##### 🔸Método format

```python
nome = "Rebeca"
idade = 25
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}. " format (nome, idade, profissao, linguagem))

>>> Olá, me chamo Rebeca. Eu tenho 25 anos de idade, trabalho com Programadora e estou matriculado no curso de Python
```
##### 🔸f-string

```python
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
>>> "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}")
>>> "Valor de PI:         3.14"
```
### 🔹 Fatiamento de String
- *É uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[,step]]*

```python
nome = "Izuku Midoryia de lima "
nome[0]
>>> "I"

nome[:5]
>>> "Guilherme"

nome[13:]
>>> "Izuku Midoryia"

nome[10:16]
>>> "Midoryia"

nome[10:16:2]

nome[:]
>>> "Izuku Midoryia de lima "

nome[::-1]
>>> "Cópia invertida"
```

### 🔹 String Múltiplas linhas
- *São definidas informando 3 aspas simples ou duplas durante a atribuição.*
- *Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.*

```python
nome = "Ochaco Uraraka"

mensagem = f"""
Olá, meu nome é {nome},
Eu estou aprendendo Python
"""
>>>
Olá, meu nome é Ochaco Uraraka,
Eu estou aprendendo Python
```
---
## 📌 Módulo 5 – Trabalhando com Listas
> *Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor **list**, a função range ou colocando valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.*

##### 🔸 Exemplo

```python
frutas = ["laranja", "maçã", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
```

### 🔹 Acesso direto
- *A lista é uma sequência, portanto, podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero*

##### 🔸Índices negativos
- *Sequências suportam indexação negativa. Acontagem começa em -1*

##### 🔸Listas aninhadas
- *Listas podem armazenas todos os tipos de objetos Python, portanto, podemos ter listas que armazenam outras listas. Com isso, podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna*

##### 🔸Fatiamento
- *Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso, basta passar o índice inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso*

##### 🔸 Exemplos

```python
frutas = ["Maçã", "Laranja", "Uva", "Pera"]

frutas[0] #Maçã
frutas[2] #Uva

### ìndices negativos

colecaoYugioh = ["Monster Reborn", "Infinite Impermanence" , "Linkuriboh", "Droll & Lock Bird", "Solemn Warning" ]

colecaoYugioh[-1] #Solemn Warning
colecaoYugioh[-3] #Linkuriboh

### Listas aninhadas

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] # "c"

### Fatiamento

lista = ["p", "i", "p", "o", "c", "a"]

lista[2:] # ["p", "o", "c", "a"]
lista[:2] # ["p", "i"]
lista[1:3] # ["i", "p"]
lista[0:3:2] # ["p", "p"]
lista[::] # ["p", "i", "p", "o", "c", "a"]
lista[::-1] # ["a", "c", "o", "p", "i", "p"]
```

### 🔹Iterar listas
- *A forma mais comum para percorrer os dados de uma lista é utilizando o comando **for***

```python
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
```

### 🔹Função enumerate
- *Ás vezes é necessário saber qual o índice do objeto dentro do laço **for**. Para isso podemos usar esta função*

```python
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
```

### 🔹Compressão de listas
- *A compressão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente*

```python
### Filtro versão 1

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

### Filtro versão 2

numeros = [1, 30, 21, 2, 9, 65, 25]
pares = [numero for numero in numeros if numero % 2 == 0]      

### Modificando valores version 1

numeros = [1, 30, 21, 2, 9, 65, 25]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

### Modificando valores version 2

numeros = [1, 30, 21, 2, 9, 65, 25]
quadrado = [numero ** 2 for numero in numeros]    
```

### 🔹 Métodos da classe list
##### 🔸 Exemplos

```python
### [] append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) #[1, "Python", [40, 30, 20]]

### [].clear
lista = [1, "Python", [40, 30, 20]]

print(lista) #[1, "Python", [40, 30, 20]]

lista.clear()

print(lista) # []

### [].copy
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista) # [1, "Python", [40, 30, 20]]

### [].count

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1

cores.count("azul") # 2

cores.count("verde") # 1

### [].extend

linguagens = ["python", "js", "Java"]

print(linguagens) # ["python", "js", "Java"]

linguagens.extend(["HTML", "CSS"])

print(linguagens) # ["python", "js", "Java", "HTML", "CSS"]

### [].index

linguagens = ["python", "js", "c", "Java", "csharp"]

linguagens.index("Java") # 3
linguagens("python") # 0

### [].pop - estrutura de dados
linguagens = ["python", "js", "c", "Java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # Java
linguagens.pop() # c
linguagens.pop(0) # python

### [].remove
linguagens = ["python", "js", "c", "Java", "csharp"]

linguagens.remove("c")

print(linguagens) # linguagens = ["python", "js", "Java", "csharp"]

### [].reverse
linguagens = ["python", "js", "c", "Java", "csharp"]

linguagens.reverse()

print(linguagens) # ["csharp", "Java", "c", "js", "python" ]

### [].sort
linguagens = ["python", "js", "c", "Java", "csharp"]
linguagens.sort() # ["c", "csharp", "Java", "js", "python"]

linguagens = ["python", "js", "c", "Java", "csharp"]
linguagens.sort(reverse=True) 
# ["python", "js", "Java", "csharp", "c"] 

linguagens = ["python", "js", "c", "Java", "csharp"]
linguagens.sort(key=lambda x: len(x))
# ["c", "js", "Java", "python", "csharp"] 

linguagens = ["python", "js", "c", "Java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
# ["python", "csharp", "Java", "js", "c"] 

### len

doces = ["pirulito", "sorvete", "chocolate", "surpresa de uva", "pizza"]

len(doces) # 5

### sorted
linguagens = ["python", "js", "c", "Java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) #["c", "js", "Java", "python", "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True) #["python", "csharp", "Java", "js", "c"]

```
---
## 📌 Módulo 6 – Conhecendo tuplas
> São estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis, enquanto listas são mutáveis. Podemos criar tuplas através da classe **tuple**, ou colocando valores separados por vírgula de parenteses.

##### 🔸 Exemplos

```python
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)
```

### 🔹 Índices negativos
- *Sequências suportam indexação negativa. A contagem começa em -1*

##### 🔸 Exemplos
```python
frutas = ("laranja", "pera", "uva",)

frutas[-1] #uva
frutas[-2] #pera
```

### 🔹 Tuplas aninhadas
- *Tuplas podem armazenar todos os tipos de objetos Python, portanto, podemos ter tuplas que armazenam outras tuplas. Com isso, podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna*

##### 🔸 Exemplos

```python
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] # "c"
```

### 🔹 Acesso direto
- *A tupla é uma sequência, portanto, podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequÊncia a partir do zero*

##### 🔸 Exemplos
```python
frutas = ("laranja", "pera", "uva",)

frutas[0] #laranja
frutas[2] #uva
```
---
## 📌 Módulo 5 – Dicionários: Criação e acesso aos dados
> É um conjunto não-ordenado de pares chave: valor, onde as chaves são únicas em uma dada instância do dicionário. Eles são delimitados por chaves: {}, e contém uma lista de pares chave: valor separada por vírgulas.

##### 🔸 Exemplos
```python
pokedex = {"name" : "Pikachu", "tipo" : "Elétrico" }

pokedex = dict(name="Pikachu", tipo="Elétrico")

pokedex["telefone"] = "3333-1234"
# {name : "Pikachu", "tipo" : "Elétrico", "telefone" : "3333-1234"}
```

### 🔹 Acesso

##### 🔸 Exemplos

```python
fichaRPG = {"nome" : "Lina", "raça" : "paladino", "idade" : 25}

fichaRPG["nome"] # Lina
fichaRPG["raça"] # paladino
fichaRPG["idade"] # 25

fichaRPG["nome"] = "Alexa"
fichaRPG["raça"] = "bardo"
fichaRPG["idade"] = 35
fichaRPG["arma"] = "adaga"

print(fichaRPG) # {"nome" : "Alexa", "raça" : "bardo", "idade" : 35, "arma" : "adaga"}
```

### 🔹 Dicionários aninhados
- *Podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como: strings e números*


##### 🔸 Exemplos

```python
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}
contatos["giovanna@gmail.com"] ["telefone"]
# "3443-2121"
```

### 🔹 Iterar dicionários
- *A forma mais comum para percorrer os dados de um dicionários é utilizando o comando **for***

##### 🔸 Exemplos

```python
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)    
```
---

### 🔍 Curiosidades
- *Booleano: implementado pela classe bool. Em Python, o tipo booleano é uma subclasse de int, uma vez que qualquer número diferente de 0 representa verdadeiro e 0 representa falso.*
- *extend une*

---
### 🔹 Modo Interativo
- *O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código e ver o resultado na hora - escrever e ver antes de códigos que o exibam no modo bruto.*

```python
- Chamando o interpretador (python)
- executando o script com a flag -i (python -i app.py)
```
---
