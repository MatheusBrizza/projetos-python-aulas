'''
1. Escolha de Café: 
Crie um programa que apresente um menu com opções de café (expresso, cappuccino, latte 
macchiato) e permita ao usuário selecionar sua bebida preferida. Exiba uma mensagem 
informando a escolha do usuário.
'''
import tkinter as tk

def adicionarItemNoMenu(submenu, nome_item, tipo):
    submenu_item = tk.Menu(submenu, tearoff=0)
    if tipo == "cascade":
        submenu.add_cascade(label=nome_item, menu=submenu_item)
        selecionarTamanhoItem(submenu_item, nome_item)
    elif tipo == "command":
        submenu.add_command(label=nome_item, command=lambda: print(f"Você escolheu {nome_item}"))
    

def selecionarTamanhoItem(submenu, nome_item):
    submenu.add_command(label="P", command=lambda: print(f"Você escolheu {nome_item} tamanho P"))
    submenu.add_command(label="M", command=lambda: print(f"Você escolheu {nome_item} tamanho M"))
    submenu.add_command(label="G", command=lambda: print(f"Você escolheu {nome_item} tamanho G"))

janela = tk.Tk()
janela.title("Exercício 1: Escolha de Café")

menu_cascata = tk.Menu(janela)
janela.config(menu=menu_cascata)

submenu_cafes = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Cafés", menu=submenu_cafes)
adicionarItemNoMenu(submenu_cafes, "Expresso", "cascade")
adicionarItemNoMenu(submenu_cafes, "Cappuccino", "cascade")
adicionarItemNoMenu(submenu_cafes, "Mocca", "cascade")
adicionarItemNoMenu(submenu_cafes, "Chocolate quente", "cascade")

submenu_pasteis = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Pastéis", menu=submenu_pasteis)
adicionarItemNoMenu(submenu_pasteis, "Pastel de frango", "command")
adicionarItemNoMenu(submenu_pasteis, "Pastel de calabresa", "command")


janela.mainloop()