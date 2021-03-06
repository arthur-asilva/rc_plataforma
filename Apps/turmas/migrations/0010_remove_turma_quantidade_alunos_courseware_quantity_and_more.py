# Generated by Django 4.0 on 2022-03-03 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0009_buildkit_remove_turma_livro_1_remove_turma_livro_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turma',
            name='quantidade_alunos',
        ),
        migrations.AddField(
            model_name='courseware',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='turma',
            name='complemento',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='courseware',
            name='distribution_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='dia_aula',
            field=models.CharField(blank=True, choices=[('1', 'Segunda'), ('2', 'Terça'), ('3', 'Quarta'), ('4', 'Quinta'), ('5', 'Sexta'), ('6', 'Sábado')], max_length=254, null=True),
        ),
    ]
