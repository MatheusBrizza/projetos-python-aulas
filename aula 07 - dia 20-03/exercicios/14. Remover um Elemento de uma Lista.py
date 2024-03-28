# 14. Remover um Elemento de uma Lista

listaNumerica = []
numeroRemovido = 0
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
print(listaNumerica)
while True:
    try:
        numeroRemovido = int(input("Escolha um número da lista para remover: "))
    except ValueError:
        print("não pode deixar em branco!")
        continue
    if numeroRemovido in listaNumerica:
        listaNumerica.remove(numeroRemovido)
        break
    else:
        print("número não está na lista")
print(f"Lista atualizada: {listaNumerica}")