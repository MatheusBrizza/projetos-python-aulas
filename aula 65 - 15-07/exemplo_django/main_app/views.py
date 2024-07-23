from django.shortcuts import render
from .forms import ContatoForm
from main_app.bd_config import conectarDB
from django.http import HttpResponseRedirect

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
    connector = conectarDB()
    cursor = connector.cursor()
    cursor.execute('SELECT * FROM contatos WHERE situacao != "Em atendimento" AND situacao != "Finalizado";')
    contatos = cursor.fetchall()
    return render(request, 'contatos.html', {"contatos":contatos})