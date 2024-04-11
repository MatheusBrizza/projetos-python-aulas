'''
1. Calculadora básica: 
Crie uma função para cada operação matemática básica (soma, subtração, 
multiplicação e divisão) que recebe dois números como parâmetros e retorna o 
resultado da operação.
'''

def calcular():
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    opcao = int(input("informe a operação que deseja: "))
    match opcao:
        case 1:
            adicao()
        case 2:
            subtracao()
        case 3: 
            multiplicacao()
        case 4:
            divisao()
        case _:
            print("opção inválida")
            
def adicao():
    try:
        num1 = int(input("informe o primeiro número: "))
        num2 = int(input("informe o segundo número: "))
    except ValueError:
        print("valor inválido")
    try:
        return print(f"Resultado da soma é: {num1 + num2}")
    except UnboundLocalError:
        print("não pode efetuar o cálculo por falta de um valor")
def subtracao():
    try:
        num1 = int(input("informe o primeiro número: "))
        num2 = int(input("informe o segundo número: "))
    except ValueError:
        print("valor inválido")
    try:
        return print(f"Resultado da subtração é: {num1 - num2}")
    except UnboundLocalError:
        print("não pode efetuar o cálculo por falta de um valor")
def multiplicacao():
    try:
        num1 = int(input("informe o primeiro número: "))
        num2 = int(input("informe o segundo número: "))
    except ValueError:
        print("valor inválido")
    try:
        return print(f"Resultado da multiplicação é: {num1 * num2}")
    except UnboundLocalError:
        print("não pode efetuar o cálculo por falta de um valor")
def divisao():
    try:
        num1 = int(input("informe o primeiro número: "))
        num2 = int(input("informe o segundo número: "))
    except ValueError:
        print("valor inválido")
    try:
        return print(f"Resultado da divisão é: {num1 / num2}")
    except UnboundLocalError:
        print("não pode efetuar o cálculo por falta de um valor")


calcular()