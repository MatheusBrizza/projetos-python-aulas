'''
4. Crie um dicionário vazio e adicione pares chave-valor utilizando o 
método update(). O dicionário deve mapear nomes de animais para seus 
sons. 
'''
teclaParada = "-"
animaisDict = {}
while True:
    nome = input("digite o nome de um animal: ")
    if nome != teclaParada:
        som = input("digite o som do animal: ")
        animaisInputDict = {nome:som}
        animaisDict.update(animaisInputDict)
    else:
        break
print(animaisDict)

nome_verificar = input("veja se o nome está no dicionário: ")

if nome_verificar in animaisDict:
    print(f"o animal {nome_verificar} está no banco de dados. Seu som é {animaisDict.get(nome_verificar, "impossível verificar som")}")
else:
    print(f"não temos o animal {nome_verificar} nos nossos dados. {animaisDict.get(nome_verificar, "Impossível verificar som")}")