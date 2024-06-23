'''
3. Escolha de Tamanho de Pizza: 
Implemente um programa com um OptionMenu para selecionar o tamanho da pizza 
(Pequena, Média, Grande). Um campo de entrada permite digitar o número de pizzas. Ao 
clicar em um botão "Pedir", o programa exibe o total a pagar, considerando o preço de cada 
tamanho.
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import ttk
import datetime
import mysql.connector
import re

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
    
# verificando se já existe a tabela pedidos
executor_comando_sql = connector.cursor() # também é necessário reiniciar a variável pois também senão dá o erro ReferenceError: weakly-referenced object no longer exists já que a variável anterior se referia apenas ao uso para procurar o banco de dados 
executor_comando_sql.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_db}'  AND table_name = '{tb_pedidos}');")
resultado_tb = executor_comando_sql.fetchone()[0]
connector.close()

if resultado_tb > 0:
    print(f"tabela {tb_pedidos} já existe!")
else:
    print("criando tabela pedidos")
    connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
    executor_comando_sql = connector.cursor()
    executor_comando_sql.execute('CREATE TABLE pedidos (id INT AUTO_INCREMENT PRIMARY KEY, data DATETIME NOT NULL, tamanho VARCHAR(255), quantidade VARCHAR(255), valor_total DECIMAL(10,2) NOT NULL);')
    connector.commit()
    connector.close()
    
connector = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database= nome_db  
)
    
# verificando se já existe a tabela clientes
executor_comando_sql = connector.cursor() # também é necessário reiniciar a variável pois também senão dá o erro ReferenceError: weakly-referenced object no longer exists já que a variável anterior se referia apenas ao uso para procurar o banco de dados 
executor_comando_sql.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_db}'  AND table_name = '{tb_clientes}');")
resultado_tb = executor_comando_sql.fetchone()[0]
connector.close()

if resultado_tb > 0:
    print(f"tabela {tb_clientes} já existe!")
else:
    print("criando tabela clientes")
    connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
    executor_comando_sql = connector.cursor()
    executor_comando_sql.execute('CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL, telefone VARCHAR(255), email VARCHAR(255));')
    connector.commit()
    connector.close()
    
    
#Função de tela de fazer novo pedido
def novoPedido():
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
            tela_novo_pedido.destroy()
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

    tela_novo_pedido = tk.Tk()
    tela_novo_pedido.title("Novo pedido")
    tela_novo_pedido.geometry("170x280")

    label_titulo = tk.Label(tela_novo_pedido,text="Escolha o tamanho da Pizza!")
    label_titulo.grid(row=0, column=0, padx=10, pady=5)

    selecao_tamanho = tk.StringVar(tela_novo_pedido)
    menu_pizzas = tk.OptionMenu(tela_novo_pedido, selecao_tamanho, *tamanho_pizzas, command=apresentarValorUnitario)
    menu_pizzas.grid(row=1, column=0, pady=5)

    label_exibir_preco_unitario = tk.Label(tela_novo_pedido, text="")
    label_exibir_preco_unitario.grid(row=2, column=0, pady=2)

    quantidade_pizzas = tk.Entry(tela_novo_pedido)
    quantidade_pizzas.grid(row=3, column=0, pady=5)

    for x in range(len(ingredientes_adicionais)):
        var = tk.IntVar()
        l = tk.Checkbutton(tela_novo_pedido, text=ingredientes_adicionais[x], variable=var, command=lambda x=ingredientes_adicionais[x]: adicionarExtrasPedido(x))
        l.grid(padx=10, pady=2, sticky=tk.W)

    botao_pedido = tk.Button(tela_novo_pedido, text="Pedir", command=valorTotal)
    botao_pedido.grid(row=8, column=0, pady=10)

    tela_novo_pedido.mainloop()

def listarPedidos():
    tela_lista_pedidos = Toplevel(tela_inicial)
    tela_lista_pedidos.title("Lista Pedidos")
    
    tabela_pedidos = ttk.Treeview(tela_lista_pedidos, columns=("ID", "Data", "Tamanho", "Quantidade", "Valor_Total"), show='headings')

    tabela_pedidos.heading('ID', text='ID')
    tabela_pedidos.heading('Data', text='Data')
    tabela_pedidos.heading('Tamanho', text='Tamanho')
    tabela_pedidos.heading('Quantidade', text='Quantidade')
    tabela_pedidos.heading('Valor_Total', text='Valor_Total')
    tabela_pedidos.pack(fill="both", expand=True)
    tabela_pedidos.bind('<Map>', lambda event: atualizarTabelaPedidos())
    
    def atualizarTabelaPedidos():
        connector = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database=nome_db)
            # Buscar dados do banco de dados e popular a tabela_pedidos treeview
        executor_comando_sql =  executor_comando_sql = connector.cursor()
        executor_comando_sql.execute('SELECT * FROM pedidos')
        rows = executor_comando_sql.fetchall()
            # Limpar dados anteriores
        for row in tabela_pedidos.get_children():
            tabela_pedidos.delete(row)

            # Adicionar novos dados
        for row in rows:
            tabela_pedidos.insert('', 'end', values=row)

            # Adicionar um evento de seleção
        tabela_pedidos.bind('<<TreeviewSelect>>', selecao_unica)
            # Botões para atualizar e deletar
    def selecao_unica(event):
            # Obter o item selecionado
            item = tabela_pedidos.selection()[0]

            # Pegar os dados do item selecionado
            dados = tabela_pedidos.item(item, 'values')
            id = dados[0]
            data = dados[1]
            tamanho = dados[2]
            quantidade = dados[3]
            valor = dados[4]

    def atualizarDadosPedido():
        if tabela_pedidos.selection():
            tamanho_pizzas = ["Pequena", "Média", "Grande", "Familia"]
            precos_pizzas = {"Pequena": 30, "Média": 50, "Grande": 70, "Familia": 80}

            ingredientes_adicionais = ["Catupiry", "Maionese caseira", "Ketchup", "Borda recheada"]
            ingredientes_adicionais_select = []
            precos_adicionais = {"Catupiry": 5, "Maionese caseira": 7, "Ketchup": 5, "Borda recheada": 10}

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
                    
            def atualizarValor():
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
                
                item = tabela_pedidos.selection()[0]
                data = tabela_pedidos.item(item, 'values')
                id = data[0]
                
                # Enviando dados para inserir na tabela pedidos
                connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database=nome_db)
                executor_comando_sql = connector.cursor()
                executor_comando_sql.execute('UPDATE pedidos SET data=%s, tamanho=%s, quantidade=%s, valor_total=%s WHERE id=%s', (datetime.datetime.now(), tamanho, quantidade, valorTotal, id))
                connector.commit()
                connector.close()
                atualizarTabelaPedidos()
                tela_atualizar_dados_pedido.destroy()
                    
            tela_atualizar_dados_pedido = Toplevel(tela_lista_pedidos)
            tela_atualizar_dados_pedido.title('Atualizar dados pedido')
            tela_atualizar_dados_pedido.geometry("170x280")
            
            selecao_tamanho = tk.StringVar(tela_atualizar_dados_pedido)
            menu_pizzas = tk.OptionMenu(tela_atualizar_dados_pedido, selecao_tamanho, *tamanho_pizzas, command=apresentarValorUnitario)
            menu_pizzas.grid(row=1, column=0, pady=5)
                        
            label_exibir_preco_unitario = tk.Label(tela_atualizar_dados_pedido, text="")
            label_exibir_preco_unitario.grid(row=2, column=0, pady=2)
            
            quantidade_pizzas = tk.Entry(tela_atualizar_dados_pedido)
            quantidade_pizzas.grid(row=3, column=0, pady=5)

            for x in range(len(ingredientes_adicionais)):
                var = tk.IntVar()
                l = tk.Checkbutton(tela_atualizar_dados_pedido, text=ingredientes_adicionais[x], variable=var, command=lambda x=ingredientes_adicionais[x]: adicionarExtrasPedido(x))
                l.grid(padx=10, pady=2, sticky=tk.W)
                            
            # Botão para confirmar a adição command=lambda: atualizarBdPedidos(nome_cliente.get(), fone_cliente.get(), email_cliente.get())
            botao_atualizar_cliente = tk.Button(tela_atualizar_dados_pedido, text='Atualizar', command=lambda: atualizarValor())
            botao_atualizar_cliente.grid(row=8, column=0, columnspan=2, pady=10)
                    
        else:
            # Nenhum item selecionado, mostre uma mensagem de erro ou faça outra ação
            messagebox.showerror('Erro', 'Nenhum registro selecionado.')
            return
    def deletarPedido():
                if tabela_pedidos.selection():  # Verifica se há algum item selecionado
                    item = tabela_pedidos.selection()[0]
                    # Pegar o ID do contato selecionado
                    data = tabela_pedidos.item(item, 'values')
                    id = data[0]
                    
                # Verificar se o usuário realmente deseja excluir o registro
                    if messagebox.askyesno('Confirmação', 'Deseja excluir o registro?'):
                         
                    # Deletar dados do banco de dados
                        connector = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database=nome_db)
            # Buscar dados do banco de dados e popular a tabela_pedidos treeview
                        executor_comando_sql = connector.cursor()
                       
                        executor_comando_sql.execute('DELETE FROM pedidos WHERE id=%s', (id,))  # Passe o ID como uma tupla de um elemento
                        connector.commit()
                        atualizarTabelaPedidos()
                        
                else:
            # Nenhum item selecionado, mostre uma mensagem de erro ou faça outra ação
                    messagebox.showerror('Erro', 'Nenhum registro selecionado.')
                    return

    botao_atualizar = tk.Button(tela_lista_pedidos, text="Atualizar", command=atualizarDadosPedido)
    botao_excluir = tk.Button(tela_lista_pedidos, text="Excluir", command=deletarPedido)
    botao_atualizar.pack(side='left') 
    botao_excluir.pack(side='left') 


def novoCliente():
    def addicinar_dados(nome, telefone, email):
        if nome == '' or telefone == '' or email == '':
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return False
        if not re.match(r'^[0-9]+$', telefone):
            messagebox.showerror("Erro", "Número de telefone deve conter apenas números.")
            return False
        if len(telefone) < 9:
            messagebox.showerror("Erro", "Número de telefone inválido.")
            return False
        if "@" and ".com" not in email:
            messagebox.showerror("Erro", "E-mail digitado inválido.")
            return False
        
        connector = mysql.connector.connect(
                       host='127.0.0.1',
                       user='root',
                       password='',
                       database=nome_db
                       )
        
        executor_comando_sql = connector.cursor()
        executor_comando_sql.execute('INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)', (nome, telefone, email))
        connector.commit()
        connector.close()
        messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
        tela_novo_cliente.destroy()

    tela_novo_cliente = Toplevel(tela_inicial)
    tela_novo_cliente.title("Adicionar Cliente")
    tela_novo_cliente.geometry("220x125")
    
    frame_nome = tk.Frame(tela_novo_cliente)
    frame_nome.grid(row=1, column=0, pady=5, padx=10)
    
    label_nome_cliente = tk.Label(frame_nome, text="Insira Nome:")
    label_nome_cliente.grid(row=0, column=0)
    
    nome_cliente = tk.Entry(frame_nome)
    nome_cliente.grid(row=0, column=1)
    
    frame_fone = tk.Frame(tela_novo_cliente)
    frame_fone.grid(row=2, column=0, pady=5, padx=10)

    label_fone_cliente = tk.Label(frame_fone, text="Insira Telefone:")
    label_fone_cliente.grid(row=0, column=0)
    
    fone_cliente = tk.Entry(frame_fone)
    fone_cliente.grid(row=0, column=1)
    
    frame_email = tk.Frame(tela_novo_cliente)
    frame_email.grid(row=3, column=0, pady=5, padx=10)
    
    label_email_cliente = tk.Label(frame_email, text="Insira Email:")
    label_email_cliente.grid(row=0, column=0)
    
    email_cliente = tk.Entry(frame_email)
    email_cliente.grid(row=0, column=1)
    
    botao_adicionar_novo_cliente = tk.Button(tela_novo_cliente, text="Adicionar Cliente", command=lambda: addicinar_dados(nome_cliente.get(), fone_cliente.get(), email_cliente.get()))
    botao_adicionar_novo_cliente.grid(row=4, column=0)

def listarClientes():
    tela_lista_clientes = Toplevel(tela_inicial)
    tela_lista_clientes.title("Lista clientes")
    
    tabela_clientes = ttk.Treeview(tela_lista_clientes, columns=('ID', 'Nome', 'Telefone', 'Email'), show='headings')

    tabela_clientes.heading('ID', text='ID')
    tabela_clientes.heading('Nome', text='Nome')
    tabela_clientes.heading('Telefone', text='Telefone')
    tabela_clientes.heading('Email', text='Email')
    tabela_clientes.pack(fill="both", expand=True)
    tabela_clientes.bind('<Map>', lambda event: atualizarTabelaClientes())
    
    def atualizarTabelaClientes():
        connector = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database=nome_db)
            # Buscar dados do banco de dados e popular a tabela_clientes treeview
        executor_comando_sql =  executor_comando_sql = connector.cursor()
        executor_comando_sql.execute('SELECT * FROM clientes')
        rows = executor_comando_sql.fetchall()
            # Limpar dados anteriores
        for row in tabela_clientes.get_children():
            tabela_clientes.delete(row)

            # Adicionar novos dados
        for row in rows:
            tabela_clientes.insert('', 'end', values=row)

            # Adicionar um evento de seleção
        tabela_clientes.bind('<<TreeviewSelect>>', selecao_unica)
            # Botões para atualizar e deletar
    def selecao_unica(event):
            # Obter o item selecionado
            item = tabela_clientes.selection()[0]

            # Pegar os dados do item selecionado
            data = tabela_clientes.item(item, 'values')
            id = data[0]
            nome = data[1]
            telefone = data[2]
            email = data[3]
    
    def atualizarDadosCliente():
        if tabela_clientes.selection():
           
            tela_atualizar_dados = Toplevel(tela_lista_clientes)
            tela_atualizar_dados.title('Atualizar dados cliente')
            tela_atualizar_dados.geometry("220x150")
            
            frame_nome = tk.Frame(tela_atualizar_dados)
            frame_nome.grid(row=1, column=0, pady=5, padx=10)
            
            label_nome_cliente = tk.Label(frame_nome, text="Insira Nome:")
            label_nome_cliente.grid(row=0, column=0)
            
            nome_cliente = tk.Entry(frame_nome)
            nome_cliente.grid(row=0, column=1)
            
            frame_fone = tk.Frame(tela_atualizar_dados)
            frame_fone.grid(row=2, column=0, pady=5, padx=10)

            label_fone_cliente = tk.Label(frame_fone, text="Insira Telefone:")
            label_fone_cliente.grid(row=0, column=0)
            
            fone_cliente = tk.Entry(frame_fone)
            fone_cliente.grid(row=0, column=1)
            
            frame_email = tk.Frame(tela_atualizar_dados)
            frame_email.grid(row=3, column=0, pady=5, padx=10)
            
            label_email_cliente = tk.Label(frame_email, text="Insira Email:")
            label_email_cliente.grid(row=0, column=0)
            
            email_cliente = tk.Entry(frame_email)
            email_cliente.grid(row=0, column=1)
            
            # Botão para confirmar a adição
            botao_atualizar_cliente = tk.Button(tela_atualizar_dados, text='Atualizar', command=lambda: atualizarBd(nome_cliente.get(), fone_cliente.get(), email_cliente.get()))
            botao_atualizar_cliente.grid(row=4, column=0, columnspan=2, pady=10)
                    
        else:
            # Nenhum item selecionado, mostre uma mensagem de erro ou faça outra ação
            messagebox.showerror('Erro', 'Nenhum registro selecionado.')
            return
        def atualizarBd(novo_nome, novo_telefone, novo_email):
                if novo_nome == '' or novo_telefone == '' or novo_email == '':
                    messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                    return False
                if not re.match(r'^[0-9]+$', novo_telefone):
                    messagebox.showerror("Erro", "Número de telefone deve conter apenas números.")
                    return False
                if len(novo_telefone) < 9:
                    messagebox.showerror("Erro", "Número de telefone inválido.")
                    return False
                if "@" and ".com" not in novo_email:
                    messagebox.showerror("Erro", "E-mail digitado inválido.")
                    return False
            
                item = tabela_clientes.selection()[0]
                data = tabela_clientes.item(item, 'values')
                id = data[0]
                # Atualizar dados no banco de dados
                # o objeto 'cursor' é utilizado para executar a instrução SQL
                connector = mysql.connector.connect(
                                host='127.0.0.1',
                                user='root',
                                password='',
                                database=nome_db)
                # Buscar dados do banco de dados e popular a tabela_clientes treeview
                executor_comando_sql = connector.cursor()
                executor_comando_sql.execute('UPDATE clientes SET nome=%s, telefone=%s, email=%s WHERE id=%s', (novo_nome, novo_telefone, novo_email, id))
                # Confirma a alteração no banco de dados usando a função commit
                connector.commit()
                # Fecha a janela de atualização
                atualizarTabelaClientes()
                tela_atualizar_dados.destroy()
            
    def deletarCliente():
                if tabela_clientes.selection():  # Verifica se há algum item selecionado
                    item = tabela_clientes.selection()[0]
                    # Pegar o ID do contato selecionado
                    data = tabela_clientes.item(item, 'values')
                    id = data[0]
                    
                # Verificar se o usuário realmente deseja excluir o registro
                    if messagebox.askyesno('Confirmação', 'Deseja excluir o registro?'):
                         
                    # Deletar dados do banco de dados
                        connector = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database=nome_db)
            # Buscar dados do banco de dados e popular a tabela_clientes treeview
                        executor_comando_sql = connector.cursor()
                       
                        executor_comando_sql.execute('DELETE FROM clientes WHERE id=%s', (id,))  # Passe o ID como uma tupla de um elemento
                        connector.commit()
                        atualizarTabelaClientes()
                        
                else:
            # Nenhum item selecionado, mostre uma mensagem de erro ou faça outra ação
                    messagebox.showerror('Erro', 'Nenhum registro selecionado.')
                    return

    botao_atualizar = tk.Button(tela_lista_clientes, text="Atualizar", command=atualizarDadosCliente)
    botao_excluir = tk.Button(tela_lista_clientes, text="Excluir", command=deletarCliente)
    botao_atualizar.pack(side='left') 
    botao_excluir.pack(side='left') 

    
tela_inicial = tk.Tk()

tela_inicial.title("Senac pizzaria")
tela_inicial.geometry("400x200")

frame_pedidos = tk.Frame(tela_inicial)
frame_pedidos.grid(row=2, column=0,)

label_texto_pedidos = tk.Label(frame_pedidos, text="Pedidos:")
label_texto_pedidos.grid(row=0, column=0, pady=10)

botao_novo_pedido = tk.Button(frame_pedidos, text="Novo Pedido", command=novoPedido)
botao_novo_pedido.grid(row=1, column=0, padx=10)

botao_listar_pedidos = tk.Button(frame_pedidos, text="Lista de Pedidos", command=listarPedidos)
botao_listar_pedidos.grid(row=2, column=0, pady=10)

frame_clientes = tk.Frame(tela_inicial)
frame_clientes.grid(row=2, column=1, padx=10)

label_texto_clientes = tk.Label(frame_clientes, text="Clientes:")
label_texto_clientes.grid(row=0, column=0, pady=10)

botao_novo_cliente = tk.Button(frame_clientes, text="Novo Cliente", command=novoCliente)
botao_novo_cliente.grid(row=1, column=0)

botao_listar_clientes = tk.Button(frame_clientes, text="Lista de Clientes", command=listarClientes)
botao_listar_clientes.grid(row=2, column=0, pady=10)

tela_inicial.mainloop()