'''
4. Par ou ímpar: 
Crie uma função que recebe um número como parâmetro e retorna True se o 
número for par e False se for ímpar.
'''

def isPar(x):
    if x % 2 == 0:
        print(True)
    else:
        print(False)

try:
    num = int(input("informe o primeiro número: "))
    isPar(num)
except NameError and ValueError:
    print("não pode fazer a verificação porque não foi passado nenhum número")