MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você pode tirar a cnh.")

if idade < MAIOR_IDADE:
    print("Você não pode tirar a cnh.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh.") 

else:
    print("Ainda não pode tirara a cnh.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a cnh.")

elif idade == IDADE_ESPECIAL:
    print("Você pode participar das aulas teóricas, mas não da prática.")

else:
    print("Ainda não pode tirar a cnh.")