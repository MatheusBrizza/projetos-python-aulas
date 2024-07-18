import mysql.connector

nome_bd = "senac_pizzaria"
tb_pedidos = "pedidos"
tb_usuarios = "usuarios"
tb_usuario_pedido = "usuario_pedido"

def conectarDB():
    # Verificando e criando banco de dados
    connector = mysql.connector.connect(host='127.0.0.1', user='root', password='')
    
    cursor = connector.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM information.schema.SCHEMATA WHERE SCHEMA_NAME = {nome_bd};')
    resultado_bd = cursor.fetchone[0]
    connector.close()
    
    if resultado_bd > 0:
        print(f"Banco de dados {nome_bd} já existe e está pronto para uso.")
    else:
        print(f"Criando banco de dados {nome_bd}")

        connector = mysql.connector.connect(host='127.0.0.1', user='root', password='', database=nome_bd)
        
        cursor = connector.cursor()
        cursor.execute(f'CREATE DATABASE {nome_bd}')
        connector.commit()
        connector.close()
    
    #Verificando e criando tabela pedidos
    connector = mysql.connector.connect(host='127.0.0.1', user='root', password='', database=nome_bd)
    cursor = connector.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_bd}'  AND table_name = '{tb_pedidos}');")
    resultado_tb = cursor.fetchone[0]
    connector.close()

    if resultado_tb > 0:
        print(f"tabela {tb_pedidos} já existe!")
    else:
        print("criando tabela pedidos")
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_bd)
        cursor = connector.cursor()
        cursor.execute('CREATE TABLE pedidos (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,pedido TEXT NOT NULL, situacao VARCHAR(255) NOT NULL);')
        connector.commit()
        connector.close()
    
    # Verificando e criando tabela usuarios
    connector = mysql.connector.connect(host='127.0.0.1', user='root', password='', database= nome_bd)
    cursor = connector.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_bd}' AND table_name = '{tb_usuarios}');")
    resultado_tb = cursor.fetchone[0]
    connector.close()
    
    if resultado_tb > 0:
        print(f"tabela {tb_usuarios} já existe!")
    else:
        print("Criando tabela usuarios")
        connector = mysql.connector.connect(host='127.0.0.1', user='root', password='', database= nome_bd)
        cursor = connector.cursor()
        cursor.execute('CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255),senha VARCHAR(255));')
        connector.commit()
        
        nome="ADMIN"
        email="admin@a.com"
        senha="admin123"
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        connector.commit()
        connector.close()
    
    # Verificando e criando tabela usuario_pedido    
    connector = mysql.connector.connect(host='127.0.0.1', user='root', password='', database= nome_bd)

    cursor = connector.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_bd}'  AND table_name = '{tb_usuario_pedido}');")
    resultado_tb = cursor.fetchone[0]
    connector.close()
    
    if resultado_tb > 0:
        print(f"tabela {tb_usuario_pedido} já existe!")
    else:
        print("Criando tabela usuario_pedido")
        connector = mysql.connector.connect(host='127.0.0.1', user='root', password='', database= nome_bd)
        cursor = connector.cursor()
        cursor.execute('CREATE TABLE usuario_pedido (usuario_id INT NOT NULL, pedido_id INT NOT NULL, situacao VARCHAR(255) NOT NULL, PRIMARY KEY (usuario_id, pedido_id), FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE, FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON DELETE CASCADE);')
        connector.commit()
        connector.close()
    try:
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_bd)
    except mysql.connector.Error as e:
        print("Erro de conexão com banco de dados:", e)
        raise
    return connector
    