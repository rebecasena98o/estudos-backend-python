def sacar (valor):
    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por utilizar o nosso caixa eletrônico.") #faz parte do método

def depositar(valor):
    saldo = 500
    saldo += valor
    
sacar(1000)