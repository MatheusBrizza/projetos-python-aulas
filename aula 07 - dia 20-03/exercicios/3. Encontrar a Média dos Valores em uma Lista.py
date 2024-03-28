#3. Encontrar a Média dos Valores em uma Lista

listaNumerica = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada:
        print(f"Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica.append(numeros)
try:
    if len(listaNumerica) < 2:
        print("Não é possível verificar a média da lista com apenas 1 elemento")
    else:
        mediaListaNumerica = sum(listaNumerica) / len(listaNumerica)
        print(f"A média dos valores da lista {listaNumerica} = {mediaListaNumerica}")
except ValueError and NameError and ZeroDivisionError as error:
    print("Lista está vazia")