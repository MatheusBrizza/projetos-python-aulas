'''
Exercício 3: Criando Menus Hierárquicos com Submenus em Cascata 
• Crie um menu principal com submenus para "Arquivo", "Editar" e "Ajuda". 
• Crie submenus em cascata para cada item principal, com opções como "Novo", 
"Abrir", "Desfazer", "Copiar", "Conteúdo" e "Sobre". 
• Adicione comandos a cada opção de submenu para executar ações simples, como 
imprimir uma mensagem no console.
'''

import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 3: Criando Menus Hierárquicos com Submenus em Cascata")

menu_cascata = tk.Menu(janela)
janela.config(menu=menu_cascata)

submenu_arquivo = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Arquivo", menu=submenu_arquivo)
submenu_arquivo.add_command(label="Novo", command=lambda: print("Arquivo novo"))
submenu_arquivo.add_command(label="Abrir", command=lambda: print("Arquivo aberto"))

submenu_editar = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Editar", menu= submenu_editar)
submenu_editar.add_command(label="Desfazer", command=lambda: print("Desfeito"))
submenu_editar.add_command(label="Copiar", command=lambda: print("Trecho copiado"))
submenu_editar.add_separator()
# Submenu de salvar adicionado ao submenu editar
submenu_salvar = tk.Menu(submenu_editar, tearoff=0)
submenu_editar.add_cascade(label="Salvar", menu=submenu_salvar)
# Esboço inicial onde adiciona opções de salvar no menu principal
# submenu_salvar = tk.Menu(menu_cascata, tearoff=0)
# menu_cascata.add_cascade(label="Salvar", menu=submenu_salvar) 
submenu_salvar.add_command(label="Salvar", command=lambda: print("Arquivo salvo"))
submenu_salvar.add_command(label="Salvar como...", command=lambda: print("Escolher caminho que deseja salvar o arquivo"))

submenu_ajuda = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Ajuda", menu=submenu_ajuda)
submenu_ajuda.add_command(label="Conteúdo", command=lambda: print("Conteúdo pode ser encontrado na pasta 'conteúdo' "))
submenu_ajuda.add_command(label="Sobre", command=lambda: print("Exercícios para reforçar conhecimento de menus e submenus em tkinter"))

janela.mainloop()