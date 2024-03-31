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
# while True:
#     numeroRepetido = int(input("digite um número que deseja ver se está em ambos os conjuntos: "))
#     for numeroRepetido in conjuntoNumerico1:
#         for numeroRepetido in conjuntoNumerico2:
#             if numeroRepetido in conjuntoNumerico1 and numeroRepetido in conjuntoNumerico2:
#                 print(f"{numeroRepetido} está em ambos os conjuntos")
#                 break
#             else:
#                 print(f"{numeroRepetido} não está nas listas")

#método com intersection()

numeroConjuntoIntersection = conjuntoNumerico1.intersection(conjuntoNumerico2)
print(f"O(s) número(s) que faz(em) intercessão  nos conjuntos é/são: {numeroConjuntoIntersection}")