# Generated by Django 4.0 on 2021-12-22 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0006_resposta_usuario_alter_planejamento_data_envio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_envio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 22, 20, 6, 52, 449640), null=True),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 22, 20, 6, 52, 450411), null=True),
        ),
    ]
