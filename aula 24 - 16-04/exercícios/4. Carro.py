'''
4. Carro 
Crie uma classe Carro com os atributos: 
marca: marca do carro 
modelo: modelo do carro 
ano: ano de fabricação do carro 
Implemente os métodos getters e setters para: 
marca 
modelo 
ano 
Crie um objeto da classe Carro e realize as seguintes operações: 
Acesse e imprima a marca do carro. 
Altere a marca do carro. 
Acesse e imprima o modelo do carro. 
Altere o modelo do carro. 
Acesse e imprima o ano de fabricação do carro. 
Altere o ano de fabricação do carro.
'''

# Crie uma classe Carro com os atributos: 
# marca: marca do carro 
# modelo: modelo do carro 
# ano: ano de fabricação do carro 
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Implemente os métodos getters e setters para: 
# marca 
# modelo 
# ano 
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano
    
    def set_marca(self, nova_marca):
        self.marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.ano = novo_ano
        
# Crie um objeto da classe Carro e realize as seguintes operações: 
carro = Carro("vw", "corsa", 2000)

# Acesse e imprima a marca do carro.
print(f"marca carro: {carro.get_marca()}")
# Altere a marca do carro.
carro.set_marca("ford")
print(f"nova marca carro: {carro.get_marca()}")

# Acesse e imprima o modelo do carro. 
print(f"modelo carro: {carro.get_modelo()}")

# Altere o modelo do carro. 
carro.set_modelo("fiesta")
print(f"novo modelo carro: {carro.get_modelo()}")

# Acesse e imprima o ano de fabricação do carro. 
print(f"ano carro: {carro.get_ano()}")

# Altere o ano de fabricação do carro.
carro.set_ano(2020)
print(f"novo ano carro: {carro.get_ano()}")