'''
5. Ponto Geográfico 
Crie uma classe PontoGeografico com os atributos: 
latitude: latitude do ponto 
longitude: longitude do ponto 
Implemente os métodos getters e setters para: 
latitude 
longitude 
Crie um objeto da classe PontoGeografico e realize as seguintes operações: 
Acesse e imprima a latitude do ponto. 
Altere a latitude do ponto. 
Acesse e imprima a longitude do ponto. 
Altere a longitude do ponto.
'''

# Crie uma classe PontoGeografico com os atributos: 
# latitude: latitude do ponto 
# longitude: longitude do ponto 
class PontoGeografico:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

# Implemente os métodos getters e setters para: 
# latitude 
# longitude 
    def get_latitude(self):
        return self.latitude
    
    def get_longitude(self):
        return self.longitude
    
    def set_latitude(self, nova_latitude):
        self.latitude = nova_latitude
    
    def set_longitude(self, nova_longitude):
        self.longitude = nova_longitude
    
# Crie um objeto da classe PontoGeografico e realize as seguintes operações: 
pontoGeografico = PontoGeografico(100, 100)
# Acesse e imprima a latitude do ponto.
print(f"latitude: {pontoGeografico.get_latitude()}")
# Altere a latitude do ponto. 
pontoGeografico.set_latitude(200)
print(f"nova latitude: {pontoGeografico.get_latitude()}")

# Acesse e imprima a longitude do ponto. 
print(f"longitude: {pontoGeografico.get_longitude()}")

# Altere a longitude do ponto.
pontoGeografico.set_longitude(200)
print(f"nova longitude: {pontoGeografico.get_longitude()}")
