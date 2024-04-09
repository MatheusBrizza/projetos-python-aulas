'''
1. Crie um dicionário que mapeie nomes de frutas para seus preços. Em 
seguida, utilize os métodos keys(), values() e items() para imprimir as 
chaves, valores e pares chave-valor do dicionário, respectivamente.
'''
dicionarioFrutas = {"banana":35, "maca": 15, "abacaxi": 20}

for chave in dicionarioFrutas.keys():
    print(f"chave: {chave}")
    
for valor in dicionarioFrutas.values():
    print(f"valor: {valor}")

for c, v in dicionarioFrutas.items():
    print(f"chave: {c}, valor: {v}")