from django.db import models

# Create your models here.

class Camisa(models.Model):
    time = models.CharField(max_length=30)
    jogador = models.CharField(max_length=15)
    numero = models.CharField(max_length=3)
    tamanho = models.CharField(max_length=1)
