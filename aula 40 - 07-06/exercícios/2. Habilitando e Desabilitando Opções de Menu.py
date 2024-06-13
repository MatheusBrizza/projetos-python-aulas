'''
Exercício 2: Habilitando e Desabilitando Opções de Menu 
• Crie um menu principal com submenus para "Novo" e "Abrir". 
• Crie uma variável para controlar o estado das opções (ativadas ou desativadas). 
• Adicione um item ao menu para alternar o estado das opções. 
• Utilize o estado da variável para ativar ou desativar as opções de "Novo" e "Abrir" 
dinamicamente.
'''
import tkinter as tk

# Define a função para alternar o estado das opções de arquivo
def alternar_opcoes_arquivo():
   
    global esta_arquivo_aberto  # Declara que a variável `esta_arquivo_aberto` é global dentro da função.

    esta_arquivo_aberto = not esta_arquivo_aberto  # Inverte o valor atual da variável `esta_arquivo_aberto`.
    menu_arquivo.entryconfig("Novo", state=tk.NORMAL if esta_arquivo_aberto else tk.DISABLED)
    menu_arquivo.entryconfig("Abrir", state=tk.NORMAL if esta_arquivo_aberto else tk.DISABLED)

# Cria a janela principal
janela = tk.Tk()  # Cria uma instância da classe Tk, que representa a janela principal da aplicação.

# Define o título da janela principal
janela.title("Menu Principal")  # Define o título da janela principal como "Menu Principal".

# Cria o menu principal
menu_cascata = tk.Menu(janela)  # Cria um objeto do tipo Menu que será usado como menu principal da janela.

# Configura a janela principal para usar o menu criado
janela.config(menu=menu_cascata)  # Configura a janela principal para utilizar o menu criado como seu menu principal.

# Variável global para controlar o estado das opções de arquivo
esta_arquivo_aberto = False  # Inicializa a variável global `esta_arquivo_aberto` com o valor False (opções desativadas).

# Cria o menu suspenso "Arquivo" e adiciona opções com comandos
menu_arquivo = tk.Menu(menu_cascata, tearoff=0)  # Cria um submenu dentro do menu principal com o rótulo "Arquivo".
menu_cascata.add_cascade(label="Arquivo", menu=menu_arquivo)  # Adiciona o menu "Arquivo" ao menu principal como um item suspenso.

# Adiciona a opção "Novo" ao menu "Arquivo" (desativada por padrão)
menu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo criado!"), state=tk.DISABLED)

# Adiciona a opção "Abrir" ao menu "Arquivo" (desativada por padrão)
menu_arquivo.add_command(label="Abrir", command=lambda: print("Abrindo arquivo..."), state=tk.DISABLED)

# Adiciona uma linha divisória ao menu "Arquivo"
menu_arquivo.add_separator()

# Adiciona a opção "Alternar Opções" ao menu "Arquivo"
menu_arquivo.add_command(label="Alternar Opções", command=alternar_opcoes_arquivo)

janela.mainloop()