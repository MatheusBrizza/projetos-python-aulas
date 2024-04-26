'''
4. Classe AgendaTelefonica: 
Crie uma classe AgendaTelefonica que represente uma agenda telefônica com as 
seguintes características: 
Atributos privados: contatos. 
Métodos: 
__init__: Inicializa a agenda com uma lista vazia de contatos. 
adicionar_contato: Adiciona um novo contato à agenda (com nome, 
telefone e email). 
buscar_contato: Busca um contato na agenda por nome ou telefone. 
remover_contato: Remove um contato da agenda por nome ou 
telefone. 
mostrar_contatos: Imprime todos os contatos da agenda (nome, 
telefone e email).
'''
# Crie uma classe AgendaTelefonica que represente uma agenda telefônica com as seguintes características: 
class AgendaTelefonica:
# Atributos privados: contatos. 
# Métodos: 
# __init__: Inicializa a agenda com uma lista vazia de contatos. 
# adicionar_contato: Adiciona um novo contato à agenda (com nome, 
# telefone e email). 
    def __init__(self):
        self.__contatos = []
    
    # adicionar_contato: Adiciona um novo contato à agenda (com nome, 
    # telefone e email).
    def adicionar_contato(self, nome, fone, email):
        print("## adicionando contato à lista ##")
        nome = input("Informe o nome do contato: ")
        fone = input("Informe o fone do contato: ")
        email = input("informe o email do contato: ")
        