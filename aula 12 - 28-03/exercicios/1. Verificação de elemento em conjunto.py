# 1. Verificação de elemento em conjunto: 
# Escreva um programa que verifique se um determinado elemento está presente em um conjunto. 
# Utilize if e else para exibir mensagens informativas.

listaNumerica = []
while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números ao conjunto: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and listaNumerica != []:
        print(f"Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios ao conjunto')
        continue
    numeros = int(numeros)
    listaNumerica.append(numeros)
conjuntoNumerico = set(listaNumerica)
while True:
    numeroRepetido = int(input("digite um número que deseja ver se ele está no conjunto: "))

    if numeroRepetido in conjuntoNumerico:
        print(f"O número {numeroRepetido} se encontra no conjunto.")
        break
    else:
        print(f"O número {numeroRepetido} não se encontra no conjunto.")
