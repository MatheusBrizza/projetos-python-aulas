'''
1. Calculadora Básica Aprimorada: 
• Crie funções para cada operação matemática básica (soma, subtração, 
multiplicação e divisão). 
• Valide se os números recebidos são realmente numéricos. 
• Trate erros de divisão por zero de forma adequada. 
• Apresente os resultados com formatação decimal adequada (ex: 2.5, 3.14).
'''
import pacote.operacoes as pac


def calcular():
    while True:
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")
        try:
            opcao = int(input("informe a operação que deseja: "))
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
            

calcular()