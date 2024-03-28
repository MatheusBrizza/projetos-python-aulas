# 11. Concatenar Duas Listas
lista1 = []
lista2 = []


while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números à lista: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and lista1 != []:
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    lista1.append(numeros)
    

while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and lista2 != []:
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    lista2.append(numeros)
print(f"segunda lista: {lista2}")
    
print(f"juntando as duas listas fica assim: {lista1 + lista2}")