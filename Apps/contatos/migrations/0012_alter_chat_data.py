# Generated by Django 4.0 on 2022-02-16 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0011_alter_chat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 7, 33, 18, 470348), null=True),
        ),
    ]
