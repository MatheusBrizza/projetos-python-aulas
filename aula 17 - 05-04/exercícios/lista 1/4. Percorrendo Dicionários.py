'''
4. Percorrendo Dicionários: 
• Crie um dicionário com as informações de um amigo e imprima cada chave 
e valor em linhas separadas. 
• Crie um dicionário com as informações de um produto e imprima todos os 
valores em uma única linha. 
• Crie um dicionário com as informações de um livro e imprima as chaves 
"título" e "autor" em uma única linha. 
• Crie um dicionário com as informações de um filme e imprima as chaves 
"nome" e "diretor" em uma única linha.
'''

amigoDict = dict(nome="Fernando", idade=34, curso="Te puxa South System", matricula="abc123")

for c, v in amigoDict.items():
    print(f"chave: {c}, valor: {v}")

produtoDict = {"nome":"calça", "preco":35, "cor":"azul", "tamanho":42}

produtoNomeValue = produtoDict.get("nome")
produtoPrecoValue = produtoDict.get("preco")
produtoCorValue = produtoDict.get("cor")
produtoTamanhoValue = produtoDict.get("tamanho")
print(f"nome: {produtoNomeValue}, preço: {produtoPrecoValue}, cor: {produtoCorValue}, tamanho: {produtoTamanhoValue}")

livroDict = {"nome":"A história dos Pingos", "autor":"Mary e Eliardo França", "ano_publicacao":1995, "genero":"infantil"}
livroNomeValue = livroDict.get("nome")
livroAutorValue = livroDict.get("autor")
print(f"título: {livroNomeValue}, nome autor: {livroAutorValue}")

filmeDict = dict(nome="Corram que a Polícia Vem Aí!", diretor="David Zuker", ano_lancamento=1988, genero="ação/comédia")

filmeNomeValue = filmeDict.get("nome")
filmeDiretorValue = filmeDict.get("diretor")
print(f"título: {filmeNomeValue}, nome diretor: {filmeDiretorValue}")
