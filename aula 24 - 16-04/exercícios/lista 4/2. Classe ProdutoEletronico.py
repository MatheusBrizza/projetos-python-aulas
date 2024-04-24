'''
2. Classe ProdutoEletronico: 
Crie uma classe ProdutoEletronico que represente um produto eletrônico com as 
seguintes características: 
Atributos privados: codigo, nome, marca, modelo, preco, tipo. 
Métodos: 
__init__: Inicializa o produto eletrônico com os atributos necessários. 
aplicar_garantia_estendida: Adiciona garantia estendida ao produto 
(aumentando o preço). 
calcular_valor_total: Calcula o valor total do produto com garantia (se 
aplicável). 
mostrar_informacoes: Imprime as informações do produto eletrônico 
(código, nome, marca, modelo, preço, tipo, garantia).
'''
# Crie uma classe ProdutoEletronico que represente um produto eletrônico com as 
# seguintes características: 
# Atributos privados: codigo, nome, marca, modelo, preco, tipo.
class ProdutoEletronico:
    # __init__: Inicializa o produto eletrônico com os atributos necessários. 
    def __init__(self, codigo, nome, marca, modelo, preco, tipo):
        self.__codigo = codigo
        self.__nome = nome
        self.__marca = marca
        self.__modelo = modelo
        self.__preco = preco
        self.__tipo = tipo
        self.__garantia = 1
        self.__multiplicador_garantia = 0.20

    # aplicar_garantia_estendida: Adiciona garantia estendida ao produto 
    # (aumentando o preço).
    def aplicar_garantia_estendida(self):
        self.__garantia = 2
        print(f"Garantia extendida com sucesso! a garantia aumentou para {self.__garantia} anos")
    
    # calcular_valor_total: Calcula o valor total do produto com garantia (se 
    # aplicável).
    def calcular_valor_total(self):
        if self.__garantia == 1:
            print(f"O valor total do produto é R${self.__preco:.2f}")
        elif self.__garantia == 2:
            valor_extra_garantia = self.__preco * self.__multiplicador_garantia
            self.__preco += valor_extra_garantia
            print(f"O valor total do produto com garantia extendida é R${self.__preco:.2f}")
    
    # mostrar_informacoes: Imprime as informações do produto eletrônico 
    # (código, nome, marca, modelo, preço, tipo, garantia).
    def mostrar_informacoes(self):
        print(f"marca:{self.__marca}, modelo:{self.__modelo}, código do produto:{self.__codigo}, nome do produto:{self.__nome}, preço:R${self.__preco:.2f}, tipo do produto:{self.__tipo}, tempo de garantia(anos):{self.__garantia}")
        
prod = ProdutoEletronico(1003775,"tv OLED 60'","LG","tvlg",4000,"tv")
prod.mostrar_informacoes()
prod.calcular_valor_total() #sem garantia extendida
prod.aplicar_garantia_estendida()
prod.calcular_valor_total() #com garantia extendida