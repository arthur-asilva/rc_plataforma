# Generated by Django 4.0 on 2022-02-16 10:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0005_alter_turma_professor'),
        ('usuarios', '0007_alter_usuario_formacao_alter_usuario_grupo_and_more'),
        ('aulas', '0025_rename_anexo_planejamento_tema_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turmas.turma', verbose_name='turma'),
        ),
        migrations.AlterField(
            model_name='planejamento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuario', verbose_name='usuario'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 16, 7, 34, 50, 389616), null=True),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='planejamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aulas.planejamento', verbose_name='planejamento'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.usuario', verbose_name='usuario'),
        ),
    ]
