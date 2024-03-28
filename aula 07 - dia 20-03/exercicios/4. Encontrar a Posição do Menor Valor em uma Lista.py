# 4. Encontrar a Posição do Menor Valor em uma Lista

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
        print("Não é certo verificar o menor número com apenas 1 elemento na lista")
    else:
        posicaoMenorNumeroLista = listaNumerica.index(min(listaNumerica))
        print(f"A posição do menor número da lista ({min(listaNumerica)}) = posição {posicaoMenorNumeroLista} na lista")
except ValueError as error:
    print("lista está vazia")