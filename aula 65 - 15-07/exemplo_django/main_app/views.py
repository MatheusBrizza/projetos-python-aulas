from django.shortcuts import render
from .forms import PedidoForm
from main_app.bd_config import conectarDB
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'Guia/index.html')

def contato(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            try:
                connector = conectarDB()
                
                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                pedido = form.cleaned_data['pedido']
                
                cursor = connector.cursor()
                cursor.execute('INSERT INTO pedidos (nome, email, pedido, situacao) VALUES (%s, %s, %s, %s);', (nome, email, pedido, "Não atendido"))
                connector.commit()
                
                print('Pedido realizado com sucesso!')
                return HttpResponseRedirect('/')
            except Exception as e:
                print(f'Erro ao salvar seu pedido: mensagem {e}')
                mensagem_erro = "Ocorreu um erro ao processar o seu pedido. Tente novamente mais tarde."
                return render(request, 'erro.html', mensagem_erro=mensagem_erro), 500
            finally:
                if connector is not None:
                    connector.close()
        else:
            return render(request, 'contato.html', {'form':form})
    else:
        form = PedidoForm()
        return render(request, 'contato.html', {'form':form})
