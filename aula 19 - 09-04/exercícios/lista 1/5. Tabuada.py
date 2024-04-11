'''
5. Tabuada: 
Crie uma função que recebe um número como parâmetro e imprime a tabuada 
de 1 a 10 desse número.
'''
def calcularTabuadaValorInformado(x):
    for i in range(1, 11):
        resultado = x * i
        print(resultado)

try:
    num = int(input("informe o primeiro número: "))
    calcularTabuadaValorInformado(num)
except NameError and ValueError:
    print("não pode calcular a tabuada porque não foi passado nenhum número")