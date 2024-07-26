from django.shortcuts import render, redirect
from .forms import ContatoForm
from main_app.bd_config import conectarDB
from django.http import HttpResponseRedirect
from django.contrib import messages

def login(request):
    request.session['usuario_id'] = ""
    request.session['usuario_nome'] = ""
    try:
        if request.method == "POST":
            connector = conectarDB()
            
            nome = request.POST['nome']
            senha = request.POST['senha']
            
            cursor = connector.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE nome = %s AND senha = %s;', (nome, senha))
            usuario = cursor.fetchone()
            cursor.close()
            connector.close()
            
            if usuario:
                request.session['usuario_id'] = usuario[0]
                request.session['usuario_nome'] = usuario[1]
                return redirect('index')
            else:
                print('Nome de usuário ou senha inválidos')
                mensagem_erro = 'Nome de usuário ou senha inválidos.'
                return render(request, 'login.html', {'mensagem_erro': mensagem_erro})
        else:
            return render(request, 'login.html')
    except Exception as e:
        mensagem_erro = f"Erro ao conectar com banco de dados: {e}"
        return render(request, 'login.html', {'mensagem_erro': mensagem_erro})

def logout(request):
    request.session.flush()
    return redirect('index')

def index(request):
    
    return render(request, 'Guia/index.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                connector = conectarDB()

                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                assunto = form.cleaned_data['assunto']
                mensagem = form.cleaned_data['mensagem']

                cursor = connector.cursor()
                cursor.execute('INSERT INTO contatos (nome, email, assunto, mensagem, situacao) VALUES (%s, %s, %s, %s, %s);', (nome, email, assunto, mensagem, "Não atendido"))
                connector.commit()
                
                print('Contato realizado com sucesso!')
                return HttpResponseRedirect('/')
            except Exception as e:
                print(f'Erro ao salvar seu Contato: mensagem {e}')
                mensagem_erro = "Ocorreu um erro ao processar o seu pedido. Tente novamente mais tarde."
                return render(request, 'erro.html', mensagem_erro=mensagem_erro), 500
            finally:
                if connector is not None:
                    connector.close()
        else:
            return render(request, 'contato.html', {'form':form})
    else:
        form = ContatoForm()
        return render(request, 'contato.html', {'form':form})

def contatos(request):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        connector = conectarDB()
        cursor = connector.cursor()
        cursor.execute('SELECT * FROM contatos WHERE situacao != "Em atendimento" AND situacao != "Finalizado";')
        contatos = cursor.fetchall()
        return render(request, 'contatos.html', {"contatos":contatos})

def atendimento(request, id):
    usuario_id = request.session['usuario_id']
    try:
        connector = conectarDB()
        cursor = connector.cursor()
        cursor.execute('UPDATE contatos SET situacao = %s WHERE id = %s;', ("Em Atendimento", int(id)))
        cursor.execute('INSERT INTO usuario_contato (usuario_id, contato_id, situacao) VALUES(%s, %s, %s);', (int(usuario_id), int(id), "Em Atendimento"))
        connector.commit()
        connector.close()
    
        return redirect('/contatos')
    except Exception as e:
        print(f'Erro ao atender chamado: {e}')
        return redirect('/contato')

def listar_meus_contatos(request):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        usuario_id = request.session.get('usuario_id')
        connector = conectarDB()
        cursor = connector.cursor()
        cursor.execute('SELECT contatos.* FROM contatos INNER JOIN usuario_contato ON usuario_contato.contato_id = contatos.id WHERE usuario_contato.usuario_id = %s ORDER BY contatos.id;', (usuario_id,),)
        contatos = cursor.fetchall()
        return render(request, 'meus_contatos.html', {"contatos":contatos})

def finalizar_contato(request, id):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        usuario_id = request.session.get('usuario_id')
        connector = conectarDB()
        cursor = connector.cursor()
        cursor.execute('UPDATE contatos SET situacao = %s WHERE id = %s;', ("Finalizado", int(id)))
        connector.commit()
        cursor.execute('UPDATE usuario_contato SET situacao = %s WHERE usuario_id = %s AND contato_id = %s;', ("Finalizado", int(usuario_id), int(id)))
        connector.commit()
        return redirect('meus_contatos')

def listar_usuarios(request):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        connector = conectarDB()
        cursor = connector.cursor()
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        
        return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def novo_usuario(request):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        if request.method == 'POST':
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            
            connector = conectarDB()
            cursor = connector.cursor()
            cursor.execute('INSERT INTO usuarios SET nome = %s, email = %s, senha = %s;', (nome, email, senha))
            connector.commit()
            cursor.close()
            connector.close()
            
            return redirect('index')
        
        return render(request, 'novo_usuario.html')
    
def editar_usuario(request, id):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        connector = conectarDB()
        cursor = connector.cursor()
        cursor.execute('SELECT id, nome, email FROM usuarios WHERE id = %s;', (id,))
        connector.close()
        
        if request.method == 'POST':
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            if not all([nome, email, senha]):
                return render(request, 'lista_usuarios.html')
            connector = conectarDB()
            cursor = connector.cursor()
            cursor.execute('UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s;', (nome, email, senha, id))
            connector.commit()
            cursor.close()
            connector.close()
            
            return redirect('listar_usuarios')
        return render(request, 'editar_usuario.html', {'id': id})

def excluir_usuario(request, id):
    if not request.session.get('usuario_id'):
        return redirect('login')
    else:
        try:
            connector = conectarDB()
            cursor = connector.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = %s;', (id,))
            connector.commit()
            cursor.close()
            connector.close()
            
            messages.success(request, 'Usuário deletado com sucesso!')
            return redirect('listar_usuarios')
        
        except Exception as e:
            print(f'Falha ao deletar usuário: {e}')
            messages.error(request, f'Falha ao deletar usuario {e}')
            return redirect('index')
