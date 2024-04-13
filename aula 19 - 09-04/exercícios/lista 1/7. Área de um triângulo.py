'''
7. Área de um triângulo: 
Crie uma função que recebe a base e a altura de um triângulo como 
parâmetros e retorna a área do triângulo.
'''
def calcularAreaTriangulo(base, altura):
    area = base * altura
    print(area)
    
while True:
    try:
        num1 = int(input("informe o valor da base do triângulo: "))
        num2 = int(input("informe o valor da altuda do triângulo: "))
        calcularAreaTriangulo(num1, num2)
        break
    except ValueError:
        print("é necessário informar 2 números para calcular a área do triângulo")