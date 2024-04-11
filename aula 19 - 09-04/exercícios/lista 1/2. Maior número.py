'''
2. Maior número: 
Crie uma função que recebe dois números como parâmetros e retorna o maior 
entre eles.
'''

def maiorEntreDuasVariaveis(x, y):
    if x > y:
        print(f"{x} é maior que {y}")
    elif x < y:
        print(f"{y} é maior que {x}")
    elif x == y:
        print(f"são o mesmo valor")
    else:
        print("como chegou aqui?")

while True:
    try:
        num1 = int(input("informe o primeiro número: "))
        num2 = int(input("informe o segundo número: "))
        maiorEntreDuasVariaveis(num1, num2)
        break
    except ValueError and NameError:
        print("não pode averiguar qual o maior por falta de um dos elementos")
        