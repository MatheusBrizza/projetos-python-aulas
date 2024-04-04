#1. Verificação de Elemento:
#Crie um conjunto com os nomes de seus amigos.
#Peça ao usuário para digitar um nome.
#Verifique se o nome está no conjunto e informe o usuário se ele é seu amigo ou não.
amigos = {"Ana", "João", "Pedro", "Maria"}

nome = input("Digite o nome de um amigo: ")

if nome in amigos:
  print(f"{nome} é meu amigo!")
else:
  print(f"{nome} não é meu amigo.")
