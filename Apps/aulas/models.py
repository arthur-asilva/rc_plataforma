from distutils import text_file
from statistics import mode
from django.db import models
from Apps.turmas.models import Turma
from Apps.usuarios.models import Usuario
from Apps.turmas.models import Turma
import datetime

class Planejamento(models.Model):

    EMPHASIS_CHOICES = (
        ("T", "Técnico"),
        ("P", "Propedêutico")
    )

    usuario = models.ForeignKey(Usuario, verbose_name="usuario", on_delete=models.PROTECT)
    enfase = models.CharField(max_length=1, choices=EMPHASIS_CHOICES)
    turma = models.ForeignKey(Turma, verbose_name="turma", on_delete=models.PROTECT)
    data = models.DateField()
    tema = models.CharField(max_length=254)
    objetivo = models.TextField()
    visto = models.BooleanField(default=False, blank=True, null=True)
    data_envio = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    

class Resposta(models.Model):
    planejamento = models.ForeignKey(Planejamento, verbose_name="planejamento", on_delete=models.PROTECT)
    mensagem = models.TextField(blank=True, null=True)
    visto = models.BooleanField(default=False, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, verbose_name="usuario", on_delete=models.PROTECT)
    data = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
