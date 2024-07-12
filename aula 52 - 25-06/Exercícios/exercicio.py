import io
import reportlab
from flask import Flask, render_template, redirect, url_for, session, request, flash, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from config_bd import conectarBD
from io import BytesIO
from xlsxwriter import Workbook
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)
app.config['SECRET_KEY'] = "wompity womp"

class FormularioPedido(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()], render_kw={"placeholder":"Nome"})
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()], render_kw={"placeholder":"Email"})
    pedido = StringField('Pedido:', validators=[validators.DataRequired()], render_kw={"placeholder":"Pedido"})
    
class FormularioAtendente(FlaskForm):
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
    executor_sql.execute("""SELECT * FROM atendentes WHERE nome = %s AND senha = %s """, (nome, senha,))
    usuario = executor_sql.fetchone()
    executor_sql.close()
    connector.close()
    
    if usuario:
        session['usuario_id'] = usuario[0]
        return redirect(url_for('index'))
    else:
        return redirect(url_for('pagina_login'))

@app.route('/homepage')
def index():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

# Telas contatos
@app.route('/pedido', methods=['GET', 'POST'])
def pedido():
    form = FormularioPedido()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        pedido = form.pedido.data

        try:
            connector = conectarBD()
            
            executor_sql = connector.cursor()
            comando_sql = "INSERT INTO pedidos (nome, email, pedido) VALUES (%s, %s, %s)"
            values = (nome, email, pedido)
            executor_sql.execute(comando_sql, values)
            connector.commit()
            
            print("Salvo com sucesso!")
        except connector.connector.Error as e:
            print(f"Falha ao salvar dados! {e}")
            mensagem_erro = "Ocorreu um erro ao processar o seu pedido. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
        finally:
            if connector is not None:
                connector.close()
            return redirect('/sucesso')
    else:
        return render_template("pedido.html", form=form)


@app.route('/sucesso')
def sucesso():
    return render_template("sucesso.html")

@app.errorhandler(Exception)
def erro_geral(e):
    mensagem_erro = str(e)
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500

@app.route('/lista_pedidos')
def listar_pedidos():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    
    connector = conectarBD()
    executor_sql = connector.cursor()
    executor_sql.execute('SELECT * FROM pedidos where situacao!="Em atendimento" AND situacao!="Finalizado";')
    pedidos = executor_sql.fetchall()
    return render_template("pedidos.html", pedidos=pedidos)# achar como mudar para pedidos

@app.route('/atendercontato/<id>', methods = ['GET', 'POST'])
def atendercontato(id):
    
    usuario_id = session.get('usuario_id')
    try:
        connector = conectarBD()
        executor_sql = connector.cursor()
        
        sql = 'UPDATE pedidos SET situacao = %s WHERE id = %s;'
        valores = ("Em atendimento", int(id))
        executor_sql.execute(sql, valores)
        connector.commit()

        comando_sql = 'INSERT INTO atendente_pedido (atendente_id, pedido_id, situacao) VALUES (%s, %s, %s);'
        valores = (int(usuario_id), int(id), "Em atendimento")
        executor_sql.execute(comando_sql, valores)
        connector.commit()
        return redirect(url_for('listar_pedidos'))
    except Exception as e:
        return render_template('erro_geral', mensagem=str(e))

@app.route('/meus_pedidos')
def listar_meus_pedidos():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    
    usuario_id = session.get('usuario_id')
    connector = conectarBD()
    executor_sql = connector.cursor()
    executor_sql.execute(' SELECT pedidos.* FROM pedidos INNER JOIN atendente_pedido ON atendente_pedido.pedido_id = pedidos.id WHERE atendente_pedido.atendente_id = %s order by pedidos.id ', (usuario_id,),)
    contatos = executor_sql.fetchall()
    return render_template("meuspedidos.html", contatos=contatos) 

    
@app.route('/finalizar_pedido/<id>', methods= ['GET', 'POST'])
def finalizar_pedido(id):
    usuario_id = session.get('usuario_id')
    try:
        connector = conectarBD()
        executor_sql = connector.cursor()
        
        sql = 'UPDATE pedidos SET situacao = %s WHERE id = %s;'
        valores = ("Finalizado", int(id))
        executor_sql.execute(sql, valores)
        connector.commit()

        comando_sql = 'UPDATE atendente_pedido SET situacao = %s WHERE atendente_id = %s AND pedido_id = %s;'
        valores = ("Finalizado", int(usuario_id), int(id))
        executor_sql.execute(comando_sql, valores)
        connector.commit()
        return redirect(url_for('listar_meus_pedidos'))
    except Exception as e:
        return render_template('erro_geral', mensagem=str(e))
    
