# Generated by Django 4.0 on 2021-12-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_nivel_usuario_segmentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='segmentos',
            field=models.CharField(max_length=254),
        ),
    ]
