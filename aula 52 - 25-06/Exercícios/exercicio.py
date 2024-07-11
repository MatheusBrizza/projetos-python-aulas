from flask import Flask, render_template, redirect, url_for, session, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from config_bd import conectarBD


app = Flask(__name__)
app.config['SECRET_KEY'] = "segredo"

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()], render_kw={"placeholder":"Nome"})
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Email"})
    mensagem = StringField('Mensagem:', validators=[validators.DataRequired()], render_kw={"placeholder":"Mensagem"})
    
class FormularioUsuario(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()], render_kw={"placeholder":"Nome"})
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Email"})
    senha = PasswordField('Senha:', validators=[validators.DataRequired()], render_kw={"placeholder":"Senha"})


@app.route('/', methods=['GET', 'POST'])
def pagina_login():
    session.clear()
    session.pop('usuario_id', None)
    return render_template("login.html")
    
@app.route('/validarlogin', methods=["POST", "GET"])
def validar_login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    
    connector = conectarBD()
    
    executor_sql = connector.cursor()
    executor_sql.execute("""SELECT * FROM usuarios WHERE nome = %s AND senha = %s """, (nome, senha,))
    usuario = executor_sql.fetchone()
    executor_sql.close()
    connector.close()
    
    if usuario:
        session['usuario_id'] = usuario[0]
        return redirect(url_for('index'))
    else:
        return redirect(url_for('pagina_login'))

@app.route('/paginainicial')
def index():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

# Telas contatos
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = FormularioContato()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        mensagem = form.mensagem.data

        try:
            connector = conectarBD()
            
            executor_sql = connector.cursor()
            comando_sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
            values = (nome, email, mensagem)
            executor_sql.execute(comando_sql, values)
            connector.commit()
            
            print("Salvo com sucesso!")
        except connector.connector.Error as e:
            print(f"Falha ao salvar dados! {e}")
            mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
        finally:
            if connector is not None:
                connector.close()

        return redirect('/sucesso')
    else:
        return render_template("contato.html", form=form)


@app.route('/sucesso')
def sucesso():
    return render_template("sucesso.html")

@app.errorhandler(Exception)
def erro_geral(e):
    mensagem_erro = str(e)
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500

@app.route('/contatos')
def contatos():
    connector = conectarBD()
    executor_sql = connector.cursor()
    executor_sql.execute('SELECT * FROM contatos')
    contatos = executor_sql.fetchall()
    return render_template("contatos.html", contatos=contatos)

@app.route('/atendercontato/<id>', methods = ['GET', 'POST'])
def atendercontato(id):
    
    usuario_id = session.get('usuario_id')
    try:
        connector = conectarBD()
        executor_sql = connector.cursor()
        
        sql = 'UPDATE contatos SET situacao = %s WHERE id = %s;'
        valores = ("Em atendimento", int(id))
        executor_sql.execute(sql, valores)
        connector.commit()

        comando_sql = 'INSERT INTO usuario_contato (usuario_id, contato_id, situacao) VALUES (%s, %s, %s);'
        valores = (int(usuario_id), int(id), "Em atendimento")
        executor_sql.execute(comando_sql, valores)
        connector.commit()
        return redirect(url_for('contatos'))
    except Exception as e:
        return render_template('erro_geral', mensagem=str(e))

@app.route('/meuscontatos')
def listarmeuscontatos():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    usuario_id = session.get('usuario_id')
    connector = conectarBD()
    executor_sql = connector.cursor()
    executor_sql.execute(' SELECT contatos.* FROM contatos INNER JOIN usuario_contato ON usuario_contato.contato_id = contatos.id WHERE usuario_contato.usuario_id = %s order by contatos.id ', (usuario_id,),)
    contatos = executor_sql.fetchall()
    return render_template("meuscontatos.html", contatos=contatos) 

    
