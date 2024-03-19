# 7. Verificar se um valor está presente em uma tupla: 
# Modifique o código para verificar se um determinado valor está presente na tupla.

tuplaNumerico = (2690, 573, 516, 8046, 43, 269)
numeroAProcurar = int(input("Digite um número para ver se aparece na tupla: "))
quantidadeVezesNumeroAparece = tuplaNumerico.count(numeroAProcurar)
if quantidadeVezesNumeroAparece == 0:
    print(f"O número {numeroAProcurar} não está na tupla")
else:
    print(f"O número {numeroAProcurar} está presente na tupla")