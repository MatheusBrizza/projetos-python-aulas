'''
2: Figuras Geométricas 
Crie as classes: 
Forma (classe base com método calcular_area() abstrato). 
Quadrado (herda de Forma, implementa calcular_area()). 
Retângulo (herda de Forma, implementa calcular_area()). 
Círculo (herda de Forma, implementa calcular_area()). 
Crie uma lista de formas: 
Inclua objetos de Quadrado, Retângulo e Círculo. 
Calcule e mostre: 
A área de cada forma.
'''
import math

# Crie as classes: 
# Forma (classe base com método calcular_area() abstrato).
class Forma:
    def calcular_area(self):
        raise NotImplementedError
    
# Quadrado (herda de Forma, implementa calcular_area()). 
class Quadrado(Forma):
    def calcular_area(self, lado):
        area = math.pow(lado, 2)
        print(f"Área do quadrado: {area}")

# Retângulo (herda de Forma, implementa calcular_area()).     
class Retangulo(Forma):
    def calcular_area(self, base, altura):
        area = base * altura
        print(f"Área do retângulo: {area}")

# Círculo (herda de Forma, implementa calcular_area()).
class Circulo(Forma):
    def calcular_area(self, raio):
        area = 3.14 * math.pow(raio, 2)
        print(f"Área do círculo: {area}")

# Crie uma lista de formas:
# Inclua objetos de Quadrado, Retângulo e Círculo.        
quadrado1 = Quadrado()
retangulo1 = Retangulo()
circulo1 = Circulo()
listaFormas = []
listaFormas.append(quadrado1)
listaFormas.append(retangulo1)
listaFormas.append(circulo1)

# Calcule e mostre: 
# A área de cada forma.

listaFormas[0].calcular_area(5)
listaFormas[1].calcular_area(5, 6)
listaFormas[2].calcular_area(3)