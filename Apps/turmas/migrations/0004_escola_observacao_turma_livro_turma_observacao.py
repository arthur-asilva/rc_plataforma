# Generated by Django 4.0 on 2022-01-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0003_turma_turno_alter_turma_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='escola',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='livro',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='observacao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