# Telas usuários
@app.route('/usuarios')
def usuarios():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))
    connector = conectarBD()
    executor_sql = connector.cursor()
    executor_sql.execute('SELECT * FROM atendentes')
    usuarios = executor_sql.fetchall()
    return render_template("usuarios.html", usuarios=usuarios)


@app.route('/novousuario', methods=['GET', 'POST'])
def novousuario():
    if not session.get('usuario_id'):
        return redirect(url_for('pagina_login'))

    form = FormularioAtendente()
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
    
        connector = conectarBD()
        
        executor_sql = connector.cursor()
        executor_sql.execute('SELECT COUNT(*) FROM atendentes WHERE email = %s;', (email,))
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
                comando_sql = 'INSERT INTO atendentes (nome, email, senha) VALUES (%s, %s, %s)'
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
    executor_sql.execute("""SELECT id, nome, email FROM atendentes WHERE id = %s;""", (id,))
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
        comando_sql = 'UPDATE atendentes SET nome = %s, email = %s, senha = %s WHERE id = %s;'
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
        executor_sql.execute("""DELETE FROM atendentes WHERE id = %s;""", (id,))
        connector.commit()
        executor_sql.close()
        connector.close()

        return redirect(url_for('usuarios'))
    except connector.connector.Error as e:
        return render_template('excluirusuario.html', error=str(e))

# gerador relatórios
@app.route('/relatorios_excel')
def gerar_relatorio_excel():
    usuario_id = session.get('usuario_id')
    
    connector = conectarBD()
    executor_sql = connector.cursor()
    
    executor_sql.execute('SELECT pedidos.* FROM pedidos INNER JOIN atendente_pedido ON atendente_pedido.pedido_id = pedidos.id WHERE atendente_pedido.atendente_id = %s order by pedidos.id', (usuario_id,),)

    data = []
    for row in executor_sql.fetchall():
        data.append(row)
    
    output = io.BytesIO()
    workbook = Workbook(output)
    worksheet = workbook.add_worksheet()
    
    worksheet.write('A1', 'ID')
    worksheet.write('B1', 'Nome')
    worksheet.write('C1', 'Email')
    worksheet.write('D1', 'Pedido')
    
    for i, row in enumerate(data):
        worksheet.write(i +1, 0, row[0])
        worksheet.write(i +1, 1, row[1])
        worksheet.write(i +1, 2, row[2])
        worksheet.write(i +1, 3, row[3])
    
    workbook.close()
    output.seek(0)
    
    resposta = make_response(output.read())
    resposta.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    resposta.headers['Content-Disposition'] = 'attachment; filename=relatorio_contatos.xlsx'
    
    return resposta

@app.route('/relatorios_pdf')
def gerar_relatorio_pdf():
    usuario_id = session.get('usuario_id')
    
    connector = conectarBD()
    executor_sql = connector.cursor()
    
    executor_sql.execute('SELECT pedidos.* FROM pedidos INNER JOIN atendente_pedido ON atendente_pedido.pedido_id = pedidos.id WHERE atendente_pedido.atendente_id = %s order by pedidos.id', (usuario_id,),)
    
    data = executor_sql.fetchall()
    
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setTitle('Relatório de Pedidos')
    
    c.setFont('Times-Roman', 15)
    c.drawString(25, 725, 'ID')
    c.drawString(100, 725, 'Nome')
    c.drawString(200, 725, 'Email')
    c.drawString(300, 725, 'Pedido')
    
    for i, row in enumerate(data):
        y = 700 - i * 25
        c.setFont('Times-Roman', 10)
        c.drawString(25, y, str(row[0]))
        c.drawString(100, y, str(row[1]))
        c.drawString(200, y, str(row[2]))
        c.drawString(300, y, str(row[3]))
    
    c.save()
    
    pdf_content = buffer.getvalue()
    
    resposta = make_response(pdf_content)
    resposta.headers['Content-Type'] = 'application/pdf'
    resposta.headers['Content-Disposition'] = 'attachment; filename=relatorio.pdf'
    
    return resposta
    
if __name__ == '__main__':
    app.run