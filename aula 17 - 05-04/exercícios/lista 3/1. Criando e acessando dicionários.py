'''
1. Criando e acessando dicionários: 
Crie um dicionário para armazenar informações sobre um filme, incluindo 
título, ano, diretor e atores principais. 
Acesse o ano de lançamento do filme usando a chave apropriada. 
Modifique o valor do diretor para um novo diretor. 
Adicione uma nova chave-valor ao dicionário para incluir a duração do 
filme.
'''
filmeDict = {}
teclaParada = "-"
while True:
    chave = input("digite o chave: ")
    if chave != teclaParada:
        if chave == 'principais_atores':
            valorLista = input("lista de atores: ").split(' ')
            filmeDict[chave] = valorLista
        else:
            valor = input("digite o valor que deseja inserir na chave: ")
            filmeDict[chave] = valor
    else:
        break
print(filmeDict)

anoFilme = filmeDict.get("ano", "não tem chave 'ano'")
print(anoFilme)

diretorNovo = input("Informe o nome do novo diretor: ")
filmeDict["diretor"] = diretorNovo


# 'titulo': 'Corram que a Polícia Vem Aí!', 'diretor': 'David Zuker', 'genero': 'ação/comédia', 'principais_atores':[Leslie Nielsen, Priscilla Presley]