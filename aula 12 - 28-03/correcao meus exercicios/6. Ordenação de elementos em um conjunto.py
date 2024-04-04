# 6. Ordenação de elementos em um conjunto:
# Escreva um programa que ordene os elementos de um conjunto em ordem crescente ou 
# decrescente. Utilize for para iterar pelos elementos e if para comparar e trocar posições.

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
conjuntoNumerico = set(listaNumerica)

conjuntoOrdenado = sorted(conjuntoNumerico)
print(f"o conjunto ordenado fica: {conjuntoOrdenado}")