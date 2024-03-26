# 12. Dividir uma Lista em Duas
listaNumerica = []

while True:
  tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
  if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
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

print(f"primeira lista: {listaNumerica}")
meio = len(listaNumerica) // 2
listaMenorInicio = listaNumerica[:meio]
listaMenorFinal = listaNumerica[meio:]
print(f"Primeira parte da lista: {listaMenorInicio}")
print(f"Segunda parte da lista: {listaMenorFinal}")