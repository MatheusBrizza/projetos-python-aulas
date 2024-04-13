'''
9. Contador de vogais: 
Crie uma função que recebe uma string como parâmetro e retorna o número de 
vogais na string.
'''
palavra = input("Digite uma palavra: ")

def contadorVogais(palavra):
    while True:
        if palavra == "":
            print("não é possível contar vogais sem informar uma palavra.")
            break
        contador = 0
        for i in palavra:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                contador += 1
            else:
                continue
        if contador == 0:
            print("não tinha vogais nesta palavra")
            break
        else:
            print(f"O total de vogais na palavra {palavra} é : {str(contador)}")
            break
        
contadorVogais(palavra)