# Generated by Django 4.0 on 2022-02-16 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0026_alter_planejamento_turma_alter_planejamento_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 7, 38, 58, 798939), null=True),
        ),
    ]
