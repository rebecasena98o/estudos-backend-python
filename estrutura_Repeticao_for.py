texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #Adiciona quebra de linha 
    print("Executa no final do laço")   

# Exemplo usando a função built-in range()
for numero in range(0, 51, 5):
    print(numero, end=" ")        