"""
URL configuration for exemplo_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('contatos/', views.contatos, name='contatos'),
    path('atender_contato/<int:id>/', views.atendimento, name='atendimento'),
    path('meus_contatos/', views.listar_meus_contatos, name='meus_contatos'),
    path('finalizar_atendimento/<int:id>', views.finalizar_atendimento, name='finalizar_atendimento'),
    path('mostrar_resposta/<int:id>', views.mostrar_resposta, name='mostrar_resposta'),
    path('lista_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('novo_usuario/', views.novo_usuario, name='novo_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('excluir_usuario/<int:id>', views.excluir_usuario, name='excluir_usuario'),

]
