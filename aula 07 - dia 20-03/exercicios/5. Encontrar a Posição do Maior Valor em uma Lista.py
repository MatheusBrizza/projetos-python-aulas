# 5. Encontrar a Posição do Maior Valor em uma Lista
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
posicaoMenorNumeroLista = listaNumerica.index(max(listaNumerica))
print(f"A posição do menor número da lista ({max(listaNumerica)}) = posição {posicaoMenorNumeroLista} na lista")