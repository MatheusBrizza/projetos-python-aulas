'''
4. Classe Veículo e Carro:
Crie uma classe abstrata Veiculo com os atributos marca, modelo e ano. 
Crie uma classe Carro que herde de Veiculo. 
Adicione à classe Carro os atributos cor, numero_portas e tipo_cambio. 
Implemente 
métodos ligar(), desligar(), acelerar(), frear() e descrever() nas 
classes Veiculo e Carro. 
Crie um objeto carro1 e chame os métodos adequados.
'''

# Crie uma classe abstrata Veiculo com os atributos marca, modelo e ano. 
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.motorLigado = False
        self.velocidade = 0

    def descrever(self):
        print(f"marca:{self.marca}, modelo:{self.modelo}, ano:{self.ano}")
    # Implemente métodos ligar(), desligar(), acelerar(), frear() e descrever() nas 
    # classes Veiculo e Carro.        
    def ligar(self):
        if self.motorLigado == True:
            print("veículo já está ligado!")
        else:
            self.motorLigado = True
            print("veículo ligado")
    
    def desligar(self):
        if self.motorLigado == False:
            print("veículo já está desligado!")
        else:
            self.motorLigado = False
            print("veículo desligado")
    
    def acelerar(self):
        if self.motorLigado == False:
            print("não é possível acelerar com o motor desligado!")
        else:
            self.velocidade += 10
            print(f"velocidade atual: {self.velocidade}")
    
    def frear(self):
        if self.velocidade <= 0:
            print("veículo está parado")
        else:
            self.velocidade -= 10
            print(f"velocidade atual: {self.velocidade}")
    
# Crie uma classe Carro que herde de Veiculo.
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, numero_portas, tipo_cambio):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.numero_portas = numero_portas
        self.tipo_cambio = tipo_cambio
    
# Implemente métodos ligar(), desligar(), acelerar(), frear() e descrever() nas 
# classes Veiculo e Carro.
    def descrever(self):
        super().descrever()
        print(f"cor:{self.cor}, numero de portas:{self.numero_portas}, tipo de câmbio:{self.tipo_cambio}")

# Crie um objeto carro1 e chame os métodos adequados.
carro1 = Carro("vw", "corsa", 2020, "azul", 5, "manual")
carro1.ligar()
carro1.ligar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.frear()
carro1.desligar()
carro1.acelerar()
carro1.descrever()