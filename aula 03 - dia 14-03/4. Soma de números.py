# Leia um número N e some todos os números de 1 a N usando while.
numero = int(input("Digite um número: "))
cont = 1
somaNova = 0
while cont <= numero:
    somaAntiga = somaNova
    somaNova += cont
    cont += 1
    print(f"{cont-1} + {somaAntiga} = {somaNova}")