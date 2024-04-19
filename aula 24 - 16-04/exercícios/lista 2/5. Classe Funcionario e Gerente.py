'''
5. Classe Funcionario e Gerente: 
Crie uma classe Funcionario com os 
atributos nome, cargo, salario e data_admissao. 
Crie uma classe Gerente que herde de Funcionario. 
Adicione à classe Gerente os atributos bonus e area_gerenciada. 
Implemente 
métodos calcular_pagamento(), bonificar(), promover() e apresentar_dados()
nas classes Funcionario e Gerente. 
Crie objetos funcionario1 e gerente1 e chame os métodos adequados.
'''
# Crie uma classe Funcionario com os 
# atributos nome, cargo, salario e data_admissao. 
class Funcionario:
    def __init__(self, nome, cargo, salario, data_admissao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao

    # Implemente métodos calcular_pagamento(), bonificar(), promover() e apresentar_dados()
    # nas classes Funcionario e Gerente.
    def calcular_pagamento(self):
        print(f"salário do funcionário é R${self.salario:.2f}")

    def promover(self):
        if self.cargo == "gerente":
            print("funcionário não pode ser promovido")
        else:
            self.cargo = "gerente"
            print(f"funcionário {self.nome} foi promovido para {self.cargo}")
    
    def apresentar_dados(self):
        print(f"nome funcionário: {self.nome}, cargo: {self.cargo}, salário: {self.salario}, data_admissão: {self.data_admissao}")
        
# Crie uma classe Gerente que herde de Funcionario. 
# Adicione à classe Gerente os atributos bonus e area_gerenciada. 
class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, data_admissao, bonus, area_gerenciada):
        super().__init__(nome, cargo, salario, data_admissao)
        self.bonus = bonus
        self.area_gerenciada = area_gerenciada

            
    # Implemente métodos calcular_pagamento(), bonificar(), promover() e apresentar_dados()
    # nas classes Funcionario e Gerente. 
    def bonificar(self):
        bonus_mensal = self.salario + self.bonus
        print(f"salário do mês com bônus será de R$ {bonus_mensal:.2f}")

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"bônus do mês: {self.bonus}, área gerenciada: {self.area_gerenciada}")
        
# Crie objetos funcionario1 e gerente1 e chame os métodos adequados.
funcionario1 = Funcionario("matheus", "faxineiro", 1000, "07/06/2018")
funcionario1.apresentar_dados()
funcionario1.calcular_pagamento()
funcionario1.promover()
funcionario1.promover()
gerente1 = Gerente("lucas", "gerente", 1500, "25/02/2016", 300, "TI")
gerente1.bonificar()
gerente1.promover()
gerente1.apresentar_dados()
