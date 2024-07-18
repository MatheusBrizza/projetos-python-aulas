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
                cursor.execute('INSERT INTO pedidos (nome, email, pedido) VALEUS (%s, %s, %s);', (nome, email, pedido))
                connector.commit()
                
                print('Pedido realizado com sucesso!')
                return HttpResponseRedirect('/')
            except Exception as e:
                
# Create your views here.
