'''
2. Contar Letras: 
Crie uma função que conte o número de letras (A-Z, a-z) em um campo Text. 
Teste a função com diferentes textos, incluindo espaços em branco, números, pontuação e 
caracteres especiais. 
'''

import tkinter as tk # importa biblioteca tkinter e apelida como tk

def contar_letras(): # Cria a função de contar letras
    numero_letras = 0 # cria uma variável chamada numero_letras e dá o valor pra ela de 0
    texto = caixa_texto.get(1.0, tk.END) # Pega tudo escrito da caixa de texto criada na linha 22 do começo ao fim e salva em uma variável chamada texto
    for char in texto: # loop for para percorrer todo texto da variável texto
        if char.isalpha(): # condição para verificar o texto e identificar apenas as letras 
            numero_letras += 1 # passando a condição acima aumenta em 1 o valor da variável numero_letras
    resultado_label.config(text=f"O texto possui {numero_letras} caracteres.") # Pega a label criada na linha 29 e muda o texto vazio para "O texto possui {numero_caracteres} caracteres." adicionando o valor da variável numero_caracteres da linha acima.


janela = tk.Tk() # Cria a tela principal
janela.title("Exercício 2 - contar letras") # Nomeia a tela principal como Exercício 2 - contar letras

caixa_texto = tk.Text(janela) # Cria uma caixa de texto
caixa_texto.pack(padx=10, pady=5) # Anexa a caixa de texto à tela inicial 

botao_contar_caracteres = tk.Button(janela, text="Contar Caracteres", command=contar_letras) # Cria botão e aplica a função de contar letras quando pressionado
botao_contar_caracteres.pack() # Anexa o botão à tela principal

resultado_label = tk.Label(janela, text="") # Cria uma label vazia
resultado_label.pack() # Anexa a label à tela principal

janela.mainloop() # "trava" a execução da janela atual usando um event loop fazendo com que não feche assim que abrir e só termine a execução quando apretarmos para fechar a janela