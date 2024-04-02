# 2. Interseção de conjuntos: 
# Escreva um programa que encontre a interseção de dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença em ambos os conjuntos.

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
listaIntersection = []
for numero in listaNumerica1:
    for numero in listaNumerica2:
        print(numero)
        if numero in listaNumerica1 and numero in listaNumerica2:
            listaIntersection.append(numero)
conversorListaConjunto = set(listaIntersection)
print(conversorListaConjunto)

#método com intersection()
# numeroConjuntoIntersection = conjuntoNumerico1.intersection(conjuntoNumerico2)
# print(f"O(s) número(s) que faz(em) intercessão  nos conjuntos é/são: {numeroConjuntoIntersection}")