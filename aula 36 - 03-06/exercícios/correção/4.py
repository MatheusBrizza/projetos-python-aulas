import tkinter as tk
import os
from tkinter import filedialog

def carregar_texto():
    
    try: # Tenta executar o código dentro deste bloco. Se algo der errado, o bloco `except` será executado.
        arquivo_nome = filedialog.askopenfilename( # Abre uma janela para o usuário selecionar um arquivo de texto.# Retorna o nome do arquivo selecionado ou `None` se nenhum for selecionado.

            filetypes=[("Arquivos de texto", "*.txt")],
        )
        if arquivo_nome:# Se um arquivo foi selecionado...
            if not os.path.exists(arquivo_nome):
                raise Exception("Arquivo não encontrado")
                # Verifica se o arquivo existe.
                # Se não existir, levanta uma exceção com a mensagem "Arquivo não encontrado".

            if os.path.isdir(arquivo_nome):
                raise Exception("Caminho especificado é um diretório")
                # Verifica se o caminho selecionado é um diretório (pasta).
                # Se for um diretório, levanta uma exceção com a mensagem "Caminho especificado é um diretório".

            with open(arquivo_nome, "r") as arquivo:#O modo de escrita "r" (abreviação de "read") se refere a um modo específico de abrir um arquivo para leitura de dados. 
                 # Abre o arquivo no modo leitura ("r").
                 # O bloco `with` garante que o arquivo seja fechado automaticamente após o término do bloco.
                
                texto.delete(1.0, tk.END)
                # Apaga todo o conteúdo da caixa de texto `texto`.
                texto.insert(tk.END, arquivo.read())
                 # Insere o conteúdo do arquivo aberto na caixa de texto `texto`.
            mensagem_status.config(text=f"Texto carregado de '{arquivo_nome}'")
            # Atualiza a mensagem de status para informar que o Texto carregado de .
    except Exception as e:
        # Se algo der errado durante a execução do código dentro do bloco `try`, 
    # a exceção será capturada e armazenada na variável `e`.

        mensagem_status.config(text=f"Erro ao carregar: {e}")
        # Atualiza a mensagem de status para informar que ocorreu um erro e exibe a mensagem de erro capturada.

# Criar a janela principal
janela = tk.Tk()
janela.title("Criador de Arquivos TXT")

# Criar o widget Text
texto = tk.Text(janela, width=60, height=20)
texto.pack(pady=5)

# Criar frame para botão de carregar
frame_salvar_carregar = tk.Frame(janela)
frame_salvar_carregar.pack(pady=5)

#carregar Texto de Arquivo
botao_carregar_texto = tk.Button(frame_salvar_carregar, text="Carregar Texto", command=carregar_texto)
botao_carregar_texto.pack(pady=5)


# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")
mensagem_status.pack(pady=5)
resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=5)

# Executar o loop principal da interface
janela.mainloop()