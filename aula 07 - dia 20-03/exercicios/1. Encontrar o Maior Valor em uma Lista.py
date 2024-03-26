# 1. Encontrar o Maior Valor em uma Lista

listaNumerica = []
numeros = ''
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
        print(f"Fechando lista... {listaNumerica}")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica.append(numeros)
try:
    print(f"O menor número da lista é: {min(listaNumerica)}")
except ValueError as error:
    print("lista está vazia")