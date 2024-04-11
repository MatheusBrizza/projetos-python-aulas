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
    except ValueError and NameError:
        print("não pode calcular a média dos 3 elementos pois um ou mais elementos não foram informados.")
        
    def calcularMediaTresElementos(x, y, z):
        media = (x + y + z) / 3
        print(media)