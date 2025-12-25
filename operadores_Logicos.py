print(True and True)

print(True and False)

print(True or True)

print(True or False)

#and = True se ambos os valores forem True
#or = True se ao menos um dos valores for True

saldo = 1000
saque = 250
limite = 200
conta_especial = True



expression = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

expression2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque  )

print(expression)
print(expression2)