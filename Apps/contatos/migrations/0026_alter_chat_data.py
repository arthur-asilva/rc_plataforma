# Generated by Django 4.0 on 2022-03-03 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0025_alter_chat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 16, 23, 40, 938228), null=True),
        ),
    ]
