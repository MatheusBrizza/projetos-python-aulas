from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    assunto = models.CharField(max_length=50, choices=[
        ('DUVIDAS', 'Dúvidas/informações'),
        ('SOLICITACOES', 'Solicitações'),
        ('ELOGIOS', 'Elogios'),
        ('SUGESTOES', 'Sugestões'),
        ('RECLAMACOES', 'Reclamações')
    ])
    mensagem = models.TextField()
    
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=30)
# Create your models here.
