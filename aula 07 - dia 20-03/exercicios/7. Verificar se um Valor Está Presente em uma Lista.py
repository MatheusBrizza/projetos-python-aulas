# 7. Verificar se um Valor Está Presente em uma Lista

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
numeroRepetido = int(input("digite um número que deseja ver se ele está na lista: "))
if listaNumerica.count(numeroRepetido) != 0:
    print(f"O número {numeroRepetido} se encontra na lista.")
else:
    print(f"O número {numeroRepetido} não se encontra na lista.")