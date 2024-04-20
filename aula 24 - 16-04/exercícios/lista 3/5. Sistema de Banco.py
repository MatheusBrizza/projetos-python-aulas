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
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor_depositado):
        if valor_depositado <= 0:
            print("valor inválido.")
        else:
            self.saldo += valor_depositado
    
    def sacar(self, valor_sacado):
        if self.saldo < valor_sacado:
            print("saldo insuficiente!")
        elif valor_sacado <= 0:
            print("valor inválido")
        else:
            self.saldo -= valor_sacado
    
    def consultar_saldo(self):
        print(f"seu saldo é de R${self.saldo}")

# ContaPoupanca (herda de Conta, com taxa de juros e método render_juros()). 
class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_juros):
        super().__init__(titular, saldo)
        self.taxa_juros = taxa_juros
        
    def render_juros(self):
        rendimento = self.saldo * self.taxa_juros
        self.saldo += rendimento
        print(f"seu dinheiro guardado rendeu {rendimento}, seu saldo agora é {self.saldo}")
        
# ContaCorrente (herda de Conta, com limite de cheque especial). 
class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite_cheque_especial):
        super().__init__(titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial
        