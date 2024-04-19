'''
1. Classe Pessoa e Aluno:
Crie uma classe Pessoa com os atributos nome, idade e sexo.
Crie uma classe Aluno que herde da classe Pessoa.
Adicione à classe Aluno o atributo matricula.
Implemente métodos get_matricula(), set_matricula(), apresentar() nas 
classes Pessoa e Aluno. 
Crie objetos pessoa1 e aluno1 e chame os métodos adequados.
'''
# Crie uma classe Pessoa com os atributos nome, idade e sexo. 
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo =sexo

    # Implemente métodos get_matricula(), set_matricula(), apresentar() nas classes Pessoa e Aluno. 
    def apresentar(self):
        print(f"Olá meu nome é {self.nome}")
    
# Crie uma classe Aluno que herde da classe Pessoa.
class Aluno(Pessoa):
    # Adicione à classe Aluno o atributo matricula.
    def __init__(self, nome, idade, sexo, matricula):
        super().__init__(nome, idade, sexo)
        self.matricula = matricula

    # Implemente métodos get_matricula(), set_matricula(), apresentar() nas classes Pessoa e Aluno. 
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula
    
    # Crie objetos pessoa1 e aluno1 e chame os métodos adequados.
pessoa1 = Pessoa("joão", 48, "Macho")
pessoa1.apresentar()

aluno1 = Aluno("João", 48, "Macho", 15387)
print(f"matrícula aluno: {aluno1.get_matricula()}")
aluno1.set_matricula(89746)
print(f"nova matrícula aluno: {aluno1.get_matricula()}")
