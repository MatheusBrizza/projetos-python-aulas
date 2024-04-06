'''
2. Acessando Valores: 
• Crie um dicionário com as informações de um amigo e acesse o valor da 
chave "nome". 
• Crie um dicionário com as informações de um produto e acesse o valor da 
chave "preço".
'''

amigoDict = dict(nome="Fernando", idade=34, curso="Te puxa South System", matricula="abc123")
nomeAmigo = amigoDict.get("nome")

print(f"Nome do amigo: {nomeAmigo}")

produtoDict = {"nome":"calça", "preco":35, "cor":"azul", "tamanho":42}

precoProduto = produtoDict["preco"]

print(f"Preço do produto: {precoProduto}")