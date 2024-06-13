'''
Exercício 1: Criando um Menu Principal e Submenus 
• Crie uma janela principal com um título. 
• Crie um menu principal e adicione um item principal. 
• Crie submenus para o item principal, com opções como "Novo", "Abrir" e "Sair". 
• Adicione comandos a cada opção de submenu para executar ações simples, como 
imprimir uma mensagem no console.
'''
import tkinter as tk

janela = tk.Tk()
janela.title("Exercício 1: Criando um Menu Principal e Submenus")

menu_cascata = tk.Menu(janela)
janela.config(menu=menu_cascata)

submenu = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Arquivo", menu=submenu)
submenu.add_command(label="Novo", command=lambda: print("novo arquivo"))
submenu.add_command(label="Abrir", command=lambda: print("arquivo aberto"))
submenu.add_command(label="Salvar", command=lambda: print("Arquivo salvo"))
submenu.add_command(label="Fechar", command=janela.quit)

janela.mainloop()