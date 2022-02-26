from distutils import text_file
from statistics import mode
from django import views
from django.db import models
from Apps.usuarios.models import Usuario
from Apps.turmas.models import Escola
import datetime
# from Apps.tools import data_choices

class GradePlan(models.Model):

    # EMPHASIS_CHOICES = data_choices.GRADE_PLAN_EMPHASIS

    posted_by = models.ForeignKey(Usuario, verbose_name="posted_by", on_delete=models.PROTECT)
    # emphasis = models.CharField(max_length=1, choices=EMPHASIS_CHOICES)
    # grade = models.ForeignKey(Turma, verbose_name="grade", on_delete=models.PROTECT)
    school = models.ForeignKey(Escola, verbose_name="school", on_delete=models.PROTECT)
    lesson_month = models.DateField()
    document = models.CharField(max_length=254)
    description = models.CharField(max_length=254, blank=True, null=True)
    viewed = models.BooleanField(blank=True, null=True, default=False)
    creation_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    

class GradePlanComment(models.Model):
    class_plan = models.ForeignKey(GradePlan, verbose_name="grade_plan_comment", on_delete=models.PROTECT)
    message = models.CharField(max_length=254)
    posted_by = models.ForeignKey(Usuario, verbose_name="posted_by", on_delete=models.PROTECT)
    viewed = models.BooleanField(blank=True, null=True, default=False)
    creation_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
