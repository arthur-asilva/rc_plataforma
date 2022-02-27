from django.db import models
from Apps.usuarios.models import Usuario
import datetime
from computedfields.models import ComputedFieldsModel, computed

class Chat(ComputedFieldsModel):
    de_usuario = models.ForeignKey(Usuario, related_name="de_usuario", on_delete=models.CASCADE)
    para_usuario = models.ForeignKey(Usuario, related_name="para_usuario", on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=254)
    data = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    visto = models.BooleanField(blank=True, null=True, default=False)

    @computed(models.CharField(max_length=50), depends=[['self', ['data']]])
    def data_str(self):
        return self.data.strftime("%m/%d/%Y, %H:%M:%S")
