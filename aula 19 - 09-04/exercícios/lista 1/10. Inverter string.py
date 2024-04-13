'''
10. Inverter string: 
Crie uma função que recebe uma string como parâmetro e retorna a string 
invertida.
'''
def inverterString(string):
    if len(string) > 1:
        stringInvertida = string[::-1]
        print(stringInvertida)
    else:
        print("não é possível inverter uma string com apenas 1 elemento.")
    
palavra = input("digite uma palavra: ")
inverterString(palavra)