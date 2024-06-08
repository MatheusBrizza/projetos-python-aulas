'''
4.Carregar Texto de Arquivo: 
Crie uma função que permita ao usuário carregar o conteúdo de um arquivo de texto para o 
campo Text. 
Exiba o conteúdo do arquivo no campo Text.
'''
import tkinter as tk # importa a biblioteca tkinter e apelida como tk
import os # importa a biblioteca os que interage com sistema operacional
from tkinter import filedialog #Importa o módulo filedialog da biblioteca tkinter. Este módulo fornece funções para criar caixas de diálogo que permitem aos usuários selecionar arquivos ou diretórios.

def carregar_texto(): # função para carregar um arquivo externo iniciada 
    
    try: # início de try que irá tentar uma proção do código e se falhar não irá parar o programa
        arquivo_nome = filedialog.askopenfilename( # Abre uma janela para o usuário selecionar um arquivo do tipo ".docx".
            filetypes=[("Arquivos de texto", "*.docx")], # especificando que queremos apenas arquivos do tipo ".docx"
        )
        if arquivo_nome:# condicional para verificar se selecionou um arquivo na parte anterior
            if not os.path.exists(arquivo_nome): # condicional para verificar se caminho do arquivo selecionado existe
                raise Exception("Arquivo não encontrado") # Se condição for atendida então lançará um erro com a mensagem "Arquivo não encontrado".

            if os.path.isdir(arquivo_nome): # condicional para verificar se o aquivo caminho selecionado é uma pasta 
                raise Exception("Caminho especificado é um diretório") # Se condição for atendida então lançará um erro com a mensagem "Caminho especificado é um diretório".

            with open(arquivo_nome, "r") as arquivo: # Abre o arquivo no modo leitura ("r").                
                caixa_texto.delete(1.0, tk.END) # Deixa a caixa de texto da linha 38 em branco.
                caixa_texto.insert(tk.END, arquivo.read()) # Insere o conteúdo do arquivo aberto na caixa de texto da linha 38.
            label_status.config(text=f"Texto carregado de '{arquivo_nome}'") # Insere uma mensagem de sucesso informando no label da linha 40.
    except Exception as e: # caso o bloco dentro do try dê erro, irá impedir o programa de fechar e fará o que segue abaixo dele.
        label_status.config(text=f"Erro ao carregar: {e}") # irá apresentar uma mensagem de erro no label da linha 40.

janela = tk.Tk() # Cria a tela principal
janela.title("Salvar Texto em Arquivo") # Nomeia a tela principal como "Salvar texto em arquivo"

caixa_texto = tk.Text(janela) # Cria uma caixa de texto
caixa_texto.pack(padx=10, pady=5) # Anexa a caixa de texto à tela inicial 

label_status = tk.Label(janela, text="") # Cria uma label vazia
label_status.pack() # Anexa a label à tela principal

botao_salvar_arquivo = tk.Button(janela, text="Carregar arquivo", command=carregar_texto)# Cria botão e aplica a função de contar letras quando pressionado
botao_salvar_arquivo.pack() # Anexa o botão à tela principal

janela.mainloop()