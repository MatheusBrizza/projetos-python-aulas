# Crie um simulador de caixa eletrônico com as operações de saldo, saque e 
# depósito usando while.

saldo = 0

while True:
    print("Bem vindo ao banco Senac")
    print("1 - ver saldo")
    print("2 - saque")
    print("3 - depósito")
    print("0 - sair")
    opcao = int(input("escolha uma opção: "))
    
    match opcao:
        case 1:
            print(saldo)
        case 2:
            saque = float(input("Digite o valor que deseja sacar na conta: "))
            if saque <= 0:
                print("não pode sacar valor negativo nem 0")
            elif saldo <= 0:
                print("saldo insuficiente!")
            else:
                saldo -= saque 
                print(f"saque realizado com sucesso! O saldo atual é: {saldo}")
        case 3:
            deposito = float(input("Digite o valor que deseja depositar na conta: "))
            if deposito <= 0:
                print("não pode depositar valor negativo nem 0")
            else:
                saldo += deposito
                print(f"depósito realizado com sucesso! O saldo atual é: {saldo}")
        case 0:
            break
        case _:
            print("opção inválida")