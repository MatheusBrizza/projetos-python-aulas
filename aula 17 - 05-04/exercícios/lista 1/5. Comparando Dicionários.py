'''
5. Comparando Dicionários: 
• Crie dois dicionários com as informações de dois alunos e compare seus 
nomes e idades. 
• Crie dois dicionários com as informações de dois produtos e compare seus 
preços. 
• Crie dois dicionários com as informações de dois livros e compare seus 
autores. 
• Crie dois dicionários com as informações de dois filmes e compare seus 
diretores.
'''

dicionario1 = {"nome": "lucas", "idade": 34}
dicionario2 = {"nome": "lucas", "idade": 52}

intersecao = {}
                    
for chave in dicionario1:
    if dicionario1[chave] == dicionario2[chave]:
        intersecao[chave] = dicionario1[chave]

print(intersecao)
