# 5. Encontrar a posição do maior valor em uma tupla: 
# Modifique o código para encontrar a posição (índice) do maior valor na tupla.

tuplaNumerico = (2690, 573, 516, 8046, 43, 269)

indiceMaiorNumero = tuplaNumerico.index(max(tuplaNumerico))
print(f"A posição do maior número da tupla é: {indiceMaiorNumero}")