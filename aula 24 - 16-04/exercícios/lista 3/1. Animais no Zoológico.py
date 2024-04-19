'''
1: Animais no Zoológico 
Crie as classes: 
Animal (classe base com métodos comer() e dormir()). 
Cachorro (herda de Animal, com método latir()). 
Gato (herda de Animal, com método miar()). 
Papagaio (herda de Animal, com método falar()). 
Crie uma lista de animais: 
Inclua objetos de Cachorro, Gato e Papagaio. 
Faça os animais: 
Comerem. 
Dormirem. 
Realizarem ações específicas (latir, miar, falar) de acordo com seu tipo.
'''

# Animal (classe base com métodos comer() e dormir()). 
class Animal:
    def comer(self):
        print("está comendo")
    
    def dormir(self):
        print("está dormindo")
        
# Cachorro (herda de Animal, com método latir()).
class Cachorro(Animal):
    def latir(self):
        print("Au Au")

# Gato (herda de Animal, com método miar()). 
class Gato(Animal):
    def miar(self):
        print("Maiu")
        
# Papagaio (herda de Animal, com método falar()).
class Papagaio(Animal):
    def falar(self):
        print("bolacha!")

# Crie uma lista de animais:
listaAnimais = []

# Inclua objetos de Cachorro, Gato e Papagaio. 
cachorro1 = Cachorro()
gato1 = Gato()
pepa = Papagaio()
listaAnimais.append(cachorro1)
listaAnimais.append(gato1)
listaAnimais.append(pepa)
print(listaAnimais)

# Faça os animais: 
# Comerem. 
# Dormirem. 
# Realizarem ações específicas (latir, miar, falar) de acordo com seu tipo.
listaAnimais[0].latir()
listaAnimais[0].dormir()
listaAnimais[0].comer()

listaAnimais[1].miar()
listaAnimais[1].dormir()
listaAnimais[1].comer()

listaAnimais[2].falar()
listaAnimais[2].dormir()
listaAnimais[2].comer()