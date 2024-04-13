'''
3. Média de três números: 
Crie uma função que recebe três números como parâmetros e retorna a média 
aritmética dos três.
'''

while True:
    try:
        num1 = int(input("informe o primeiro número: "))
        num2 = int(input("informe o segundo número: "))
        num3 = int(input("informe o terceiro número: "))
        calcularMediaTresElementos(num1, num2, num3)
        break
    except ValueError:
        print("é necessário que os 3 elementos sejam números para calcular a média.")
        
    def calcularMediaTresElementos(x, y, z):
        media = (x + y + z) / 3
        print(media)