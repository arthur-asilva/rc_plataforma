from django.db import models
from Apps.usuarios.models import Usuario
from Apps.tools.data_choices import GRADE_SHIFTS

class Unidade(models.Model):
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.cidade}/{self.estado}"



class Escola(models.Model):
    nome = models.CharField(max_length=254)
    endereco = models.CharField(max_length=254)
    responsavel = models.CharField(max_length=254)
    contato = models.CharField(max_length=254)
    unidade = models.ForeignKey(Unidade, verbose_name="unidade", on_delete=models.PROTECT)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome}, {self.unidade}"



class Turma(models.Model):

    nome = models.CharField(max_length=254)
    escola = models.ForeignKey(Escola, verbose_name="escola", on_delete=models.PROTECT)
    quantidade_alunos = models.IntegerField()
    professor = models.ForeignKey(Usuario, verbose_name="professor", on_delete=models.SET_NULL, blank=True, null=True)
    turno = models.CharField(max_length=2, choices=GRADE_SHIFTS)
    livro = models.CharField(max_length=254, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        shift_index = list(zip(*GRADE_SHIFTS))[0].index(self.turno)
        return f"{self.nome}, {self.escola.nome}/{GRADE_SHIFTS[shift_index][1]}"