# 14. Remover um Elemento de uma Lista

listaNumerica = []
numeroRemovido = 0

while len(listaNumerica) < 5:
    try:
        numeros = int(input("Digite um número: "))
        if len(listaNumerica) > 5:
            print("Limite de 5 itens excedido. Tente novamente.")
            continue
        listaNumerica.append(numeros)
    except NameError and ValueError as error:
        print("não pode deixar em branco!")
print(listaNumerica)
while True:
    numeroRemovido = int(input("Escolha um número da lista para remover: "))
    if numeroRemovido in listaNumerica:
        listaNumerica.remove(numeroRemovido)
        break
    else:
        print("número não está na lista")
print(f"Lista atualizada: {listaNumerica}")