from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from config_bd import conectarBD


app = Flask(__name__)
app.config['SECRET_KEY'] = "segredo"

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = StringField('Mensagem:', validators=[validators.DataRequired()])

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
            
    
    return render_template("contato.html")

if __name__ == '__main__':
    app.run