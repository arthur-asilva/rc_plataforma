# Generated by Django 4.0 on 2022-02-10 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_usuario_formacao_usuario_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='formacao',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.grupo', verbose_name='grupo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
