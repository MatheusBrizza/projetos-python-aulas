'''
2. Crie um dicionário que mapeie nomes de países para suas capitais. 
Utilize o método get() para buscar a capital de um país específico, tratando 
o caso de chave inexistente.
'''

teclaParada = "-"
paisesDict = {}
while True:
    pais = input("digite um país: ")
    if pais != teclaParada:
        capital = input("digite uma capital: ")
        paisesDict[pais] = capital
    else:
        break
print(paisesDict)

pais_verificar = input("veja se o pais está no dicionário: ")


if pais_verificar in paisesDict:
    print(f"o país {pais_verificar} está no dicionário. Sua capital é {paisesDict.get(pais_verificar)}")
else:
    print(f"o país {pais_verificar} não está na lista. {paisesDict.get(pais_verificar, "não tem")} a capital no dicionário")
