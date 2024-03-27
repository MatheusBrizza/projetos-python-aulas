# 15. Adicionar um Elemento a uma Lista

listaNumerica = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada:
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
        numeroAdicionado = int(input("Escolha um número da lista para adicionar: "))
    except ValueError:
        print("não pode deixar em branco")
        continue
    if numeroAdicionado in listaNumerica:
        print(f"número {numeroAdicionado} já está na lista.")
    else:
        listaNumerica.append(numeroAdicionado)
        print("Número adicionado!")
        break
print(f"Lista atualizada: {listaNumerica}")