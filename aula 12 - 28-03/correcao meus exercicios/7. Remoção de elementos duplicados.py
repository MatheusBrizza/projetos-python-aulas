# 7. Remoção de elementos duplicados: 
# Escreva um programa que remova elementos duplicados de um conjunto. Utilize while para iterar 
# pelo conjunto e if para verificar a presença de elementos duplicados.

listaNumerica = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números ao conjunto: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and listaNumerica != []:
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica.append(numeros)

conversorListaConjunto = set(listaNumerica)
for numeroRepetido in listaNumerica:
    if listaNumerica.count(numeroRepetido) > 1:
        listaNumerica.remove(numeroRepetido)
        conjuntoNumerico = set(listaNumerica)
        print(f"O número {numeroRepetido} teve suas repetições removidas e o resultado do conjunto foi {conjuntoNumerico}.")
    elif listaNumerica.count(numeroRepetido) == 1:
        conjuntoNumerico = set(listaNumerica)
        print(f"O número {numeroRepetido} não tem repetições no conjunto {conjuntoNumerico}")
    else:
        print(f"número {numeroRepetido} não está na lista")
