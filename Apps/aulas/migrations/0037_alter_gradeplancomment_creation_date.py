# Generated by Django 4.0 on 2022-03-02 22:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0036_gradeplan_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradeplancomment',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 2, 19, 41, 49, 590873), null=True),
        ),
    ]
