# Generated by Django 4.0 on 2022-02-08 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0008_alter_chat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 7, 21, 24, 31, 118264), null=True),
        ),
    ]
