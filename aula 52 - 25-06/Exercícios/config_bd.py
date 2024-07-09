import mysql.connector

nome_db = "senac_pizzaria"
tb_contatos = "contatos"
tb_usuarios = "usuarios"
tb_usuario_contato = "usuario_contato"
def conectarBD():
    connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=''
    )

    executor_comando_sql = connector.cursor()
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
    # verificando se já existe a tabela contatos
    connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database= nome_db  
    )

    executor_comando_sql = connector.cursor() # também é necessário reiniciar a variável pois também senão dá o erro ReferenceError: weakly-referenced object no longer exists já que a variável anterior se referia apenas ao uso para procurar o banco de dados 
    executor_comando_sql.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_db}'  AND table_name = '{tb_contatos}');")
    resultado_tb = executor_comando_sql.fetchone()[0]
    connector.close()

    if resultado_tb > 0:
        print(f"tabela {tb_contatos} já existe!")
    else:
        print("criando tabela contatos")
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
        executor_comando_sql = connector.cursor()
        executor_comando_sql.execute('CREATE TABLE contatos (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,mensagem TEXT NOT NULL);')
        connector.commit()
        connector.close()
 
    # verificando se já existe a tabela usuários    
    connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database= nome_db  
    )
        
    executor_comando_sql = connector.cursor() # também é necessário reiniciar a variável pois também senão dá o erro ReferenceError: weakly-referenced object no longer exists já que a variável anterior se referia apenas ao uso para procurar o banco de dados 
    executor_comando_sql.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_db}'  AND table_name = '{tb_usuarios}');")
    resultado_tb = executor_comando_sql.fetchone()[0]
    connector.close()

    if resultado_tb > 0:
        print(f"tabela {tb_usuarios} já existe!")
    else:
        print("criando tabela usuários")
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
        executor_comando_sql = connector.cursor()
        executor_comando_sql.execute('CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255),senha VARCHAR(255));')
        connector.commit()
        
        nome="ADMIN"
        email="a@a.com"
        senha="admin123"
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (nome, email, senha)
        executor_comando_sql.execute(sql, valores)
        connector.commit()
        connector.close()

        # verificando se já existe tabela usuario-contato
    connector = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database= nome_db  
    )

    executor_comando_sql = connector.cursor() # também é necessário reiniciar a variável pois também senão dá o erro ReferenceError: weakly-referenced object no longer exists já que a variável anterior se referia apenas ao uso para procurar o banco de dados 
    executor_comando_sql.execute(f"SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_schema = '{nome_db}'  AND table_name = '{tb_usuario_contato}');")
    resultado_tb = executor_comando_sql.fetchone()[0]
    connector.close()

    if resultado_tb > 0:
        print(f"tabela {tb_usuario_contato} já existe!")
    else:
        print("criando tabela contatos")
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
        executor_comando_sql = connector.cursor()
        executor_comando_sql.execute('CREATE TABLE usuario_contato (usuario_id INT NOT NULL, contato_id INT NOT NULL, PRIMARY KEY (usuario_id, contato_id), FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE, FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE);')
        connector.commit()
        connector.close()
            
    try:
        connector = mysql.connector.connect(host='127.0.0.1',user='root',password='',database= nome_db)
    except mysql.connector.Error as e:
        print("Erro de conexão com banco de dados:", e)
        raise
    return connector