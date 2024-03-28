# 6. Encontrar o Número de Vezes que um Valor Aparece em uma lista

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
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica.append(numeros)
try:
    if len(listaNumerica) < 2:
        print("Não é possível ver número repetído com apenas 1 elemento.")
    else:
        numeroRepetido = int(input("digite um número que deseja ver quantas vezes foi repetido: "))
        print(f"O número {numeroRepetido} se repetiu na lista {listaNumerica}: {listaNumerica.count(numeroRepetido)} vezes")
except ValueError as error:
    print("lista está vazia")