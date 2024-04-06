'''
1. Criando Dicionários: 
• Crie um dicionário com as informações de um aluno: nome, idade, curso e 
matrícula. 
• Crie um dicionário com as informações de um produto: nome, preço, cor e 
tamanho. 
• Crie um dicionário com as informações de um livro: título, autor, ano de 
publicação e gênero. 
• Crie um dicionário com as informações de um filme: nome, diretor, ano de 
lançamento e gênero. 
• Crie um dicionário com as informações de um país: nome, capital, 
população e língua oficial.
'''
alunoDict = dict(nome="matheus", idade=17, curso="Te puxa South System", matricula="abc123")

produtoDict = {"nome":"calça", "preco":35, "cor":"azul", "tamanho":42}

livroDict = {"nome":"A história dos Pingos", "autor":"Mary e Eliardo França", "ano_publicacao":1995, "genero":"infantil"}

filmeDict = dict(nome="Corram que a Polícia Vem Aí!", diretor="David Zuker", ano_lancamento=1988, genero="ação/comédia")

paisDict = {"nome":"Brasil", "capital":"Brasília", "populacao":280000000, "lingua_oficial":"português"}

print(alunoDict)
print(produtoDict)
print(livroDict)
print(filmeDict)
print(paisDict)