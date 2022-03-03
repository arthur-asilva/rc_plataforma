from django.contrib import admin
from . import models

admin.site.register(models.Unidade)
admin.site.register(models.Escola)
admin.site.register(models.Turma)
admin.site.register(models.Courseware)
admin.site.register(models.Buildkit)