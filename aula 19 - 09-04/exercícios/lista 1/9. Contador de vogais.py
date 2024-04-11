'''
9. Contador de vogais: 
Crie uma função que recebe uma string como parâmetro e retorna o número de 
vogais na string.
'''
palavra = input("Digite uma palavra: ")

def contadorVogais(palavra):
    contador = 0
    for i in palavra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador += 1
        else:
            continue
    if contador == 0:
        print("não tinha vogais")
    else:
        print(f"O total de vogais é : {str(contador)}")
        
contadorVogais(palavra)