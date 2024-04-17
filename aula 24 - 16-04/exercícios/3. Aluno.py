'''
3. Aluno 
Crie uma classe Aluno com os atributos: 
matricula: número da matrícula 
nome: nome do aluno 
curso: nome do curso 
Implemente os métodos getters e setters para: 
matricula 
nome 
curso 
Crie um objeto da classe Aluno e realize as seguintes operações: 
Acesse e imprima o número da matrícula do aluno. 
Altere o número da matrícula do aluno. 
Acesse e imprima o nome do aluno. 
Altere o nome do aluno. 
Acesse e imprima o nome do curso do aluno. 
Altere o nome do curso do aluno.
'''

# Crie uma classe Aluno com os atributos: 
# matricula: número da matrícula 
# nome: nome do aluno 
# curso: nome do curso 
class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        
# Implemente os métodos getters e setters para: 
# matricula 
# nome 
# curso 
    def get_matricula(self):
        return self.matricula
    
    def get_nome(self):
        return self.nome
    
    def get_curso(self):
        return self.curso
    
    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_curso(self, novo_curso):
        self.curso = novo_curso

# Crie um objeto da classe Aluno e realize as seguintes operações: 
aluno = Aluno(1123, "matheus", "TI")

# Acesse e imprima o número da matrícula do aluno. 
print(f"número matrícula: {aluno.get_matricula()}")

# Altere o número da matrícula do aluno.
aluno.set_matricula(9876)
print(f"novo número matrícula: {aluno.get_matricula()}")

# Acesse e imprima o nome do aluno. 
print(f"nome aluno: {aluno.get_nome()}")

# Altere o nome do aluno.
aluno.set_nome("joão")
print(f"novo nome aluno: {aluno.get_nome()}")

# Acesse e imprima o nome do curso do aluno. 
print(f"nome curso: {aluno.get_curso()}")

# Altere o nome do curso do aluno.
aluno.set_curso("ADM")
print(f"nome curso: {aluno.get_curso()}")
