# 15. Adicionar um Elemento a uma Lista

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
print(listaNumerica)
while True:
    numeroAdicionado = int(input("Escolha um número da lista para adicionar: "))
    if numeroAdicionado in listaNumerica:
        print(f"número {numeroAdicionado} já está na lista.")
    else:
        listaNumerica.append(numeroAdicionado)
        print("Número adicionado!")
        break
print(f"Lista atualizada: {listaNumerica}")