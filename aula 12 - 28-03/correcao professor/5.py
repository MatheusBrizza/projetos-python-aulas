#5Ordenação de Elementos:
#Crie um conjunto com números de 1 a 10.
#Ordene os elementos do conjunto em ordem crescente e decrescente e imprima as listas ordenadas.


numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Ordenação crescente
numeros_crescente = sorted(numeros)
print(f"Números em ordem crescente: {numeros_crescente}")

# Ordenação decrescente
numeros_decrescente = sorted(numeros, reverse=True)
print(f"Números em ordem decrescente: {numeros_decrescente}")

