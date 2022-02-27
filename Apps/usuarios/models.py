from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=254)
    foto = models.CharField(max_length=254, blank=True, null=True, default='../media/Usuarios/default_user.jpeg')
    grupo = models.ForeignKey("Grupo", verbose_name="grupo", on_delete=models.SET_NULL, blank=True, null=True)
    email = models.CharField(max_length=254)
    senha = models.CharField(max_length=254)
    segmentos = models.CharField(max_length=254)
    nivel = models.IntegerField(default=1, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    formacao = models.CharField(max_length=254, blank=True, null=True)
    status = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField(max_length=254)
    acessos = models.TextField()

    def __str__(self):
        return self.nome