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
principais_atores = []
while True:
    chave = input("digite o chave: ")
    if chave != teclaParada:
        if chave == 'principais_atores':
            valorLista = input("digite o valor que deseja inserir na chave: ").split(' ')
            principais_atores.append(valorLista)
            filmeDict.update(principais_atores)
        else:
            valor = input("digite o valor que deseja inserir na chave: ")
            filmeDict[chave] = valor
    else:
        break
print(filmeDict)
# 'titulo': 'Corram que a Polícia Vem Aí!', 'diretor': 'David Zuker', 'genero': 'ação/comédia', 'principais_atores':[Leslie Nielsen, Priscilla Presley]