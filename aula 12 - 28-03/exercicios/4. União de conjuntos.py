# 4. União de conjuntos: 
# Escreva um programa que encontre a união de dois conjuntos. Utilize for para iterar pelos 
# elementos de ambos os conjuntos e adicionar à lista final.

listaNumerica1 = []
listaNumerica2 = []
while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números ao conjunto: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and listaNumerica1 != []:
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica1.append(numeros)
conjuntoNumerico1 = set(listaNumerica1)

while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and listaNumerica2 != []:
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica2.append(numeros)
conjuntoNumerico2 = set(listaNumerica2)

conjuntoConcatenados = conjuntoNumerico1.union(conjuntoNumerico2)
print(conjuntoConcatenados)