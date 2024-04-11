'''
10. Inverter string: 
Crie uma função que recebe uma string como parâmetro e retorna a string 
invertida.
'''
def inverterString(string):
    stringInvertida = string[::-1]
    print(stringInvertida)
    
palavra = input("digite uma palavra: ")
inverterString(palavra)