# Generated by Django 4.0 on 2022-03-02 22:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0037_alter_gradeplancomment_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeplancomment',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 2, 19, 59, 6, 960283), null=True),
        ),
    ]