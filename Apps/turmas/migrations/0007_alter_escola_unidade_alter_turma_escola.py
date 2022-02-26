# Generated by Django 4.0 on 2022-02-16 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0006_alter_turma_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escola',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turmas.unidade', verbose_name='unidade'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='escola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turmas.escola', verbose_name='escola'),
        ),
    ]