'''
3. Escolha de Tamanho de Pizza: 
Implemente um programa com um OptionMenu para selecionar o tamanho da pizza 
(Pequena, Média, Grande). Um campo de entrada permite digitar o número de pizzas. Ao 
clicar em um botão "Pedir", o programa exibe o total a pagar, considerando o preço de cada 
tamanho.
'''
import tkinter as tk

def valorTotal():
    tamanho = selecao_tamanho.get()
    if tamanho == "Pequena":
        valorPequena = int(quantidade_pizzas.get()) * 30
        label_valor_total.config(text=f"Valor total é R${valorPequena:.2f}")
    elif tamanho == "Média":
        valorMedia = int(quantidade_pizzas.get()) * 50
        label_valor_total.config(text=f"Valor total é R${valorMedia:.2f}")
    elif tamanho == "Grande":
        valorGrande = int(quantidade_pizzas.get()) * 70
        label_valor_total.config(text=f"Valor total é R${valorGrande:.2f}")
    elif tamanho == "Familia":
        valorFamilia = int(quantidade_pizzas.get()) * 80
        label_valor_total.config(text=f"Valor total é R${valorFamilia:.2f}")
        
janela = tk.Tk()
janela.title("Exercício 3: Escolha de Tamanho de Pizza")

tamanho_pizzas = ["Pequena", "Média", "Grande", "Familia"]

selecao_tamanho = tk.StringVar(janela)
selecao_tamanho.set(tamanho_pizzas[0])

quantidade_pizzas = tk.Entry(janela)
quantidade_pizzas.pack(padx=5, pady=5)

menu_pizzas = tk.OptionMenu(janela, selecao_tamanho, *tamanho_pizzas)
menu_pizzas.pack(pady=10)

botao_pedido = tk.Button(janela, text="Pedir", command=valorTotal)        
botao_pedido.pack()

label_valor_total = tk.Label(janela, text="")
label_valor_total.pack(pady=5)

janela.mainloop()