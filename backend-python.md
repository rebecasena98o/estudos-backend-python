

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
° *Parêntesis*
° *Expoentes*
° *Multiplicações e divisões (da esquerda para a direita)*
° *Somas e subtrações (da esquerda para a direita)*

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

### 🔹 Condicionais
```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
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
