#3. Encontrar a Média dos Valores em uma Lista

listaNumerica = []
while len(listaNumerica) < 5:
    try:
        numeros = int(input("Digite um número: "))
        if len(listaNumerica) > 5:
            print("Limite de 5 itens excedido. Tente novamente.")
            continue
        listaNumerica.append(numeros)
    except NameError and ValueError as error:
        print("não pode deixar em branco!")
mediaListaNumerica = sum(listaNumerica) / len(listaNumerica)
print(f"A média dos valores da lista {listaNumerica} = {mediaListaNumerica}")