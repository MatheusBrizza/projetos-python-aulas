'''
3. Classe Restaurante: 
Crie uma classe Restaurante que represente um restaurante com as seguintes 
características: 
Atributos 
privados: nome, especialidade, endereco, horario_funcionamento, cardapio. 
Métodos: 
__init__: Inicializa o restaurante com os atributos necessários. 
adicionar_prato: Adiciona um novo prato ao cardápio (com nome, 
descrição e preço). 
remover_prato: Remove um prato do cardápio (por nome). 
mostrar_cardapio: Imprime o cardápio completo (nome do prato, 
descrição e preço).
'''

# Crie uma classe Restaurante que represente um restaurante com as seguintes 
# características: 
# Atributos privados: nome, especialidade, endereco, horario_funcionamento, cardapio. 
class Restaurante:
    # Métodos: 
    # __init__: Inicializa o restaurante com os atributos necessários. 
    def __init__(self, nome, especialidade, endereco, horario_funcionamento):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__endereco = endereco
        self.__horario_funcionamento = horario_funcionamento
        self.__cardapio = {}
    
    
    # adicionar_prato: Adiciona um novo prato ao cardápio (com nome, 
    # descrição e preço). 
    def adicionar_prato(self):
        print("## Adicionando prato ##")
        while True:
            nome_prato = input("inserir nome de prato: ").lower()
            if nome_prato not in self.__cardapio:
                descricao_prato = input("inserir descrição prato: ").lower()
                preco_prato = float(input("Inserir preço prato: "))
                self.__cardapio[nome_prato] = {"descrição": descricao_prato, "preço":preco_prato}
            else:
                print("prato já está adicionado!")
            quebrar_loop = input("deseja inserir outro prato? (s/n) ")
            if quebrar_loop.lower() == 's':
                print(f"cardapio => {self.__cardapio}")
                # print([Prato.__init__(self, nome_prato, descricao_prato, preco_prato) for prato in self.__cardapio]) tentativa de printar objeto Prato dentro de lista cardápio, mas não deu
                continue
            elif quebrar_loop.lower() == 'n':
                print(f"cardapio => {self.__cardapio}")
                break

    # remover_prato: Remove um prato do cardápio (por nome).
    def remover_prato(self):
        print("## Removendo prato ##")
        nome_prato = input("inserir nome de prato: ").lower()
        if nome_prato in self.__cardapio:
            del self.__cardapio[nome_prato]
            print(f"{nome_prato} removido com sucesso!")
        else:
            print(f"{nome_prato} não está no cardápio!")
        
rest = Restaurante("bar do tião", "boteco", "rua a, 132", "17:00 - 02:00")
rest.adicionar_prato()
rest.remover_prato()
