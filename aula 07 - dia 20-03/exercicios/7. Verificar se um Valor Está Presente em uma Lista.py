# 7. Verificar se um Valor Está Presente em uma Lista

listaNumerica = []

while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
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
try:
    numeroRepetido = int(input("digite um número que deseja ver se ele está na lista: "))
    if listaNumerica.count(numeroRepetido) != 0:
        print(f"O número {numeroRepetido} se encontra na lista.")
    else:
        print(f"O número {numeroRepetido} não se encontra na lista.")
except ValueError as error:
    print("lista está vazia")