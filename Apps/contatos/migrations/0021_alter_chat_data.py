# Generated by Django 4.0 on 2022-02-24 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0020_alter_chat_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 24, 15, 48, 12, 831074), null=True),
        ),
    ]
