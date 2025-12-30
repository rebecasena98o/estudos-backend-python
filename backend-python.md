

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

### 🔹Exemplos:

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
### 🔍 Curiosidades
- *Booleano: implementado pela classe bool. Em Python, o tipo booleano é uma subclasse de int, uma vez que qualquer número diferente de 0 representa verdadeiro e 0 representa falso.*

---
### 🔹 Modo Interativo
- *O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código e ver o resultado na hora - escrever e ver antes de códigos que o exibam no modo bruto.*

```python
- Chamando o interpretador (python)
- executando o script com a flag -i (python -i app.py)
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
**Input**
- *A função builtin input é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.*
```python
nome = input("informe o seu nome: ")
>>> informe o seu nome:
```

**Print**
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
**Dir**
- *Sem argumentos, retorna a lista de nomes no escopo local  atual.* 
- *Com um argumento, retorna uma lista de atributos válidos para o objeto.*

```python
dir()
dir(100)
```

**Help**
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

## 📌 Anotações importantes
> Python usa indentação para definir blocos de código.
