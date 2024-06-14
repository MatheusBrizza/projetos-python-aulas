import tkinter as tk

tamanho_pizzas = ["Pequena", "Média", "Grande", "Família"]
precos_pizzas = {"Pequena": 30, "Média": 50, "Grande": 70, "Família": 80}

ingredientes_adicionais = ["Catupiry", "Maionese caseira", "Ketchup", "Borda recheada"]
ingredientes_selecionados = [] 
precos_adicionais = {"Catupiry": 5, "Maionese caseira": 7, "Ketchup": 5, "Borda recheada": 10}

def calcular_valor_total():
    global ingredientes_selecionados

    tamanho = selecao_tamanho.get()
    quantidade = int(quantidade_pizzas.get())

    if quantidade < 0:
        raise ValueError("Quantidade inválida!")

    valor_pizza = precos_pizzas[tamanho] * quantidade
    valor_adicionais = sum(precos_adicionais[ingrediente] for ingrediente in ingredientes_selecionados)
    valor_total = valor_pizza + valor_adicionais

    label_valor_total.config(text=f"Valor total: R$ {valor_total:.2f}")

def adicionar_ingrediente(ingrediente):
    global ingredientes_selecionados

    if ingrediente in ingredientes_selecionados:
        ingredientes_selecionados.remove(ingrediente)
    else:
        ingredientes_selecionados.append(ingrediente)

def apresentar_valor_unitario(selecao_tamanho):
    tamanho = selecao_tamanho.get()
    if tamanho in precos_pizzas:
        label_exibir_preco_unitario.config(text=f"R$ {precos_pizzas[tamanho]}")
    else:
        label_exibir_preco_unitario.config(text="Tamanho inválido!")

# Criação da interface gráfica
janela = tk.Tk()
janela.title("Pizza Perfeita")

# Frame para o título
frame_titulo = tk.Frame(janela)
frame_titulo.pack(pady=10)

# Título da tela
label_titulo = tk.Label(frame_titulo, text="Escolha o tamanho da Pizza!")
label_titulo.pack(padx=10, pady=5)

# Frame para seleção de tamanho e quantidade
frame_selecao = tk.Frame(janela)
frame_selecao.pack(pady=10)

# Menu suspenso para selecionar o tamanho da pizza
selecao_tamanho = tk.StringVar(janela)
menu_pizzas = tk.OptionMenu(frame_selecao, selecao_tamanho, *tamanho_pizzas, command=apresentar_valor_unitario)
menu_pizzas.pack(padx=10, pady=5)

# Label para exibir o preço unitário
label_exibir_preco_unitario = tk.Label(frame_selecao, text="")
label_exibir_preco_unitario.pack(padx=10, pady=5)

# Campo de entrada para quantidade de pizzas
quantidade_pizzas = tk.Entry(frame_selecao)
quantidade_pizzas.pack(padx=10, pady=5)

# Frame para ingredientes adicionais
frame_ingredientes = tk.Frame(janela)
frame_ingredientes.pack(pady=10)

for row, ingrediente in enumerate(ingredientes_adicionais):
    var = tk.IntVar()
    l = tk.Checkbutton(frame_ingredientes, text=ingrediente, variable=var, command=lambda x=ingrediente: adicionar_ingrediente(x))
    l.grid(row=row, column=0, sticky="w", padx=10, pady=5)

# Frame para o botão de pedido e valor total
frame_valor = tk.Frame(janela)
frame_valor.pack(pady=10)

# Botão para calcular o valor total
botao_pedido = tk.Button(frame_valor, text="Pedir", command=calcular_valor_total)
botao_pedido.pack(padx=10, pady=5)

# Label para exibir o valor total do pedido
label_valor_total = tk.Label(frame_valor, text="")
label_valor_total.pack(padx=10, pady=5)

# Execução da interface gráfica
janela.mainloop()