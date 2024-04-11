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
    except ValueError and NameError:
        print("não pode averiguar qual o maior por falta de um dos elementos")