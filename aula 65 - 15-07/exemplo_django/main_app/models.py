from django.db import models

class Pedido(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    pedido = models.TextField()
# Create your models here.
