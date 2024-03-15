# Imprima a tabuada de um número digitado pelo usuário usando for
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")