'''
5. Tabuada: 
Crie uma função que recebe um número como parâmetro e imprime a tabuada 
de 1 a 10 desse número.
'''
def calcularTabuadaValorInformado(x):
    for i in range(1, 11):
        resultado = x * i
        print(f"{x} * {i} = {resultado}")

try:
    num = int(input("Digite um número para calcular sua tabuada: "))
    calcularTabuadaValorInformado(num)
except ValueError:
    print("é necessário informar 1 número para calcular sua tabuada")