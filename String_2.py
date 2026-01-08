nome = "Rebeca"
idade = 25
profissao = "Programadora"
linguagem = "Python"
salario = 60000.00

dados = {"nome": "Rebeca", "idade": 25, "profissao": "Programadora", "linguagem": "Python"}

print("Nome: %s idade: %d" % (nome, idade)) #String e Inteiro
print("Profissão: %s" % profissao) #String


print("Nome: {} idade: {}".format(nome, idade))

print("Nome: {1} idade: {0}".format(nome, idade))

print("Nome: {nome} idade: {idade}".format(nome=nome, idade=idade))

print("Nome: {nome} idade: {idade} profissao: {profissao} linguagem: {linguagem}".format(**dados))

print(f"Nome: {nome} idade: {idade} salario: {salario:.2f}")

print(f"Nome: {nome} idade: {idade} salario: {salario:10.2f}") #ou 0.2f para preencher com zeros a esquerda