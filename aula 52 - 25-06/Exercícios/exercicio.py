from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from config_bd import conectarBD


app = Flask(__name__)
app.config['SECRET_KEY'] = "segredo"

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()], render_kw={"placeholder":"Nome"})
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Email"})
    mensagem = StringField('Mensagem:', validators=[validators.DataRequired()], render_kw={"placeholder":"Mensagem"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    session.pop('usuario_id', None)
    #continuar
    

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

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

if __name__ == '__main__':
    app.run