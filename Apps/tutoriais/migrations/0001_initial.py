# Generated by Django 4.0 on 2021-12-19 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indice', models.IntegerField()),
                ('turma', models.CharField(max_length=150)),
                ('video', models.CharField(max_length=150)),
                ('plano_1', models.CharField(max_length=150)),
                ('plano_2', models.CharField(max_length=150)),
                ('programacao', models.CharField(max_length=150)),
            ],
        ),
    ]