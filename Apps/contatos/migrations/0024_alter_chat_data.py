# Generated by Django 4.0 on 2022-03-02 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0023_alter_chat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 2, 19, 41, 49, 592024), null=True),
        ),
    ]
