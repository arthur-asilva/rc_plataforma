# Generated by Django 4.0 on 2022-02-16 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0030_alter_resposta_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 10, 7, 32, 906758), null=True),
        ),
    ]
