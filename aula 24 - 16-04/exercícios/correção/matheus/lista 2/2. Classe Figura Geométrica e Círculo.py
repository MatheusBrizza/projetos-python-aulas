'''
2. Classe Figura Geométrica e Círculo: 
Crie uma classe abstrata FiguraGeometrica com os 
métodos calcular_area() e descrever(). 
Crie uma classe Circulo que herde de FiguraGeometrica. 
Implemente o método calcular_area() na classe Circulo para calcular a 
área do círculo. 
Crie um objeto circulo1 e chame os 
métodos calcular_area() e descrever().
'''
import math as m
# Crie uma classe abstrata FiguraGeometrica com os 
# métodos calcular_area() e descrever(). 
class FiguraGeometrica:
    def calcular_area(self):
        raise NotImplementedError
    
    def descrever(self):
        raise NotImplementedError
    
# Crie uma classe Circulo que herde de FiguraGeometrica. 
class Circulo(FiguraGeometrica):

    def __init__(self, raio):
        self.raio = raio
        
    # Implemente o método calcular_area() na classe Circulo para calcular a área do círculo.     
    def calcular_area(self):
        return m.pow(self.raio, 2) * 3.1415
    
    def descrever(self):
        print(f"Sou um círculo e minha área é {self.calcular_area()}")

# Crie um objeto circulo1 e chame os métodos calcular_area() e descrever().
circulo1 = Circulo(2)
circulo1.descrever()