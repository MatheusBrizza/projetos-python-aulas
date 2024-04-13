'''
4. Par ou ímpar: 
Crie uma função que recebe um número como parâmetro e retorna True se o 
número for par e False se for ímpar.
'''

def isPar(x):
    if x % 2 == 0:
        print(f"este número é par? {True}")
    else:
        print(f"este número é par? {False}")

try:
    num = int(input("informe um número para verificar se é par ou ímpar: "))
    isPar(num)
except ValueError:
    print("é necessário que digite um número para verificar se é par ou ímpar")