@app.route('/finalizarcontato/<id>', methods= ['GET', 'POST'])
def finalizarcontato(id):
    usuario_id = session.get('usuario_id')
    try:
        connector = conectarBD()
        executor_sql = connector.cursor()
        
        sql = 'UPDATE contatos SET situacao = %s WHERE id = %s;'
        valores = ("Finalizado", int(id))
        executor_sql.execute(sql, valores)
        connector.commit()

        comando_sql = 'UPDATE usuario_contato SET situacao = %s WHERE usuario_id = %s AND contato_id = %s;'
        valores = ("Finalizado", int(usuario_id), int(id))
        executor_sql.execute(comando_sql, valores)
        connector.commit()
        return redirect(url_for('listarmeuscontatos'))
    except Exception as e:
        return render_template('erro_geral', mensagem=str(e))
    
# Telas usuários
@app.route('/usuarios')
def usuarios():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    connector = conectarBD()
    executor_sql = connector.cursor()
    executor_sql.execute('SELECT * FROM usuarios')
    usuarios = executor_sql.fetchall()
    return render_template("usuarios.html", usuarios=usuarios)


@app.route('/novousuario', methods=['GET', 'POST'])
def novousuario():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))

    form = FormularioUsuario()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
    
        connector = conectarBD()
        
        executor_sql = connector.cursor()
        executor_sql.execute('SELECT COUNT(*) FROM usuarios WHERE email = %s;', (email,))
        resultado_usuario = executor_sql.fetchone()[0]
        executor_sql.close()
        connector.close()

        if resultado_usuario > 0:
            flash('Email já cadastrado')
            return render_template('novousuario.html')
        else:
            try:
                connector = conectarBD()
                executor_sql = connector.cursor()
                comando_sql = 'INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)'
                valores = (nome, email, senha)
                executor_sql.execute(comando_sql, valores)
                connector.commit()
                executor_sql.close()
                connector.close()
                
                return redirect(url_for('usuarios'))
            except connector.connector.Error as e:
                print(f"Falha ao salvar dados! {e}")
                mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
                return render_template('erro.html', mensagem_erro = mensagem_erro), 500
            finally:
                if connector is not None:
                    connector.close()
    else:
        return render_template("novousuario.html", form=form)

@app.route('/editarusuario/<id>', methods=['GET', 'POST'])
def editarusuario(id):
    if not id.isdigit():
        return render_template('editarusuario/<id>', error='ID inválido')
    
    connector = conectarBD()
    
    executor_sql = connector.cursor()
    executor_sql.execute("""SELECT id, nome, email FROM usuarios WHERE id = %s;""", (id,))
    dados_usuario = executor_sql.fetchone()
    executor_sql.close()
    connector.close()
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome:
            flash('O nome é obrigatório.')
            return render_template('editarusuario/<id>', dados_usuario=dados_usuario)
        if not email:
            flash('O e-mail é obrigatório.')
            return render_template('editarusuario/<id>', dados_usuario=dados_usuario)
        if not senha:
            flash('A senha é obrigatória.')
            return render_template('editarusuario/<id>', dados_usuario=dados_usuario)
        
        connector = conectarBD()
        
        executor_sql = connector.cursor()
        comando_sql = 'UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s;'
        valores = (nome, email, senha, id)
        executor_sql.execute(comando_sql, valores)
        connector.commit()
        executor_sql.close()
        connector.close()
        
        return redirect(url_for('usuarios'))
    
    return render_template('editarusuario.html', id=id, dados_usuario=dados_usuario)
        
@app.route('/excluirusuario/<id>', methods= ['GET', 'POST'])
def excluirusuario(id):
    try:        
        connector = conectarBD()
        
        executor_sql = connector.cursor()
        executor_sql.execute("""DELETE FROM usuarios WHERE id = %s;""", (id,))
        connector.commit()
        executor_sql.close()
        connector.close()

        return redirect(url_for('usuarios'))
    except connector.connector.Error as e:
        return render_template('excluirusuario.html', error=str(e))



if __name__ == '__main__':
    app.run