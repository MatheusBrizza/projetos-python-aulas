# Crie um jogo de adivinhação onde o usuário tenta adivinhar um número secreto 
# usando while

numero = int(input("Digite um número: "))

while numero != 5:
    print("Você errou!")
    numero = int(input("Digite um número: "))
print("Você acertou!")