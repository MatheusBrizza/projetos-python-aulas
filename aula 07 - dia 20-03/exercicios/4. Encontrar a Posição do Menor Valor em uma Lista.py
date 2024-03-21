# 4. Encontrar a Posição do Menor Valor em uma Lista

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
posicaoMenorNumeroLista = listaNumerica.index(min(listaNumerica))
print(f"A posição do menor número da lista ({min(listaNumerica)}) = posição {posicaoMenorNumeroLista} na lista")