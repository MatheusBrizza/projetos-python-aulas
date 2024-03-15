# Calcule o fatorial de um número digitado pelo usuário usando while

numero = int(input("Digite um número: "))
cont = 1
fatorial = 1
while cont <= numero:
    fatorial *= cont
    cont += 1
    print(f"{cont-1}! = {fatorial}")