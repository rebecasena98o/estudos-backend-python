nome = "Rebeca"

print(nome[0:3])  # 'Reb' - recomendação do vscode
print(nome.upper()) # 'REBECA'
print(nome.lower()) # 'rebeca'
print(nome.split("b")) # ['Re', 'eca'] - recomendação do vscode
print(nome.title()) # 'Rebeca'

texto = "Hello world    "

print(texto.strip() + "!") # 'Hello world!'
print(texto.rstrip() + "!") # 'Hello world!' - removeu os espaços da direita
print(texto.lstrip() + "!") # 'Hello world!' - removeu os espaços da esquerda

menu = "Python"

print("####" + menu + "#####")
print("####" + menu.center(20) + "#####") # centraliza o texto em um campo de 20 caracteres
print(menu.center(14))
print("-".join(menu)) # 'P-y-t-h-o-n' - insere o caractere '-' entre cada letra da string

for letra in menu:
    print(letra, end="-") #verificar e controlar o final da impressão

print("-".join(menu))    