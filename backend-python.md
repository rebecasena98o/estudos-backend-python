

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
- *Não existe uma palavra reservada em Python para informar ao interpretador que o valor é constante (usa-se a convenção que diz ao porgramador que a variável é uma constante - letras maíusculas)*
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

```Inicialização
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

### 🔹 Funções 
**Dir**
- Sem argumentos, retorna a lista de nomes no escopo local  atual. 
- Com um argumento, retorna uma lista de atributos válidos para o objeto.

```python
dir()
dir(100)
```

**Help**
- Invoca o sistema de ajuda integrado. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável.

```python
help()
help(100)
```
---

## 📌 Anotações importantes
> Python usa indentação para definir blocos de código.
