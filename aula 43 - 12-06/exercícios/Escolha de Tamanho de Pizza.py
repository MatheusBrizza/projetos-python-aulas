'''
3. Escolha de Tamanho de Pizza: 
Implemente um programa com um OptionMenu para selecionar o tamanho da pizza 
(Pequena, Média, Grande). Um campo de entrada permite digitar o número de pizzas. Ao 
clicar em um botão "Pedir", o programa exibe o total a pagar, considerando o preço de cada 
tamanho.
'''
import tkinter as tk
from tkinter import messagebox

tamanho_pizzas = ["Pequena", "Média", "Grande", "Familia"]
precos_pizzas = {"Pequena": 30, "Média": 50, "Grande": 70, "Familia": 80}

ingredientes_adicionais = ["Catupiry", "Maionese caseira", "Ketchup", "Borda recheada"]
ingredientes_adicionais_select = []
precos_adicionais = {"Catupiry": 5, "Maionese caseira": 7, "Ketchup": 5, "Borda recheada": 10}

def valorTotal():
    valorAdicionais = sum(precos_adicionais[ingrediente] for ingrediente in ingredientes_adicionais_select)
    tamanho = selecao_tamanho.get()
    try:
        quantidade = int(quantidade_pizzas.get())
        if quantidade < 1:
            raise ValueError(label_valor_total.config(text="Quantidade inválida"))
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida!")
    print(ingredientes_adicionais_select)
    print(valorAdicionais)
    if tamanho in tamanho_pizzas:
        valorTotal = quantidade * (precos_pizzas.get(tamanho) + valorAdicionais)
        #label_valor_total.config(text=f"Valor total é R${valorTotal:.2f}")
    response = messagebox.askquestion("Confirmar pedido", f"Confirmar pedido de {quantidade} pizza(s) tamanho {tamanho} com extras {ingredientes_adicionais_select} no valor de R${valorTotal:.2f}?")
    if response == "yes":
        messagebox.showinfo("Pedido confirmado", "Pedido confirmado!")

        print(f"Tamanho: {tamanho}")
        print(f"Quantidade: {quantidade}")
        print(f"Ingredientes extras: {ingredientes_adicionais_select}")
        print(f"Valor total: {valorTotal}")
def adicionarExtrasPedido(ingrediente):
#    ingredientes = [ingrediente.get() for ingrediente in ingredientes_adicionais_select if ingrediente.get()]
    
    if ingrediente in ingredientes_adicionais_select:
        ingredientes_adicionais_select.remove(ingrediente)
        valor =- precos_adicionais.get(ingrediente)
    else:
        ingredientes_adicionais_select.append(ingrediente)
        valor =+ precos_adicionais.get(ingrediente)
    return valor

def apresentarValorUnitario(selecao_tamanho):
    tamanho = selecao_tamanho
    if tamanho in precos_pizzas:
        label_exibir_preco_unitario.config(text=f"R$ {precos_pizzas[tamanho]:.2f}")
    else:
        label_exibir_preco_unitario.config(text="Tamanho inválido!")

janela = tk.Tk()
janela.title("Exercício 3: Escolha de Tamanho de Pizza")

label_titulo = tk.Label(janela,text="Escolha o tamanho da Pizza!")
label_titulo.grid(row=0, column=0, padx=10, pady=5)

label_exibir_preco_unitario = tk.Label(janela, text="")
label_exibir_preco_unitario.grid(row=3, column=0, pady=5)

quantidade_pizzas = tk.Entry(janela)
quantidade_pizzas.grid(row=2, column=0, padx=5, pady=5)

selecao_tamanho = tk.StringVar(janela)
menu_pizzas = tk.OptionMenu(janela, selecao_tamanho, *tamanho_pizzas, command=apresentarValorUnitario)
menu_pizzas.grid(row=1, column=0, pady=10)

for x in range(len(ingredientes_adicionais)):
    
    var = tk.IntVar()
    l = tk.Checkbutton(janela, text=ingredientes_adicionais[x], variable=var, command=lambda x=ingredientes_adicionais[x]: adicionarExtrasPedido(x))
    l.grid(padx=10, sticky=tk.W)

botao_pedido = tk.Button(janela, text="Pedir", command=valorTotal)
botao_pedido.grid(row=8, column=0)

label_valor_total = tk.Label(janela, text="")
label_valor_total.grid(row=9, column=0, padx=10, pady=5)

janela.mainloop()