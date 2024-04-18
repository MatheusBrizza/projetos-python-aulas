'''
3. Classe Conta Bancária e Conta Poupança: 
Crie uma classe ContaBancaria com os 
atributos titular, saldo e taxa_juros. 
Crie uma classe ContaPoupanca que herde de ContaBancaria. 
Adicione à classe ContaPoupanca o atributo rendimento_mensal. 
Implemente 
métodos depositar(), sacar(), calcular_rendimento() e apresentar_saldo()
 nas classes ContaBancaria e ContaPoupanca. 
Crie objetos conta1 e conta_poupanca1 e chame os métodos 
adequados.
'''

# Crie uma classe ContaBancaria com os atributos titular, saldo e taxa_juros. 
class ContaBancaria:
    def __init__(self, titular, saldo, taxa_juros):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros

# Implemente métodos depositar(), sacar(), calcular_rendimento() e apresentar_saldo()
# nas classes ContaBancaria e ContaPoupanca. 
    def depositar(self, valor_depositado):
        if valor_depositado <= 0:
            print("É necessário selecionar um valor válido para depositar")
        else:
            self.saldo += valor_depositado
            print(f"Valor depositado! seu saldo atual é {self.saldo}")

    def sacar(self, valor_sacado):
        if valor_sacado <= 0:
            print("É necessário selecionar um valor válido para sacar")
        elif (self.saldo - valor_sacado) <= 0:
            print("Não é possível sacar valor maior que o saldo na conta")
        else:
            self.saldo -= valor_sacado
            print(f"Saque efetuado com sucesso! seu saldo atual é {self.saldo}")
    
    def apresentar_saldo(self):
        print(f"{self.titular} seu saldo é: {self.saldo}")
    
# Crie uma classe ContaPoupanca que herde de ContaBancaria. 
class ContaPoupanca(ContaBancaria):
    # Adicione à classe ContaPoupanca o atributo rendimento_mensal.
    def __init__(self, titular, saldo, taxa_juros, rendimento_mensal):
        super().__init__(titular, saldo, taxa_juros)
        self.rendimento_mensal = rendimento_mensal

# Implemente métodos depositar(), sacar(), calcular_rendimento() e apresentar_saldo()
# nas classes ContaBancaria e ContaPoupanca. 
    def calcular_rendimento(self):
        rendimento = self.saldo * self.rendimento_mensal
        self.saldo += rendimento
        print(f"seu dinheiro guardado rendeu {rendimento}, seu saldo agora é {self.saldo}")
    
# Crie objetos conta1 e conta_poupanca1 e chame os métodos adequados.
conta1 = ContaBancaria("matheus", 0, 1.2)
conta1.apresentar_saldo()
conta1.depositar(0)
conta1.depositar(2)
conta1.sacar(0)
conta1.sacar(3)
conta1.sacar(1)

conta_poupanca1 = ContaPoupanca("matheus", 1, 1.2, 0.06)
conta_poupanca1.calcular_rendimento()