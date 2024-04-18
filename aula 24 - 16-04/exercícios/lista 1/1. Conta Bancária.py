'''
1. Conta Bancária 
Crie uma classe conta bancaria com os atributos: 
titular: nome do titular da conta 
saldo: saldo da conta 
Implemente os métodos getters e setters para: 
titular 
saldo 
Crie um objeto da classe ContaBancaria e realize as seguintes operações: 
Acesse e imprima o nome do titular da conta. 
Altere o nome do titular da conta. 
Acesse e imprima o saldo da conta. 
Deposite um valor na conta. 
Acesse e imprima o novo saldo da conta.
'''
# Crie uma classe conta bancaria com os atributos: 
# titular: nome do titular da conta 
# saldo: saldo da conta 
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

# Implemente os métodos getters e setters para: 
# titular 
# saldo 
        
    def get_titular(self):
        return self.titular
    
    def get_saldo(self):
        return self.saldo
    
    def set_titular(self, novo_titular):
        self.titular = novo_titular
    
    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

# Crie um objeto da classe ContaBancaria e realize as seguintes operações: 
contaBancaria = ContaBancaria("matheus", 0)

# Acesse e imprima o nome do titular da conta. 
print(f"nome titular: {contaBancaria.get_titular()}")

# Altere o nome do titular da conta. 
contaBancaria.set_titular("lucas")
print(f"nome novo titular: {contaBancaria.get_titular()}")

# Acesse e imprima o saldo da conta. 
print(f"saldo na conta: {contaBancaria.get_saldo()}")

# Deposite um valor na conta. 
contaBancaria.set_saldo(100)

# Acesse e imprima o novo saldo da conta.
print(f"saldo na conta: {contaBancaria.get_saldo()}")