'''
3: Funcionários em uma Empresa 
Crie as classes: 
Funcionario (classe base com atributos nome e salario). 
Gerente (herda de Funcionario, com bônus e método adicionar_funcionario()). 
Vendedor (herda de Funcionario, com comissão e 
método calcular_comissao()). 
Crie uma lista de funcionários: 
Inclua objetos de Gerente e Vendedor. 
Mostre: 
O nome e o salário de cada funcionário. 
O bônus do gerente (se houver). 
A comissão do vendedor (se houver). 
Adicione um funcionário: 
Utilize o método adicionar_funcionario() do gerente para incluir um novo 
funcionário na lista.
'''

# Crie as classes: 
# Funcionario (classe base com atributos nome e salario). 
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def get_nome(self):
        print(self.nome)
    
    def get_salario(self):
        print(self.salario)

# Gerente (herda de Funcionario, com bônus e método adicionar_funcionario()). 
class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus
    
    def adicionar_funcionario(self):
        funcionario1 = Funcionario("beltrano", 1000)
        print("novo funcionário criado")
        return funcionario1
    
    def calcular_bonus(self):
        valor_bonus = self.salario * self.bonus
        print(f"valor do bônus é R${valor_bonus}")
    
# Vendedor (herda de Funcionario, com comissão e método calcular_comissao()).
class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao
        
    def calcular_comissao(self):
        valor_comissao = self.salario * self.comissao
        print(f"valor da comissão é R${valor_comissao}")

# Crie uma lista de funcionários: 
# Inclua objetos de Gerente e Vendedor. 
listaFuncionarios = []
gerente1 = Gerente("fulano", 1500, 0.4)
vendedor1 = Vendedor("siclano", 1200, 0.2)
listaFuncionarios.append(gerente1)
listaFuncionarios.append(vendedor1)
# Mostre: 
# O nome e o salário de cada funcionário. 
# O bônus do gerente (se houver). 
# A comissão do vendedor (se houver).
for i in range(0, len(listaFuncionarios)):
    listaFuncionarios[i].get_nome()
    listaFuncionarios[i].get_salario()
listaFuncionarios[0].calcular_bonus()
listaFuncionarios[1].calcular_comissao()
# Adicione um funcionário: 
# Utilize o método adicionar_funcionario() do gerente para incluir um novo 
# funcionário na lista.
funcionario1 = listaFuncionarios[0].adicionar_funcionario()
listaFuncionarios.append(funcionario1)
for i in range(0, len(listaFuncionarios)):
    listaFuncionarios[i].get_nome()