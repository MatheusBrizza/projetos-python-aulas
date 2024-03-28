# 13. Ordenar os Elementos de uma Lista

listaNumerica = []
while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

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
    
listaOrdenada = sorted(listaNumerica)
print(listaOrdenada)

