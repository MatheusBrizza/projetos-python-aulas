'''
8. Palíndromo: 
Crie uma função que recebe uma string como parâmetro e verifica se a string é 
um palíndromo (uma palavra ou frase que se lê da mesma forma da frente para 
trás).
'''
def isPalindromo(string):
    if(string == string[::-1]):
        print("A palavra é palíndromo.")
    else:
        print("A palavra NÃO é palíndromo.")
    
palindromo = input("digite uma palavra: ")
isPalindromo(palindromo)
