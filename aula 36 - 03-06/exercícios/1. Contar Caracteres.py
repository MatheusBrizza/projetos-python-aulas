'''
1. Contar Caracteres
Crie uma função que conte o número de caracteres (incluindo espaços) em um campo Text. 
Teste a função com diferentes textos, incluindo espaços em branco e caracteres especiais.
'''

import tkinter as tk # Importa as funções de tkinter para o projeto e apelida como tk 

def contar_caracteres(): # Cria a função para contar caracteres
    texto = caixa_texto.get(1.0, tk.END) # Pega tudo escrito da caixa de texto criada na linha 18 do começo ao fim e salva em uma variável chamada texto
    numero_caracteres = len(texto) - 1 # Pega a variável texto acima e calcula o tamanho dela subtraíndo 1 que seria um caracter inexistente que pula para próxima linha e salva o resultado numa variável chamada numero_caracteres
    resultado_label.config(text=f"O texto possui {numero_caracteres} caracteres.") # Pega a label criada na linha 24 e muda o texto vazio para "O texto possui {numero_caracteres} caracteres." adicionando o valor da variável numero_caracteres da linha acima.


janela = tk.Tk() # Cria a tela principal
janela.title("Exercício 1 - contar caracteres") # Nomeia a tela principal como Exercício 1 - contar caracteres

caixa_texto = tk.Text(janela) # Cria uma caixa de texto
caixa_texto.pack(padx=10, pady=5) # Anexa a caixa de texto à tela inicial 

botao_contar_caracteres = tk.Button(janela, text="Contar Caracteres", command=contar_caracteres) # Cria botão e aplica a função de contar caracteres quando pressionado
botao_contar_caracteres.pack() # Anexa o botão à tela principal

resultado_label = tk.Label(janela, text="") # Cria uma label vazia
resultado_label.pack() # Anexa a label à tela principal

janela.mainloop() # "trava" a execução da janela atual usando um event loop fazendo com que não feche assim que abrir e só termine a execução quando apretarmos para fechar a janela