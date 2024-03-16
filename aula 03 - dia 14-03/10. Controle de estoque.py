# Crie um sistema de controle de estoque com as operações de entrada, saída e 
# consulta de produtos usando while.

estoque = 0

while True:
    print("Bem vindo ao estoque de aditivos Senac")
    print("1 - ver estoque")
    print("2 - saída de estoque")
    print("3 - entrada de estoque")
    print("0 - sair")
    opcao = int(input("escolha uma opção: "))
    
    match opcao:
        case 1:
            print(estoque)
        case 2:
            saidaEstoque = float(input("Informe a quantidade que está para retirar do estoque: "))
            if estoque <= 0:
                print("estoque insuficiente!")
            else:
                estoque -= saidaEstoque 
                print(f"saída realizada com sucesso! O estoque atual de aditivos é: {estoque}")
        case 3:
            entradaEstoque = float(input("Informe a quantidade que irá adicionar ao estoque: "))
            if entradaEstoque <= 0:
                print("não pode adicionar quantidade negativa nem 0!")
            else:
                estoque += entradaEstoque
                print(f"entrada realizada com sucesso! O estoque atual é: {estoque}")
        case 0:
            break
        case _:
            print("Opção inválida!")
                