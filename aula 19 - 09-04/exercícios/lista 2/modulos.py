import pacote.operacoes as pac


def iniciarCalculadora():
    while True:
        print("")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        print("")
        try:
            opcao = int(input("informe a operação que deseja: "))
            print("")
        except ValueError:
            opcao = -1
        match opcao:
            case 1:
                pac.adicao()
            case 2:
                pac.subtracao()
            case 3: 
                pac.multiplicacao()
            case 4:
                pac.divisao()
            case 0:
                print("Saíndo")
                break
            case _:
                print("opção inválida")
            
def maiorEntreNumeroVariaveis():
    while True:
        listaNumerica = pac.inserirNumerosLista()
        listaMaiores = []
        print(listaNumerica)
        maior = listaNumerica[0]
        for i in listaNumerica:
            if i > maior:
                maior = i
            elif i == maior:
                listaMaiores.append(i)
        print(listaMaiores)
        return print(f"O maior valor da lista é: {maior}")
        