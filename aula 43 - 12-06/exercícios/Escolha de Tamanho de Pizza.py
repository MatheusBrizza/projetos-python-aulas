'''
3. Escolha de Tamanho de Pizza: 
Implemente um programa com um OptionMenu para selecionar o tamanho da pizza 
(Pequena, Média, Grande). Um campo de entrada permite digitar o número de pizzas. Ao 
clicar em um botão "Pedir", o programa exibe o total a pagar, considerando o preço de cada 
tamanho.
'''
import tkinter as tk
from tkinter import messagebox
import datetime
import mysql.connector

nome_db = "senac_pizzaria"
tb_pedidos = "pedidos"
tb_clientes = "clientes"

connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=''
    )

# Verifica se o banco de dados senac_pizzaria existe
executor_comando_sql = connector.cursor()
'''executor_comando_sql.execute('SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "senac_pizzaria";') # busca o banco de dados pelo nome
nome_db = executor_comando_sql.fetchone()[0] # salva o resultado numa variável nome_db.'''
executor_comando_sql.execute(f'SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "{nome_db}";')

# Salvando o resultado da pesquisa acima numa variável
resultado_db = executor_comando_sql.fetchone()[0]

# Fecha a conexão com o banco de dados
connector.close()

# Se o número de resultados for maior que zero, significa que o banco de dados existe
if resultado_db > 0:
  print(f'O banco de dados {nome_db} existe e esta pronto para uso.')
else:
    print(f"banco de dados {nome_db} não encontrado, criando-o agora.")
    # Conectar-se ao servidor MySQL para criar o banco de dados
    connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=''
    )

    executor_comando_sql = connector.cursor() # necessário reiniciar a variável pois senão dá o erro ReferenceError: weakly-referenced object no longer exists pois a conexão foi terminada na utilização anterior
    executor_comando_sql.execute(f'CREATE DATABASE {nome_db}')
    connector.commit()
    

# Conectar-se ao banco de dados senac_pizzaria recém-criado
connector = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database= nome_db  
)
    
executor_comando_sql = connector.cursor() # também é necessário reiniciar a variável pois também senão dá o erro ReferenceError: weakly-referenced object no longer exists já que a variável anterior se referia apenas ao uso para procurar o banco de dados 
executor_comando_sql.execute(f'SELECT COUNT(*) FROM information_schema.TABLES WHERE TABLE_NAME = "{tb_pedidos}";')
resultado_tb = executor_comando_sql.fetchone()[0]
connector.close()

if resultado_tb > 0:
    print(f"tabela {tb_pedidos} já existe!")
else:
    print("criando tabela")
    connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
    executor_comando_sql = connector.cursor()
    executor_comando_sql.execute('CREATE TABLE pedidos (id INT AUTO_INCREMENT PRIMARY KEY, data DATETIME NOT NULL, tamanho VARCHAR(255),quantidade VARCHAR(255), valor_total DECIMAL(10,2) NOT NULL);')
    connector.commit()
    connector.close()


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
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida!")
    if tamanho in tamanho_pizzas:
        valorTotal = quantidade * (precos_pizzas.get(tamanho) + valorAdicionais)
    response = messagebox.askquestion("Confirmar pedido", f"Confirmar pedido de {quantidade} pizza(s) tamanho {tamanho} com extras {ingredientes_adicionais_select} no valor de R${valorTotal:.2f}?")
    if response == "yes":
        messagebox.showinfo("Pedido confirmado", "Pedido confirmado!")
        
        # Enviando dados para inserir na tabela pedidos
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database=nome_db)
        executor_comando_sql = connector.cursor()
        executor_comando_sql.execute("INSERT INTO pedidos (data, tamanho, quantidade, valor_total) VALUES (%s, %s, %s, %s)", (datetime.datetime.now(), tamanho, quantidade, valorTotal))
        connector.commit()
        connector.close()
        
    else:
        messagebox.showwarning("Pedido cancelado", "Pedido foi cancelado.")
        
def adicionarExtrasPedido(ingrediente):    
    if ingrediente in ingredientes_adicionais_select:
        ingredientes_adicionais_select.remove(ingrediente)
    else:
        ingredientes_adicionais_select.append(ingrediente)

def apresentarValorUnitario(selecao_tamanho):
    tamanho = selecao_tamanho
    if tamanho in precos_pizzas:
        label_exibir_preco_unitario.config(text=f"R$ {precos_pizzas[tamanho]:.2f}")
    else:
        label_exibir_preco_unitario.config(text="Tamanho inválido!")

janela = tk.Tk()
janela.title("Senac Pizzaria")

label_titulo = tk.Label(janela,text="Escolha o tamanho da Pizza!")
label_titulo.grid(row=0, column=0, padx=10, pady=5)

selecao_tamanho = tk.StringVar(janela)
menu_pizzas = tk.OptionMenu(janela, selecao_tamanho, *tamanho_pizzas, command=apresentarValorUnitario)
menu_pizzas.grid(row=1, column=0, pady=5)

label_exibir_preco_unitario = tk.Label(janela, text="")
label_exibir_preco_unitario.grid(row=2, column=0, pady=2)

quantidade_pizzas = tk.Entry(janela)
quantidade_pizzas.grid(row=3, column=0, pady=5)

for x in range(len(ingredientes_adicionais)):
    var = tk.IntVar()
    l = tk.Checkbutton(janela, text=ingredientes_adicionais[x], variable=var, command=lambda x=ingredientes_adicionais[x]: adicionarExtrasPedido(x))
    l.grid(padx=10, pady=2, sticky=tk.W)

botao_pedido = tk.Button(janela, text="Pedir", command=valorTotal)
botao_pedido.grid(row=8, column=0, pady=10)

janela.mainloop()