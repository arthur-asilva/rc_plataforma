# Generated by Django 4.0 on 2021-12-23 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0009_alter_planejamento_data_envio_alter_resposta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_envio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 23, 19, 8, 9, 227399), null=True),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 23, 19, 8, 9, 228250), null=True),
        ),
    ]