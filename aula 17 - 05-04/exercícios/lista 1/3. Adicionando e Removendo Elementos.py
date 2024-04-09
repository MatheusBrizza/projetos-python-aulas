'''
3. Adicionando e Removendo Elementos: 
• Crie um dicionário vazio e adicione as chaves "nome" e "idade" com seus 
respectivos valores. 
• Crie um dicionário com as informações de um produto e remova a chave 
"cor". 
• Crie um dicionário com as informações de um livro e adicione a chave 
"tradução" com o valor "Sim". 
• Crie um dicionário com as informações de um filme e remova a chave "ano 
de lançamento".
'''

alunoDict = {}
alunoDict["nome"] = "matheus"
alunoDict["idade"] = 15

print(f"dicionário aluno -> {alunoDict}")

produtoDict = {"nome":"calça", "preco":35, "cor":"azul", "tamanho":42}
produtoDict.pop("cor")
print(f"dicionário produto -> {produtoDict}")

livroDict = {"nome":"A história dos Pingos", "autor":"Mary e Eliardo França", "ano_publicacao":1995, "genero":"infantil"}
livroDict.update({"traducao":"Sim"})
print(f"dicionário livro -> {livroDict}")

filmeDict = dict(nome="Corram que a Polícia Vem Aí!", diretor="David Zuker", ano_lancamento=1988, genero="ação/comédia")
filmeDict.pop("ano_lancamento")
print(f"dicionário filme -> {filmeDict}")