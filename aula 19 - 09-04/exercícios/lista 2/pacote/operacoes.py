def adicao():
    try:
        num1 = float(input("informe o primeiro número: "))
        num2 = float(input("informe o segundo número: "))
        resultado = num1 + num2
        return print(f"Resultado da soma é: {resultado}")
    except ValueError:
        print("não pôde efetuar o cálculo por falta de um ou mais valores")

def subtracao():
    try:
        num1 = float(input("informe o primeiro número: "))
        num2 = float(input("informe o segundo número: "))
        resultado = num1 - num2
        return print(f"Resultado da subtração é: {resultado}")
    except ValueError:
        print("não pôde efetuar o cálculo por falta de um ou mais valores")

def multiplicacao():
    try:
        num1 = float(input("informe o primeiro número: "))
        num2 = float(input("informe o segundo número: "))
        resultado = num1 * num2
        return print(f"Resultado da multiplicação é: {resultado}")
    except ValueError:
        print("não pôde efetuar o cálculo por falta de um ou mais valores")

def divisao():
    try:
        num1 = float(input("informe o primeiro número: "))
        num2 = float(input("informe o segundo número: "))    
        resultado = num1 / num2
        return print(f"Resultado da divisão é: {resultado:.2f}")
    except ValueError:
        print("não pôde efetuar o cálculo por falta de um ou mais valores")
    except (UnboundLocalError, ZeroDivisionError):
        print("Não é possível dividir por 0.")
        


def inserirNumerosLista():
    listaNumeros = []
    while True:
        tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
        if not tecla_parada.isdigit():
            break
        else:
            print("Digite uma tecla, não um número.")

    print("Sua tecla para parar é:", tecla_parada)
    while True:
        numeros = input("Digite um número: ")
        if numeros == tecla_parada and len(listaNumeros) >= 1:
            print(f"Fechando lista...")
            break
        elif not numeros.isdigit():
            print('A lista só aceita números')
            continue
        numeros = int(numeros)
        listaNumeros.append(numeros)
    return listaNumeros
        