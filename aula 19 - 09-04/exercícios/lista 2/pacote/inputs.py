def inputsDoisElementos():
    try:
        num1 = float(input("informe o primeiro número: "))
        num2 = float(input("informe o segundo número: "))
    except ValueError:
        print("valor inválido")
    return num1, num2
