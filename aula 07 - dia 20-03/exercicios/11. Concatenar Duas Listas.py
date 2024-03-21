# 11. Concatenar Duas Listas
lista1 = []
while len(lista1) < 5:
    try:
        numeros = int(input("Digite um número: "))
        if len(lista1) > 5:
            print("Limite de 5 itens excedido. Tente novamente.")
            continue
        lista1.append(numeros)
    except NameError and ValueError as error:
        print("não pode deixar em branco!")
print(f"primeira lista: {lista1}")
lista2 = []
while len(lista2) < 5:
    try:
        numeros = int(input("Digite um número: "))
        if len(lista2) > 5:
            print("Limite de 5 itens excedido. Tente novamente.")
            continue
        lista2.append(numeros)
    except NameError and ValueError as error:
        print("não pode deixar em branco!")
print(f"segunda lista: {lista2}")
print(f"juntando as duas listas fica assim: {lista1 + lista2}")