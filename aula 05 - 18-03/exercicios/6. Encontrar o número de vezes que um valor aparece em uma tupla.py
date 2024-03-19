# 6. Encontrar o número de vezes que um valor aparece em uma tupla: 
# Modifique o código para contar o número de vezes que um determinado valor 
# aparece na tupla.

tuplaNumerico = (2690, 573, 516, 8046, 43, 269)
valorAProcurar = int(input("Digite um número para ver quantas vezes aparece na tupla: "))
quantidadeVezesNumeroAparece = tuplaNumerico.count(valorAProcurar)
print(f"o valor {valorAProcurar} aparece {quantidadeVezesNumeroAparece} vez(es) na tupla")