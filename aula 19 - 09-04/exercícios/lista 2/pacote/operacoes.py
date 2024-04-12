from inputs import inputsDoisElementos

def adicao():
    num1 = 0
    num2 = 0
    inputsDoisElementos()
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