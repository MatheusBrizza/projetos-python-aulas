# 3. Diferença de conjuntos: 
# Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença no primeiro conjunto e não no segundo.

listaNumerica1 = []
listaNumerica2 = []
listaDifference = []
while True:
    tecla_parada = input("Pressione uma tecla para parar de agregar números ao conjunto: ")
    if not tecla_parada.isdigit():
        break
    else:
        print("Digite uma tecla, não um número.")

print("Sua tecla para parar é:", tecla_parada)
while True:
    numeros = input("Digite um número: ")
    if numeros == tecla_parada and listaNumerica1 != []:
        print("Fechando lista...")
        break
    elif not numeros.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros = int(numeros)
    listaNumerica1.append(numeros)
conjuntoNumerico1 = set(listaNumerica1)

while True:
    numeros1 = input("Digite um número: ")
    if numeros1 == tecla_parada and listaNumerica2 != []:
        print("Fechando lista...")
        break
    elif not numeros1.isdigit():
        print('Não pode adicionar letras ou espaços vazios à lista')
        continue
    numeros1 = int(numeros1)
    listaNumerica2.append(numeros1)
conjuntoNumerico2 = set(listaNumerica2)


for elemento in listaNumerica1:
  # Verifique se o elemento está em apenas um dos conjuntos
  if elemento not in listaNumerica2 or elemento in listaNumerica1 and elemento not in listaNumerica2:
    listaDifference.append(elemento)

for elemento in listaNumerica2:
  # Verifique se o elemento está em apenas um dos conjuntos (considerando conjunto2)
  if elemento not in listaNumerica1 or elemento in listaNumerica2 and elemento not in listaNumerica1:
    listaDifference.append(elemento)




print(set(listaDifference))
listaDifference = list(set(listaNumerica1).symmetric_difference(set(listaNumerica2)))
print(set(listaDifference))

        
