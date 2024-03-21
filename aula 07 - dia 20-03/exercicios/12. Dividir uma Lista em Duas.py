# 12. Dividir uma Lista em Duas
listaNumerica = []
while len(listaNumerica) < 10:
    try:
        numeros = int(input("Digite um número: "))
        if len(listaNumerica) > 10:
            print("Limite de 10 itens excedido. Tente novamente.")
            continue
        listaNumerica.append(numeros)
    except NameError and ValueError as error:
        print("não pode deixar em branco!")
print(f"primeira lista: {listaNumerica}")
meio = len(listaNumerica) // 2
listaMenorInicio = listaNumerica[:meio]
listaMenorFinal = listaNumerica[meio:]
print(f"Primeira parte da lista: {listaMenorInicio}")
print(f"Segunda parte da lista: {listaMenorFinal}")