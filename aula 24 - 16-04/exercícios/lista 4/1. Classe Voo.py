'''
1. Classe Voo: 
Crie uma classe Voo que represente um voo com as seguintes características: 
Atributos 
privados: codigo, companhia, origem, destino, horario_saida, horario_chegada,
preco_passagem. 
Métodos: 
__init__: Inicializa o voo com os atributos necessários. 
calcular_duracao_voo: Calcula a duração do voo (diferença entre 
horários de saída e chegada). 
aplicar_desconto: Aplica um desconto percentual no preço da 
passagem. 
mostrar_informacoes: Imprime as informações do voo (código, 
companhia, origem, destino, horários, preço com desconto).
'''
# Crie uma classe Voo que represente um voo com as seguintes características: 
class Voo:
    # Atributos 
    # privados: codigo, companhia, origem, destino, horario_saida, horario_chegada,
    # preco_passagem.    
    # Métodos: 
    # __init__: Inicializa o voo com os atributos necessários. 
    def __init__(self, codigo, companhia, origem, destino, horario_saida, horario_chegada, preco_passagem):
        self.__codigo = codigo
        self.__companhia = companhia
        self.__origem = origem
        self.__destino = destino
        self.__horario_saida = horario_saida
        self.__horario_chegada = horario_chegada
        self.__preco_passagem = preco_passagem
        
    # calcular_duracao_voo: Calcula a duração do voo (diferença entre 
    # horários de saída e chegada). 
    def calcular_duracao_voo(self):
        duracao_voo = self.__horario_chegada - self.__horario_saida
        print(f"duração do vôo é de {duracao_voo} horas")

    # aplicar_desconto: Aplica um desconto percentual no preço da 
    # passagem. 
    def aplicar_desconto(self):
        desconto = self.__preco_passagem * 0.10
        self.__preco_passagem -= desconto
        print(f"preço da passagem com desconto é : {self.__preco_passagem}")
    
    # mostrar_informacoes: Imprime as informações do voo (código, 
    # companhia, origem, destino, horários, preço com desconto).
    def mostrar_informacoes(self):
        print(f"código do vôo:{self.__codigo}, companhia aérea:{self.__companhia}")
voo1 = Voo(123,"azul", "poa", "vaimao", 9, 19, 500.00)
voo1.calcular_duracao_voo()
voo1.aplicar_desconto()
voo1.mostrar_informacoes()
