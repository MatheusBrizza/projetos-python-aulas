'''
3. Salvar Texto em Arquivo:
Crie uma função que permita ao usuário salvar o conteúdo do campo Text em um arquivo de 
texto. 
Exiba uma mensagem de sucesso ou erro após a operação.
'''
import tkinter as tk # importa a biblioteca tkinter e apelida como tk
import os # importa a biblioteca os que interage com sistema operacional

def salvar_texto(): # função para salvar texto em um arquivo no computador 
    try: # início de try que irá tentar uma proção do código e se falhar não irá parar o programa 
        arquivo_nome = caixa_nome_arquivo.get() # irá pegar tudo escrito na caixa de texto da linha 35 e irá salvar numa variável
        if not arquivo_nome: # condicional que verifica se a variável acima está em branco 
            raise Exception("Nome de arquivo inválido") # se condição for atendida ele lançará um erro com a mensagem "Nome de arquivo inválido"  
        
        nome, extensao = os.path.splitext(arquivo_nome) # Separa nome do arquivo e a extensão dele (caso tenha) Ex: teste.txt

        if not extensao: #condicional que verifica se a variável extensão está em branco
            arquivo_nome = nome + ".docx" # se condição for atendida ela mudará o nome do arquivo como nome + extensão ".docx", ou seja estará automaticamente declarando o arquivo como o tipo ".docx"
 
        with open(arquivo_nome, "w") as arquivo: # abre o arquivo no modo escrita
            arquivo.write(caixa_texto.get(1.0, tk.END)) # escreve o conteúdo do campo de texto da linha 30 no arquivo aberto.
        label_status.config(text=f"Arquivo salvo em {arquivo_nome}") # insere uma mensagem de sucesso no label da linhha 36.
        
    except Exception as e: # caso o bloco dentro do try dê erro, irá impedir o programa de fechar e fará o que segue abaixo dele. 
        label_status.config(text=f"Erro ao salvar: {e}") # irá apresentar uma mensagem de erro no label da linha 36.

janela = tk.Tk() # Cria a tela principal
janela.title("Salvar Texto em Arquivo") # Nomeia a tela principal como "Salvar texto em arquivo"

caixa_texto = tk.Text(janela) # Cria uma caixa de texto
caixa_texto.pack(padx=10, pady=5) # Anexa a caixa de texto à tela inicial 

caixa_nome_arquivo = tk.Entry(janela) # Cria uma caixa de texto pequena
caixa_nome_arquivo.pack(pady=5) # Anexa a caixa de texto pequena à tela inicial

label_status = tk.Label(janela, text="") # Cria uma label vazia
label_status.pack() # Anexa a label à tela principal

botao_salvar_arquivo = tk.Button(janela, text="Salvar Texto", command=salvar_texto)# Cria botão e aplica a função de contar letras quando pressionado
botao_salvar_arquivo.pack() # Anexa o botão à tela principal


janela.mainloop()