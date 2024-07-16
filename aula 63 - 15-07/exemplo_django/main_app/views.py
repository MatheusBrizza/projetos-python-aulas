from django.shortcuts import render

def index(request):
    return render(request, 'Guia/index.html')

# Create your views here.
