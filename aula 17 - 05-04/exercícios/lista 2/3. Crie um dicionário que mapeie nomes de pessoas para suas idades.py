'''
3. Crie um dicionário que mapeie nomes de pessoas para suas idades. 
Utilize o método in para verificar se uma pessoa está presente no 
dicionário e, se estiver, imprima sua idade. 
'''

teclaParada = "-"
pessoasDict = {}
while True:
    nome = input("digite um nome: ")
    if nome != teclaParada:
        idade = int(input("digite uma idade: "))
        pessoasDict[nome] = idade
    else:
        break
print(pessoasDict)

nome_verificar = input("veja se o nome está no dicionário: ")

if nome_verificar in pessoasDict:
    print(f"a pessoa {nome_verificar} está no banco de dados. Sua idade é {pessoasDict.get(nome_verificar, "impossível verificar idade")}")
else:
    print(f"não temos o nome {nome_verificar} nos nossos dados. {pessoasDict.get(nome_verificar, "impossível verificar idade")}")