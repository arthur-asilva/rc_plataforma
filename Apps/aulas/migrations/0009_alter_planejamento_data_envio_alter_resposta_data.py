# Generated by Django 4.0 on 2021-12-23 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0008_planejamento_visto_resposta_visto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_envio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 23, 15, 27, 27, 235238), null=True),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 23, 15, 27, 27, 236053), null=True),
        ),
    ]
