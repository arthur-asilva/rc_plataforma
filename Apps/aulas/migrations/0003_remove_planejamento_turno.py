# Generated by Django 4.0 on 2021-12-19 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0002_planejamento_turno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planejamento',
            name='turno',
        ),
    ]