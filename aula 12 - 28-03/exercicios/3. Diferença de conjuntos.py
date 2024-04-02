# 3. Diferença de conjuntos: 
# Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença no primeiro conjunto e não no segundo.

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

#método com for e if
listaDifference = []
for numero in listaNumerica1:
    if numero in listaNumerica1 and numero not in listaNumerica2 or numero not in listaNumerica1 and numero in listaNumerica2:
        print(f"{numero}")

 
#método difference()
# numerosConjuntoDifference = conjuntoNumerico1.symmetric_difference(conjuntoNumerico2)
# print(f"os números que não tem nos conjuntos são: {numerosConjuntoDifference}")