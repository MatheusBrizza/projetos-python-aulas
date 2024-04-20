'''
4: Jogo de Cartas 
Crie as classes: 
Carta (classe base com atributos valor e naipe). 
CartaBaralho (herda de Carta, implementa métodos __str__() e comparar()). 
Baralho (armazena cartas, possui métodos para embaralhar, distribuir e 
mostrar cartas). 
Crie um baralho: 
Inclua cartas de diferentes valores e naipes. 
Embaralhe e distribua: 
Distribua cartas para jogadores (por exemplo, 2 cartas para cada um). 
Compare as cartas: 
Utilize o método comparar() para comparar as cartas de dois jogadores.
'''
import random
class Carta:
    def __init__(self, naipe):
        self.valor = random(1, 14)
        self.naipe = naipe

class CartaBaralho(Carta):
    def __str__(self) -> str:
        return super().__str__()
    
    def comparar():
        raise NotImplementedError
    
class Baralho:
    def guardar_cartas():
        baralho = []
    
    def embaralhar():
        raise NotImplementedError

    def distribuir():
        raise NotImplementedError

    def mostrar_cartas():
        raise NotImplementedError

