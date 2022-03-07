from pyexpat import model
from django.db import models
from Apps.usuarios.models import Usuario
from Apps.tools.data_choices import GRADE_SHIFTS, WEAK_DAYS

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
    professor = models.ForeignKey(Usuario, verbose_name="professor", on_delete=models.SET_NULL, blank=True, null=True)
    turno = models.CharField(max_length=2, choices=GRADE_SHIFTS)
    dia_aula = models.CharField(max_length=254, choices=WEAK_DAYS, blank=True, null=True)
    complemento = models.CharField(max_length=10, blank=True, null=True)
    ordem_aula = models.IntegerField()
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        shift_index = list(zip(*GRADE_SHIFTS))[0].index(self.turno)
        return f"{self.nome}, {self.escola.nome}/{GRADE_SHIFTS[shift_index][1]}"


class Buildkit(models.Model):
    name = models.CharField(max_length=150)
    components = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Courseware(models.Model):
    class_grade = models.ForeignKey(Turma, related_name="class_grade", on_delete=models.PROTECT)
    book_1 = models.CharField(max_length=254, blank=True, null=True)
    book_2 = models.CharField(max_length=254, blank=True, null=True)
    buildkit_1 = models.ForeignKey(Buildkit, related_name="buildkit_1", on_delete=models.PROTECT)
    buildkit_2 = models.ForeignKey(Buildkit, related_name="buildkit_2", on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=True, null=True)
    distribution_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.class_grade.nome} from  {self.class_grade.escola.nome}, {self.distribution_year}"