# Generated by Django 4.0 on 2021-12-24 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0011_alter_planejamento_data_envio_alter_resposta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='data_envio',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 24, 16, 10, 6, 824778), null=True),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 24, 16, 10, 6, 825400), null=True),
        ),
    ]
