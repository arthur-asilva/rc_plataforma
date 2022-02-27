from django.db import models
from Apps.usuarios.models import Usuario


class Tutorial(models.Model):
    indice = models.IntegerField()
    nome = models.CharField(max_length=254)
    turma = models.CharField(max_length=254)
    video = models.CharField(max_length=254)
    plano_1 = models.CharField(max_length=254)
    plano_2 = models.CharField(max_length=254)
    programacao = models.CharField(max_length=254)



class Complemento(models.Model):
    nome = models.CharField(max_length=254)
    arquivo = models.CharField(max_length=254, blank=True, null=True)
    video = models.CharField(max_length=254, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    postado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(auto_now_add=True, blank=True, null=True)