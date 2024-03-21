# 6. Encontrar o Número de Vezes que um Valor Aparece em uma lista

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
numeroRepetido = int(input("digite um número que deseja ver quantas vezes foi repetido: "))
print(f"O número {numeroRepetido} se repetiu na lista {listaNumerica}: {listaNumerica.count(numeroRepetido)} vezes")