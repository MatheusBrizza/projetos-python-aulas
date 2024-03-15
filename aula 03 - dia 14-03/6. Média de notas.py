# Leia as notas de N alunos e calcule a média da turma usando while.
repetir = ""
alunos = []
somaNotas = 0
while repetir != "n":
    aluno = input("Digite o nome do aluno: ")
    nota = int(input("Digite a nota do aluno: "))
    alunos.append(aluno)
    repetir = input("Deseja adicionar outro aluno?(s/n) ")
    somaNotas += nota
media = somaNotas / len(alunos)
print(f"a média da turma é: {somaNotas} / {len(alunos)} = {media}")