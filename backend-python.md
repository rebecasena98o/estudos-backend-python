

**Negrito**
*Itálico*
~~Riscado~~

# Bootcamp Back-End Python - DIO

## 📌 Módulo 1 – Fundamentos de Python

### 🔹 Variáveis
- *Usadas para armazenar valores*
- *Tipagem dinâmica*
- *Consomem 24 bytes de armazenamento na memória*

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

## 📌 Módulo 2 – Funções

### 🔹 Funções simples
```python
def saudacao(nome):
    return f"Olá, {nome}"
```

---

## 📌 Anotações importantes
> Python usa indentação para definir blocos de código.
