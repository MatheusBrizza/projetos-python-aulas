'''
5: Sistema de Banco 
Crie as classes: 
Conta (classe base com atributos titular, saldo e 
métodos depositar(), sacar() e consultar_saldo()). 
ContaPoupanca (herda de Conta, com taxa de juros e método render_juros()). 
ContaCorrente (herda de Conta, com limite de cheque especial). 
Crie contas para diferentes clientes: 
Conta Poupança e Conta Corrente. 
Realize operações: 
Deposite e saque valores em cada conta. 
Consulte o saldo de cada conta. 
Renda juros na Conta Poupança (se aplicável). 
Utilize o cheque especial da Conta Corrente (se disponível).
'''

# Conta (classe base com atributos titular, saldo e 
# métodos depositar(), sacar() e consultar_saldo()). 
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        
    def depositar(self, valor_depositado):
        if valor_depositado <= 0:
            print("valor inválido.")
        else:
            self.saldo += valor_depositado
            print(f"depósito realizado com sucesso! seu saldo atual é R${self.saldo:.2f}")
    
    def sacar(self, valor_sacado):
        if valor_sacado <= 0:
            print("valor inválido!")
        elif self.saldo < valor_sacado:
            print("") 
        else:
            self.saldo -= valor_sacado
            print(f"saque realizado com sucesso! seu saldo atual é R${self.saldo:.2f}")
    
    def consultar_saldo(self):
        print(f"seu saldo é de R${self.saldo:.2f}")

# ContaPoupanca (herda de Conta, com taxa de juros e método render_juros()). 
class ContaPoupanca(Conta):
    def __init__(self, titular, taxa_juros):
        super().__init__(titular)
        self.taxa_juros = taxa_juros
        
    def render_juros(self):
        rendimento = self.saldo * self.taxa_juros
        self.saldo += rendimento
        print(f"seu dinheiro guardado rendeu {rendimento}, seu saldo agora é R${self.saldo:.2f}")
        
    def sacar(self, valor_sacado):
        super().sacar(valor_sacado)
        if self.saldo < valor_sacado:
            print("saldo insuficiente!")
        
        
# ContaCorrente (herda de Conta, com limite de cheque especial). 
class ContaCorrente(Conta):
    def __init__(self, titular, limite_cheque_especial):
        super().__init__(titular)
        self.limite_cheque_especial = limite_cheque_especial
        
    def sacar(self, valor_sacado):
        super().sacar(valor_sacado)
        if self.saldo < valor_sacado:
            resto = self.saldo - valor_sacado
            self.saldo = 0
            self.limite_cheque_especial += resto
            print(f"entrou no cheque especial. seu saldo é de R${self.limite_cheque_especial:.2f}")
            
    
# Crie contas para diferentes clientes: 
# Conta Poupança e Conta Corrente.
conta_poupanca = ContaPoupanca("fulano", 0.06)
conta_corrente = ContaCorrente("siclano", 500)
# Realize operações: 
# Deposite e saque valores em cada conta.
print("conta corrente")
print("depósito 1")
conta_corrente.depositar(0)
print("depósito 2")
conta_corrente.depositar(2)
print("saque 1")
conta_corrente.sacar(-1)
print("saque 2")
conta_corrente.sacar(1)
print("saque 3")
conta_corrente.sacar(3)
print("")
print("conta poupança")
print("depósito 1")
conta_poupanca.depositar(-1)
print("depósito 2")
conta_poupanca.depositar(2)
print("saque 1")
conta_poupanca.sacar(0)
print("saque 2")
conta_poupanca.sacar(1)
print("saque 3")
conta_poupanca.sacar(3)
# Consulte o saldo de cada conta.
print("conta corrente")
conta_corrente.consultar_saldo()
print("conta poupanca")
conta_poupanca.consultar_saldo()
# Renda juros na Conta Poupança (se aplicável).
conta_poupanca.render_juros()
# Utilize o cheque especial da Conta Corrente (se disponível).
# já testado em saque 3 da conta_corrente