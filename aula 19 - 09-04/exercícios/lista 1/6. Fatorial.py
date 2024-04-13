'''
6. Fatorial: 
Crie uma função que recebe um número como parâmetro e retorna o fatorial 
desse número.
'''
numero = int(input("Digite um número para calcular o seu fatorial: "))

def fatorial(numero):
    if numero == 0:
        print(f"Fatorial({numero}) = 1")
        return 1
    else:
        resultado = numero * fatorial(numero - 1)
        print(f"Fatorial({numero}) = {resultado}")
        return resultado
    
fatorial(numero)