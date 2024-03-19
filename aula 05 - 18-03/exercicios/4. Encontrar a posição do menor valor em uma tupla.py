# 4. Encontrar a posição do menor valor em uma tupla: 
# Modifique o código para encontrar a posição (índice) do menor valor na tupla.

tuplaNumerico = (2690, 573, 516, 8046, 43, 269)

indiceMenorNumero = tuplaNumerico.index(min(tuplaNumerico))
print(f"A posição do menor número da tupla é: {indiceMenorNumero}")