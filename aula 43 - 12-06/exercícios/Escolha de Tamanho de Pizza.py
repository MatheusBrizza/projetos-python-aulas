'''
3. Escolha de Tamanho de Pizza: 
Implemente um programa com um OptionMenu para selecionar o tamanho da pizza 
(Pequena, Média, Grande). Um campo de entrada permite digitar o número de pizzas. Ao 
clicar em um botão "Pedir", o programa exibe o total a pagar, considerando o preço de cada 
tamanho.
'''
import tkinter as tk

tamanho_pizzas = ["Pequena", "Média", "Grande", "Familia"]
precos_pizzas = {"Pequena": 30, "Média": 50, "Grande": 70, "Família": 80}

ingredientes_adicionais = ["Catupiry", "Maionese caseira", "Ketchup", "Borda recheada"]
ingredientes_adicionais_select = []
precos_adicionais = {"Catupiry": 5, "Maionese caseira": 7, "Ketchup": 5, "Borda recheada": 10}

def valorTotal():
    tamanho = selecao_tamanho.get()
    quantidade = int(quantidade_pizzas.get())
    if quantidade < 0:
        raise ValueError(label_valor_total.config(text="Não é permitido quantidades negativas"))
    valorAdicionais = adicionarExtrasPedido()
    print(ingredientes_adicionais_select)
    print(valorAdicionais)
    if tamanho == "Pequena":
        valorTotalPequena = (quantidade * precos_pizzas.get("Pequena")) + valorAdicionais
        label_valor_total.config(text=f"Valor total é R${valorTotalPequena:.2f}")
    elif tamanho == "Média":
        valorTotalMedia = quantidade * precos_pizzas.get("Média")
        label_valor_total.config(text=f"Valor total é R${valorTotalMedia:.2f}")
    elif tamanho == "Grande":
        valorTotalGrande = quantidade * precos_pizzas.get("Grande")
        label_valor_total.config(text=f"Valor total é R${valorTotalGrande:.2f}")
    else:
        valorTotalFamilia = quantidade * precos_pizzas.get("Família")
        label_valor_total.config(text=f"Valor total é R${valorTotalFamilia:.2f}")

def adicionarExtrasPedido():
#    ingredientes = [ingrediente.get() for ingrediente in ingredientes_adicionais_select if ingrediente.get()]
    valorTotalAdicionais = 0
    for ingrediente in ingredientes_adicionais_select:
        if ingrediente == "Catupiry":
            valorTotalAdicionais =+ precos_adicionais.get("Catupiry")
        elif ingrediente == "Maionese caseira":
            valorTotalAdicionais =+ precos_adicionais.get("Maionese caseira")
        elif ingrediente == "Ketchup":
            valorTotalAdicionais =+ precos_adicionais.get("Ketchup")
        elif ingrediente == "Borda recheada":
            valorTotalAdicionais =+ precos_adicionais.get("Borda recheada")
        return valorTotalAdicionais

''' #Não funcionou
def apresentarValorUnitario(selecao_tamanho):
    tamanho = selecao_tamanho.get()
    if tamanho == "Pequena":
        print("foi")
        label_exibir_preco_unitario.config(text=f'R${precos_pizzas.get("Pequena")}')
'''
janela = tk.Tk()
janela.title("Exercício 3: Escolha de Tamanho de Pizza")

selecao_tamanho = tk.StringVar(janela)

label_titulo = tk.Label(janela,text="Escolha o tamanho da Pizza!")
label_titulo.pack(padx=10, pady=5)

label_exibir_preco_unitario = tk.Label(janela, text="")
label_exibir_preco_unitario.pack(pady=5)

quantidade_pizzas = tk.Entry(janela)
quantidade_pizzas.pack(padx=5, pady=5)

menu_pizzas = tk.OptionMenu(janela, selecao_tamanho, *tamanho_pizzas)
menu_pizzas.pack(pady=10)

'''
var = tk.BooleanVar()
checkbutton_queijo = tk.Checkbutton(janela, text="Queijo", variable=var, command=adicionarExtrasPedido)
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()
checkbutton_presunto = tk.Checkbutton(janela, text="Presunto", variable=var, command=adicionarExtrasPedido)
checkbutton_maionese = tk.Checkbutton(janela, text="Maionese", variable=var, command=adicionarExtrasPedido)
checkbutton_ketchup = tk.Checkbutton(janela, text="Ketchup", variable=var, command=adicionarExtrasPedido)
checkbutton_queijo.pack()
checkbutton_presunto.pack()
checkbutton_maionese.pack()
checkbutton_ketchup.pack()
'''


for x in range(len(ingredientes_adicionais)):
    var = tk.IntVar()
    l = tk.Checkbutton(janela, text=ingredientes_adicionais[x], variable=var, command=lambda x=ingredientes_adicionais[x]: ingredientes_adicionais_select.append(x))
    l.pack(anchor='w')

botao_pedido = tk.Button(janela, text="Pedir", command=valorTotal)
botao_pedido.pack()

label_valor_total = tk.Label(janela, text="")
label_valor_total.pack(padx=10, pady=5)

janela.mainloop()