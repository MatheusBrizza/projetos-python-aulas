'''
2. Seleção de Tamanho de Camiseta: 
Desenvolva um programa que ofereça um menu com opções de tamanho de camisetas (P, 
M, G, GG). Permita que o usuário escolha seu tamanho e exiba uma mensagem 
confirmando a seleção.
'''
import tkinter as tk

def adicionarItemNoMenu(submenu, nome_item):
    submenu_item = tk.Menu(submenu, tearoff=0)
    submenu.add_cascade(label=nome_item, menu=submenu_item)
    selecionarTamanhoItem(submenu_item, nome_item)

def selecionarTamanhoItem(submenu, nome_item):
    submenu.add_command(label="P", command=lambda: print(f"Você escolheu {nome_item} tamanho P"))
    submenu.add_command(label="M", command=lambda: print(f"Você escolheu {nome_item} tamanho M"))
    submenu.add_command(label="G", command=lambda: print(f"Você escolheu {nome_item} tamanho G"))
    submenu.add_command(label="GG", command=lambda: print(f"Você escolheu {nome_item} tamanho GG"))


janela = tk.Tk()
janela.title("Exercício 2: Seleção de Tamanho de Camiseta")

menu_cascata = tk.Menu(janela)
janela.config(menu=menu_cascata)

opcao_roupas_masculinas = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Roupas Masc", menu=opcao_roupas_masculinas)
adicionarItemNoMenu(opcao_roupas_masculinas, "Camiseta manga curta grêmio")
adicionarItemNoMenu(opcao_roupas_masculinas, "Camiseta manga curta inter")
adicionarItemNoMenu(opcao_roupas_masculinas, "Paletó preto")
adicionarItemNoMenu(opcao_roupas_masculinas, "Calças jeans azul")

opcao_roupas_infantis = tk.Menu(menu_cascata, tearoff=0)
menu_cascata.add_cascade(label="Infantis", menu=opcao_roupas_infantis)
adicionarItemNoMenu(opcao_roupas_infantis, "camiseta Superman")
adicionarItemNoMenu(opcao_roupas_infantis, "camiseta Homem-aranha")
adicionarItemNoMenu(opcao_roupas_infantis, "calça moletom azul")
adicionarItemNoMenu(opcao_roupas_infantis, "Meias Batman")

janela.mainloop()