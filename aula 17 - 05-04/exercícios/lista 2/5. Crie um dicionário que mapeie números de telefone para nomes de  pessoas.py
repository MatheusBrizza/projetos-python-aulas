'''
5. Crie um dicionário que mapeie números de telefone para nomes de 
pessoas. Utilize o método pop() para remover um número de telefone do 
dicionário e, em seguida, verifique se a chave foi removida. 
'''

teclaParada = "-"
pessoasDict = {}
while True:
    telefone = input("digite o telefone: ")
    if telefone != teclaParada:
        nome = input("digite o nome do dono do telefone: ")
        telefoneInputDict = {telefone:nome}
        pessoasDict.update(telefoneInputDict)
    else:
        break
print(pessoasDict)

telefone_verificar = input("veja se o telefone está no dicionário: ")

if telefone_verificar in pessoasDict:
    print(f"O telefone {telefone_verificar} está no banco de dados.")
    pessoasDict.pop(telefone_verificar)
    print(pessoasDict)
else:
    print(f"não temos o animal {telefone_verificar} nos nossos dados. {pessoasDict.get(telefone_verificar, "Impossível verificar telefone")}")