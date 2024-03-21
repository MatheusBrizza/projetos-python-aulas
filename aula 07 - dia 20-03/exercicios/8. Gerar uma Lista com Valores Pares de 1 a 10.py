# 8. Gerar uma Lista com Valores Pares de 1 a 10:

listaNumerica = []
for numeros in range(1, 11):
    if numeros % 2 == 0:
        listaNumerica.append(numeros)
print(listaNumerica)