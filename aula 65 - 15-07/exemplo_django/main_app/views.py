from django.shortcuts import render, redirect
from .forms import ContatoForm
from main_app.bd_config import conectarDB
from django.http import HttpResponseRedirect

def login(request):
    request.session['usuario_id'] = ""
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
                mensagem = form.cleaned_data['mensagem']
                
                cursor = connector.cursor()
                cursor.execute('INSERT INTO contatos (nome, email, mensagem, situacao) VALUES (%s, %s, %s, %s);', (nome, email, mensagem, "Não atendido"))
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
        cursor.execute('UPDATE contatos SET situacao = %s WHERE contato_id = %s;', ("Em Atendimento", int(id)))
        cursor.execute('INSERT INTO usuario_contato (usuario_id, contato_id, situacao) VALUES(%s, %s, %s);', (int(usuario_id), int(id), "Em Atendimento"))
        connector.commit()
        connector.close()
    
        return redirect('/contatos')
    except Exception as e:
        print(f'Erro ao atender chamado: {e}')
        return redirect('/contato')

