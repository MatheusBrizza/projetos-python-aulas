'''
2. Produto 
Crie uma classe Produto com os atributos: 
nome: nome do produto 
preco: preço do produto 
Implemente os métodos getters e setters para: 
nome 
preco 
Crie um objeto da classe Produto e realize as seguintes operações: 
Acesse e imprima o nome do produto. 
Altere o nome do produto. 
Acesse e imprima o preço do produto. 
Aplique um desconto no preço do produto. 
Acesse e imprima o novo preço do produto. 
'''

# Crie uma classe Produto com os atributos: 
# nome: nome do produto 
# preco: preço do produto 
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
# Implemente os métodos getters e setters para: 
# nome 
# preco 
    def get_nome(self):
        return self.nome
    
    def get_preco(self):
        return self.preco

    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco

# Crie um objeto da classe Produto e realize as seguintes operações: 
produto = Produto("notebook", 5000)

# Acesse e imprima o nome do produto. 
print(f"nome produto: {produto.get_nome()}")

# Altere o nome do produto.
produto.set_nome("TV")
print(f"nome novo produto: {produto.get_nome()}")

# Acesse e imprima o preço do produto.
print(f"preço produto: {produto.get_preco()}")

# Aplique um desconto no preço do produto. 
desconto = produto.get_preco() * 0.9

# Acesse e imprima o novo preço do produto. 
print(f"preço produto com desconto: {desconto}")
